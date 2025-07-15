import sys
import time
import shutil
from datetime import datetime
from pathlib import Path

def calcular_total_secs(inicio: str, fim: str) -> str:
    try:
        dt_format = "%Y/%m/%d %H:%M:%S"
        t1 = datetime.strptime(inicio.strip().replace(" Started", ""), dt_format)
        t2 = datetime.strptime(fim.strip().replace(" Ended", ""), dt_format)
        segundos = (t2 - t1).total_seconds()
        return f"{segundos:10.2f} TotalSecs"
    except Exception as e:
        return "     0.00 TotalSecs"

def corrigir_linha(linha: str) -> str:
    partes = linha.strip().split("|")

    # Completa com colunas vazias até ter 6
    while len(partes) < 6:
        partes.append("")

    # Calcular TotalSecs (campo 3)
    if not partes[2].strip():
        partes[2] = " " + calcular_total_secs(partes[0], partes[1]) + " "

    # Preencher os campos faltantes
    if not partes[3].strip():
        partes[3] = " Version N/D "
    if not partes[4].strip():
        partes[4] = " Hostname N/D "
    if not partes[5].strip():
        partes[5] = " OS N/D "

    return "|".join(part.strip() for part in partes)

def corrigir_arquivo_log(nome_arquivo: str):
    original = Path(nome_arquivo)
    if not original.exists():
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return

    # Criar backup
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    backup = original.with_suffix(f".{timestamp}.BAK")
    shutil.copy2(original, backup)
    print(f"Backup criado: {backup.name}")

    # Corrigir linhas e sobrescrever arquivo
    with open(backup, 'r', encoding='utf-8') as fin, open(original, 'w', encoding='utf-8') as fout:
        for linha in fin:
            nova = corrigir_linha(linha)
            fout.write(nova + "\n")

    print(f"Arquivo corrigido: {original.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python corrigir_log_personaldata.py <arquivo_log>")
    else:
        corrigir_arquivo_log(sys.argv[1])
