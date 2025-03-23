import time
import shutil
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

class ObservadorDeArquivo(FileSystemEventHandler):
    def __init__(self, arquivo_origem, diretorio_destino):
        self.arquivo_origem = arquivo_origem
        self.diretorio_destino = diretorio_destino

    def on_modified(self, event):
        if event.src_path.endswith("PDW.xlsx"):
            try:
                shutil.copy2(self.arquivo_origem, self.diretorio_destino)
                copied = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                print(f"{copied} - Arquivo {self.arquivo_origem} copiado para {self.diretorio_destino}")
            except Exception as e:
                print(f"Erro ao copiar o arquivo: {e}")

def monitorar_arquivo(arquivo_origem, diretorio_destino):
    started = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print(f'{started} - Iniciando monitoramento do arquivo ' + Path(arquivo_origem).name )
    event_handler = ObservadorDeArquivo(arquivo_origem, diretorio_destino)
    observer = Observer()
    observer.schedule(event_handler, path=arquivo_origem.rsplit('\\', 1)[0], recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(360)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    arquivo_origem = r"C:\Users\luizc\OneDrive\Documentos\PDW\PDW.xlsx"   # Substitua pelo caminho do seu arquivo
    diretorio_destino = r"C:\Users\luizc\Dropbox\PDW_DRPBX"                 # Substitua pelo caminho do diretório de destino

    monitorar_arquivo(arquivo_origem, diretorio_destino)