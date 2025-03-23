import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configurações
WATCHED_FILE = "C:\\Users\\luizc\\OneDrive\\Documentos\\PDW\\PDW.xlsx"  # Caminho completo do arquivo a ser monitorado
DEST_DIR = "C:\\Users\\luizc\\Dropbox\\PDW_DRPBX"  # Diretório de destino

class FileMonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == WATCHED_FILE:
            print(f"Arquivo modificado: {event.src_path}")
            try:
                shutil.copy(WATCHED_FILE, DEST_DIR)
                print("Arquivo copiado com sucesso!")
            except Exception as e:
                print(f"Erro ao copiar arquivo: {e}")

if __name__ == "__main__":
    event_handler = FileMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path="C:\\Users\\luizc\\Dropbox\\PDW_DRPBX", recursive=False)

    observer.start()
    print("Monitoramento iniciado...")

    try:
        while True:
            time.sleep(10)  # Evita consumo excessivo de CPU
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
