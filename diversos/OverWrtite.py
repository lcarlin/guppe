import time
import sys

# Texto a ser sobreescrito com cores
text = "\033[1;31mTexto em vermelho\033[0m"

for i in range(10):
    # Imprime o texto na mesma linha
    sys.stdout.write("\r" + text + " - \033[34mTentativa\033[0m " + "\033[33m"+str(i)+"\033[0m")
    sys.stdout.flush()
    time.sleep(1)  # Aguarde um segundo

# Pule uma linha após a conclusão
print()