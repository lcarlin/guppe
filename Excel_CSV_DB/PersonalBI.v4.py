import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import sys
import datetime
import subprocess

# Variável predefinida para o nome do arquivo de log
log_file_name = "log_output.txt"

# Nome do script externo que será chamado
external_script = "KleitaoBomdeGuerra.py"

# Variável para armazenar o caminho do arquivo selecionado
parameter_file = None

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
    print("Iniciando execução do script externo...")
    
    try:
        # Se o arquivo de parâmetro for selecionado, passamos como argumento
        if parameter_file:
            print(f"Executando script com o parâmetro: {parameter_file}")
            result = subprocess.run(
                ['python', external_script, parameter_file],  # Executa o script com o arquivo como argumento
                text=True,                                   # Captura a saída como string
                capture_output=True                           # Captura stdout e stderr
            )
        else:
            print("Executando script sem parâmetros.")
            result = subprocess.run(
                ['python', external_script],  # Executa o script sem argumento
                text=True,                    # Captura a saída como string
                capture_output=True            # Captura stdout e stderr
            )

        # Exibe a saída do script no terminal da interface gráfica
        print(result.stdout)
        if result.stderr:
            print("Erro durante a execução do script:")
            print(result.stderr)
        
    except Exception as e:
        print(f"Erro ao tentar executar o script {external_script}: {e}")

    print("Execução do script externo finalizada.")

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

# Função para selecionar o arquivo de parâmetro
def selecionar_arquivo():
    global parameter_file
    # Abre o diálogo para selecionar um arquivo
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo de parâmetro",
        filetypes=(("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*"))
    )
    
    if file_path:
        parameter_file = file_path
        messagebox.showinfo("Arquivo selecionado", f"Arquivo selecionado: {parameter_file}")
    else:
        parameter_file = None
        messagebox.showinfo("Nenhum arquivo selecionado", "Nenhum arquivo foi selecionado.")

# Cria a janela principal
janela = tk.Tk()
janela.title("Interface Gráfica - Terminal")
janela.geometry("600x400")

# Cria um frame para os botões para organizar o layout
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

# Cria o botão para executar a função main
botao_executar = tk.Button(frame_botoes, text="Executar PDW/PBI", command=executar_main)
botao_executar.pack(side=tk.LEFT, padx=10)

# Cria o botão para selecionar o arquivo de parâmetro
botao_parametro = tk.Button(frame_botoes, text="Parameter file", command=selecionar_arquivo)
botao_parametro.pack(side=tk.LEFT, padx=10)

# Cria a janela de terminal (caixa de texto com rolagem)
terminal = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=80, height=20)
terminal.pack(padx=10, pady=10)

# Redireciona o stdout para a janela de terminal
sys.stdout = PrintLogger(terminal)

# Inicia o loop principal da interface gráfica
janela.mainloop()
