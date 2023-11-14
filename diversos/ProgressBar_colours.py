from tqdm import tqdm
import time
import sys
# Número total de iterações
total_iterations = 100
# Texto a ser sobreescrito com cores
text = "\033[1;31mTexto em vermelho\033[0m"

# Crie uma barra de progresso
progress_bar = tqdm(total=total_iterations, desc="Progresso", unit="it")

# Simule algum trabalho em um loop
for i in range(total_iterations):
    # Atualize a barra de progresso
    progress_bar.update(1)
    # Execute alguma tarefa aqui
    time.sleep(0.1)  # Simulação de uma tarefa que leva algum tempo
    # Imprime o texto na mesma linha
    sys.stdout.write("\r" + text + " - Tentativa " + str(i))
    sys.stdout.flush()

# Certifique-se de fechar a barra de progresso quando terminar
progress_bar.close()

# Pule uma linha após a conclusão
print()
