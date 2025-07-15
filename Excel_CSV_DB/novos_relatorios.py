# novos_relatorios.py
# Requerimentos: pandas, matplotlib, seaborn, numpy, sqlite3, scipy, fpdf

import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from fpdf import FPDF
import os

def gerar_todos_relatorios_integrado(sqlite_database, general_entries_table, dir_file_out):
    # Verifica se o caminho de saída existe, se não cria
    if not os.path.exists(dir_file_out):
        os.makedirs(dir_file_out)

    output_dir = os.path.join(dir_file_out, 'relatorios_gerados')
    os.makedirs(output_dir, exist_ok=True)
    from datetime import datetime

    def load_general_entries(db_path, table_name):
        conn = sqlite3.connect(db_path)
        df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
        conn.close()
        return df

    def gerar_relatorio_tendencia(df, output_dir):
        tendencia = df.groupby(['AnoMes', 'TIPO'])['Debito'].sum().reset_index()
        pivot = tendencia.pivot(index='AnoMes', columns='TIPO', values='Debito').fillna(0)
        pivot.plot(figsize=(15, 6), marker='o')
        plt.title("Tendência de Gastos por Categoria")
        plt.ylabel("Total Debitado")
        plt.xticks(rotation=45)
        plt.tight_layout()
        file_path = os.path.join(output_dir, 'tendencia_gastos_por_categoria.png')
        plt.savefig(file_path)
        plt.close()
        return file_path

    def prever_gastos(df, output_dir):
        tipos = df['TIPO'].unique()
        df['AnoMesIndex'] = pd.to_datetime(df['AnoMes'] + '-01').map(pd.Timestamp.toordinal)
        arquivos = []
        for tipo in tipos:
            df_tipo = df[df['TIPO'] == tipo].groupby('AnoMesIndex')['Debito'].sum().reset_index()
            if len(df_tipo) < 4:
                continue
            x = df_tipo['AnoMesIndex']
            y = df_tipo['Debito']
            slope, intercept, _, _, _ = stats.linregress(x, y)
            future_x = np.array([x.max() + 30, x.max() + 60, x.max() + 90])
            future_y = intercept + slope * future_x

            plt.figure(figsize=(10, 4))
            plt.plot(x.map(pd.Timestamp.fromordinal), y, label='Real')
            plt.plot(pd.to_datetime(future_x.map(pd.Timestamp.fromordinal)), future_y, label='Previsto', linestyle='--')
            plt.title(f'Previsão de Gastos - {tipo}')
            plt.legend()
            plt.grid(True)
            plt.xticks(rotation=30)
            plt.tight_layout()
            file_path = os.path.join(output_dir, f'forecast_{tipo}.png')
            plt.savefig(file_path)
            arquivos.append(file_path)
            plt.close()
        return arquivos

    def gerar_ranking(df, output_dir):
        arquivos = []
        ranking_origem = df.groupby('Origem')['Debito'].sum().sort_values(ascending=False).head(10)
        ranking_tipo = df.groupby('TIPO')['Debito'].sum().sort_values(ascending=False).head(10)

        plt.figure(figsize=(10, 4))
        sns.barplot(x=ranking_origem.values, y=ranking_origem.index)
        plt.title("Top 10 Origens por Gastos")
        plt.tight_layout()
        path1 = os.path.join(output_dir, 'ranking_origem.png')
        plt.savefig(path1)
        arquivos.append(path1)
        plt.close()

        plt.figure(figsize=(10, 4))
        sns.barplot(x=ranking_tipo.values, y=ranking_tipo.index)
        plt.title("Top 10 Tipos por Gastos")
        plt.tight_layout()
        path2 = os.path.join(output_dir, 'ranking_tipo.png')
        plt.savefig(path2)
        arquivos.append(path2)
        plt.close()

        return arquivos

    def verificar_consistencia(df, output_dir):
        inconsistencias = {
            'data_nula': df[df['Data'].isnull()],
            'tipo_nulo': df[df['TIPO'].isnull()],
            'credito_negativo': df[df['Credito'] < 0],
            'debito_negativo': df[df['Debito'] < 0],
        }
        output_file = os.path.join(output_dir, 'relatorio_consistencia.txt')
        with open(output_file, 'w') as f:
            for nome, subset in inconsistencias.items():
                f.write(f"\n### {nome.upper()} - {len(subset)} ocorrencias\n")
                f.write(subset.head(5).to_string())
                f.write("\n---\n")
        return output_file

    class PDFReport(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'Relatórios PDW', ln=True, align='C')

        def add_image(self, image_path):
            self.add_page()
            self.image(image_path, x=10, y=25, w=180)

        def add_text(self, text_file):
            self.add_page()
            with open(text_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            self.set_font('Courier', '', 10)
            for line in lines:
                self.multi_cell(0, 5, line)

    print("Executando geração de relatórios analíticos avançados...")
    output_dir = os.path.join(dir_file_out, 'relatorios_gerados')
    os.makedirs(output_dir, exist_ok=True)
    df = load_general_entries(sqlite_database, general_entries_table)
    imagens = [gerar_relatorio_tendencia(df, output_dir)]
    imagens += prever_gastos(df, output_dir)
    imagens += gerar_ranking(df, output_dir)
    texto = verificar_consistencia(df, output_dir)

    pdf = PDFReport()
    for img in imagens:
        pdf.add_image(img)
    pdf.add_text(texto)
    pdf_path = os.path.join(output_dir, 'relatorios_pdw.pdf')
    pdf.output(pdf_path)
    print(out_line)
    print("Relatórios analíticos avançados gerados com sucesso.")
    print(f"Relatório PDF salvo em: {pdf_path}")
    print(out_line)
