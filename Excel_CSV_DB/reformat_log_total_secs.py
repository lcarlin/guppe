import sys
import shutil
import time
from pathlib import Path

def reformat_total_secs_field(line: str) -> str:
    parts = line.split('|')
    if len(parts) < 4:
        return line  # linha mal formada, retorna como está
    
    # Formatar o terceiro campo (índice 2)
    campo = parts[2].strip()
    if "TotalSecs" in campo:
        try:
            valor = campo.split()[0]  # Pega só o número
            segundos = float(valor)
            novo_campo = f"{segundos:7.2f} TotalSecs"
            parts[2] = f" {novo_campo} "
        except ValueError:
            pass  # ignora se não for possível converter
    
    return '|'.join(parts)

def processar_log(nome_arquivo: str):
    original = Path(nome_arquivo)
    if not original.exists():
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return

    # Criar backup com timestamp
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    backup = original.with_suffix(f".{timestamp}.BAK")
    shutil.copy2(original, backup)
    print(f"Backup criado: {backup}")

    # Ler e reescrever o arquivo
    with open(backup, 'r', encoding='utf-8') as fin, open(original, 'w', encoding='utf-8') as fout:
        for linha in fin:
            nova_linha = reformat_total_secs_field(linha)
            fout.write(nova_linha)

    print(f"Arquivo '{original}' foi atualizado com sucesso.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python reformat_log_total_secs.py <arquivo_log>")
    else:
        processar_log(sys.argv[1])
