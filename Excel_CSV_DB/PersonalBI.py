import tkinter as tk
from tkinter import scrolledtext
import sys
import datetime

# Variável predefinida para o nome do arquivo de log
log_file_name = "log_output.txt"

# Classe para redirecionar o 'print' para a janela de texto
class PrintLogger:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.text_widget.configure(state='disabled')
        self.text_widget.tag_configure('stdout', foreground='black')
    
    def write(self, message):
        self.text_widget.configure(state='normal')
        self.text_widget.insert(tk.END, message, ('stdout',))
        self.text_widget.configure(state='disabled')
        self.text_widget.yview(tk.END)

    def flush(self):
        pass  # Método necessário para compatibilidade com o comportamento do stdout

# Função main() que será executada pelo botão
def main():
    print("Iniciando a função main()")
    print("Executando tarefa...")
    # Simulação de algumas saídas
    for i in range(1, 6):
        print(f"Passo {i}: tarefa sendo executada...")
    print("Função main() finalizada.")

# Função chamada quando o botão for pressionado
def executar_main():
    # Chama a função main
    main()

    # Salva o conteúdo da janela de terminal em um arquivo de texto
    salvar_log()

# Função para salvar o conteúdo da janela de terminal em um arquivo
def salvar_log():
    with open(log_file_name, 'a') as f:
        f.write(f"\n--- Execução em {datetime.datetime.now()} ---\n")
        log_content = terminal.get('1.0', tk.END)  # Obtém todo o conteúdo da janela de terminal
        f.write(log_content)

# Cria a janela principal
janela = tk.Tk()
janela.title("Interface Gráfica - Terminal")
janela.geometry("600x400")

# Cria o botão para executar a função main
botao_executar = tk.Button(janela, text="Executar PDW/PBI", command=executar_main)
botao_executar.pack(pady=10)

# Cria a janela de terminal (caixa de texto com rolagem)
terminal = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=80, height=20)
terminal.pack(padx=10, pady=10)

# Redireciona o stdout para a janela de terminal
sys.stdout = PrintLogger(terminal)

# Inicia o loop principal da interface gráfica
janela.mainloop()
