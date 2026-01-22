import random
import time
import copy

def bubble_sort(arr):
    """
    BUBBLE SORT (Ordenação por Bolha)
    
    Complexidade: O(n²) no pior caso
    
    COMO FUNCIONA:
    Imagina bolhas subindo em um líquido - as maiores sobem mais rápido!
    
    1. Percorre a lista da esquerda para a direita
    2. Compara cada par de elementos adjacentes (vizinhos)
    3. Se estiverem fora de ordem, TROCA eles de posição
    4. Após cada passagem completa, o MAIOR elemento "flutua" até o final
    5. Repete o processo, mas ignorando os elementos já ordenados no final
    6. Continua até que nenhuma troca seja necessária
    
    EXEMPLO VISUAL:
    [5, 3, 8, 4, 2]
    [3, 5, 4, 2, 8]  <- 8 "flutuou" para o final
    [3, 4, 2, 5, 8]  <- 5 chegou na penúltima posição
    [3, 2, 4, 5, 8]  
    [2, 3, 4, 5, 8]  <- ORDENADO!
    """
    n = len(arr)
    # Percorre toda a lista
    for i in range(n):
        # Flag para otimização: se não houver troca, a lista já está ordenada
        houve_troca = False
        
        # Última posição já está ordenada, então vamos até (n - i - 1)
        for j in range(0, n - i - 1):
            # Compara elemento atual com o próximo
            if arr[j] > arr[j + 1]:
                # TROCA! A bolha maior sobe
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                houve_troca = True
        
        # Se não houve troca, lista já ordenada - podemos parar!
        if not houve_troca:
            break
    
    return arr


def insertion_sort(arr):
    """
    INSERTION SORT (Ordenação por Inserção)
    
    Complexidade: O(n²) no pior caso, O(n) no melhor caso (lista já ordenada)
    
    COMO FUNCIONA:
    Exatamente como você organiza cartas de baralho na mão!
    
    1. Divide mentalmente a lista em duas partes: ORDENADA (esquerda) e NÃO-ORDENADA (direita)
    2. Começa com o primeiro elemento (considera ele já ordenado)
    3. Pega o próximo elemento da parte não-ordenada (a "carta da mesa")
    4. Compara com os elementos da parte ordenada, DA DIREITA PARA ESQUERDA
    5. Move elementos maiores uma posição para a direita
    6. Insere o elemento na posição correta
    7. Repete até todos elementos estarem ordenados
    
    EXEMPLO VISUAL:
    [5, 3, 8, 4, 2]
     ^  ^
     |  └─ Pega o 3
     └─── Parte ordenada
    
    [3, 5, 8, 4, 2]  <- 3 inserido antes do 5
    [3, 5, 8, 4, 2]  <- 8 já está no lugar certo
    [3, 4, 5, 8, 2]  <- 4 inserido entre 3 e 5
    [2, 3, 4, 5, 8]  <- 2 inserido no início
    """
    n = len(arr)
    
    # Começa do segundo elemento (índice 1), pois o primeiro já está "ordenado"
    for i in range(1, n):
        # Elemento atual que será inserido na posição correta
        chave = arr[i]
        
        # Posição do último elemento da parte ordenada
        j = i - 1
        
        # Move elementos maiores que a chave uma posição para frente
        # É como abrir espaço na sua mão de cartas
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]  # Desloca para a direita
            j -= 1
        
        # Insere a chave na posição correta (o espaço que abrimos)
        arr[j + 1] = chave
    
    return arr


def selection_sort(arr):
    """
    SELECTION SORT (Ordenação por Seleção)
    
    Complexidade: O(n²) sempre
    
    COMO FUNCIONA:
    É como selecionar o melhor jogador para formar um time, um por vez!
    
    1. Divide mentalmente a lista em ORDENADA (esquerda) e NÃO-ORDENADA (direita)
    2. Procura o MENOR elemento na parte não-ordenada
    3. TROCA ele com o primeiro elemento da parte não-ordenada
    4. Agora a parte ordenada cresceu em 1 elemento
    5. Repete até ordenar todos os elementos
    
    A diferença do Insertion: aqui SEMPRE buscamos o menor, não importa onde está!
    
    EXEMPLO VISUAL:
    [5, 3, 8, 4, 2]
         └─────┘
    Menor é 2, troca com 5
    
    [2, 3, 8, 4, 5]
        └──────┘
    Menor é 3, já está no lugar
    
    [2, 3, 8, 4, 5]
           └────┘
    Menor é 4, troca com 8
    
    [2, 3, 4, 8, 5]
              └──┘
    Menor é 5, troca com 8
    
    [2, 3, 4, 5, 8]  <- ORDENADO!
    """
    n = len(arr)
    
    # Percorre toda a lista
    for i in range(n):
        # Assume que o elemento atual é o menor
        indice_minimo = i
        
        # Procura o menor elemento no restante da lista não-ordenada
        for j in range(i + 1, n):
            if arr[j] < arr[indice_minimo]:
                # Encontrou um elemento menor! Atualiza o índice
                indice_minimo = j
        
        # Troca o menor elemento encontrado com o primeiro da parte não-ordenada
        # (Só faz a troca se realmente encontrou algo menor)
        if indice_minimo != i:
            arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]
    
    return arr


def merge_sort(arr):
    """
    MERGE SORT (Ordenação por Intercalação/Mesclagem)
    
    Complexidade: O(n log n) sempre! Um dos mais eficientes!
    
    ESTRATÉGIA: DIVIDIR PARA CONQUISTAR
    
    COMO FUNCIONA:
    Como organizar pilhas de documentos: divida, organize as partes e depois mescle!
    
    FASE 1 - DIVIDIR:
    1. Se a lista tem 0 ou 1 elemento, já está ordenada (CASO BASE)
    2. Divide a lista ao MEIO
    3. Ordena recursivamente a metade ESQUERDA
    4. Ordena recursivamente a metade DIREITA
    
    FASE 2 - CONQUISTAR (Merge):
    5. MESCLA as duas metades ordenadas em uma lista final ordenada
    
    EXEMPLO VISUAL:
    [5, 3, 8, 4, 2, 7, 1, 6]
            |
    [5, 3, 8, 4]  [2, 7, 1, 6]  <- DIVIDE
         |             |
    [5, 3] [8, 4]  [2, 7] [1, 6]  <- DIVIDE MAIS
      |      |      |       |
    [5][3] [8][4]  [2][7]  [1][6]  <- Elementos únicos (CASO BASE)
      |      |      |       |
    [3,5] [4,8]   [2,7]   [1,6]  <- MESCLA
         |             |
    [3,4,5,8]     [1,2,6,7]  <- MESCLA
            |
    [1,2,3,4,5,6,7,8]  <- MESCLA FINAL!
    """
    
    # CASO BASE: lista com 0 ou 1 elemento já está ordenada
    if len(arr) <= 1:
        return arr
    
    # DIVIDIR: encontra o meio da lista
    meio = len(arr) // 2
    
    # Divide recursivamente a metade esquerda
    esquerda = merge_sort(arr[:meio])
    
    # Divide recursivamente a metade direita
    direita = merge_sort(arr[meio:])
    
    # CONQUISTAR: mescla as duas metades ordenadas
    return merge(esquerda, direita)


def merge(esquerda, direita):
    """
    Função auxiliar do MERGE SORT
    Mescla duas listas ORDENADAS em uma única lista ORDENADA
    
    É como combinar duas pilhas de cartas já ordenadas em uma única pilha ordenada!
    """
    resultado = []
    i = j = 0
    
    # Enquanto houver elementos em AMBAS as listas
    while i < len(esquerda) and j < len(direita):
        # Compara os primeiros elementos de cada lista
        if esquerda[i] <= direita[j]:
            # Elemento da esquerda é menor, adiciona ele
            resultado.append(esquerda[i])
            i += 1
        else:
            # Elemento da direita é menor, adiciona ele
            resultado.append(direita[j])
            j += 1
    
    # Adiciona os elementos restantes (se houver)
    # Uma das listas pode ter terminado antes da outra
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado


def quick_sort(arr):
    """
    QUICK SORT (Ordenação Rápida)
    
    Complexidade: O(n log n) em média, O(n²) no pior caso
    
    ESTRATÉGIA: DIVIDIR PARA CONQUISTAR (com PIVÔ)
    
    COMO FUNCIONA:
    Escolhe um "líder" (pivô) e organiza todos em torno dele!
    
    1. Se a lista tem 0 ou 1 elemento, já está ordenada (CASO BASE)
    2. Escolhe um elemento como PIVÔ (geralmente o do meio ou último)
    3. PARTICIONA: reorganiza a lista de forma que:
       - Elementos MENORES que o pivô ficam à ESQUERDA
       - O PIVÔ fica no meio
       - Elementos MAIORES que o pivô ficam à DIREITA
    4. Aplica Quick Sort recursivamente na parte ESQUERDA
    5. Aplica Quick Sort recursivamente na parte DIREITA
    
    DIFERENÇA DO MERGE: aqui o trabalho pesado é ANTES da recursão (particionamento)
    No Merge, o trabalho é DEPOIS (mesclagem)
    
    EXEMPLO VISUAL:
    [5, 3, 8, 4, 2, 7]
              ^
              └─ Pivô (4)
    
    [3, 2] [4] [5, 8, 7]  <- Particionou!
      |          |
    Quick Sort  Quick Sort
      |          |
    [2, 3] [4] [5, 7, 8]
            |
    [2, 3, 4, 5, 7, 8]  <- ORDENADO!
    """
    
    # CASO BASE: lista vazia ou com 1 elemento
    if len(arr) <= 1:
        return arr
    
    # Escolhe o pivô (aqui escolhemos o elemento do meio)
    pivo = arr[len(arr) // 2]
    
    # PARTICIONA: separa em 3 grupos
    # Menores: elementos menores que o pivô
    menores = [x for x in arr if x < pivo]
    
    # Iguais: elementos iguais ao pivô (pode haver repetidos!)
    iguais = [x for x in arr if x == pivo]
    
    # Maiores: elementos maiores que o pivô
    maiores = [x for x in arr if x > pivo]
    
    # Recursão: ordena menores e maiores, depois concatena tudo
    return quick_sort(menores) + iguais + quick_sort(maiores)


def heap_sort(arr):
    """
    HEAP SORT (Ordenação por Heap)
    
    Complexidade: O(n log n) sempre
    
    ESTRUTURA DE DADOS: HEAP (Monte/Pilha)
    Um Heap é uma árvore binária especial onde:
    - MAX HEAP: pai sempre MAIOR que os filhos
    - MIN HEAP: pai sempre MENOR que os filhos
    
    COMO FUNCIONA:
    É como organizar uma pirâmide de copos: o maior sempre no topo!
    
    FASE 1 - CONSTRUIR O HEAP:
    1. Transforma a lista em um MAX HEAP
    2. O maior elemento fica na raiz (início da lista)
    
    FASE 2 - EXTRAIR E RECONSTRUIR:
    3. Troca o maior (raiz) com o último elemento
    4. Considera o último elemento como "ordenado" e ignora ele
    5. "Conserta" o heap (heapify) para manter a propriedade
    6. Repete até ordenar toda a lista
    
    REPRESENTAÇÃO EM ARRAY:
    Para um elemento no índice i:
    - Pai: (i - 1) // 2
    - Filho esquerdo: 2 * i + 1
    - Filho direito: 2 * i + 2
    
    EXEMPLO VISUAL:
    [4, 10, 3, 5, 1]
    
    Árvore MAX HEAP:
           10
          /  \
         5    3
        / \
       4   1
    
    Array: [10, 5, 3, 4, 1]
    
    Troca 10 com 1: [1, 5, 3, 4, |10]
    Heapify: [5, 4, 3, 1, |10]
    Troca 5 com 1: [1, 4, 3, |5, 10]
    Heapify: [4, 1, 3, |5, 10]
    Continue...
    """
    n = len(arr)
    
    # FASE 1: Constrói o MAX HEAP
    # Começa do último nó não-folha e vai até a raiz
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # FASE 2: Extrai elementos um por um do heap
    for i in range(n - 1, 0, -1):
        # Move a raiz (maior elemento) para o final
        arr[0], arr[i] = arr[i], arr[0]
        
        # Chama heapify na raiz reduzida
        heapify(arr, i, 0)
    
    return arr


def heapify(arr, n, i):
    """
    Função auxiliar do HEAP SORT
    Garante que a subárvore com raiz em 'i' seja um MAX HEAP
    
    n: tamanho do heap
    i: índice da raiz da subárvore
    """
    maior = i  # Inicializa o maior como raiz
    esquerda = 2 * i + 1  # Índice do filho esquerdo
    direita = 2 * i + 2   # Índice do filho direito
    
    # Se filho esquerdo existe e é maior que a raiz
    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda
    
    # Se filho direito existe e é maior que o maior atual
    if direita < n and arr[direita] > arr[maior]:
        maior = direita
    
    # Se o maior não é a raiz
    if maior != i:
        # Troca
        arr[i], arr[maior] = arr[maior], arr[i]
        
        # Recursivamente heapifica a subárvore afetada
        heapify(arr, n, maior)


def shell_sort(arr):
    """
    SHELL SORT (Ordenação de Shell)
    
    Complexidade: Depende da sequência de gaps, geralmente O(n log²n) ou O(n^1.5)
    
    CONCEITO: INSERTION SORT TURBINADO!
    
    COMO FUNCIONA:
    Em vez de comparar elementos adjacentes (vizinhos), compara elementos DISTANTES!
    
    1. Define uma sequência de "gaps" (intervalos) que vai diminuindo
    2. Para cada gap, faz um Insertion Sort modificado:
       - Compara elementos que estão a 'gap' posições de distância
       - Isso permite que elementos "pulem" grandes distâncias rapidamente
    3. Quando o gap chega a 1, é um Insertion Sort normal
       Mas agora a lista está "quase ordenada", então é muito rápido!
    
    SEQUÊNCIA DE GAPS:
    Clássica de Shell: n/2, n/4, n/8, ..., 1
    Outras: Knuth (3^k - 1)/2, Sedgewick, etc.
    
    POR QUE É MELHOR QUE INSERTION SORT?
    Insertion Sort é ótimo para listas quase ordenadas. Shell Sort primeiro
    "pré-ordena" a lista movendo elementos distantes, depois finaliza com
    Insertion Sort em uma lista já quase organizada!
    
    EXEMPLO VISUAL (gap = 3, depois gap = 1):
    [5, 3, 8, 4, 2, 7, 1, 6]
     
    Gap = 3:
    [5, _, _, 4, _, _, 1, _]  <- Compara 5, 4, 1
    [_, 3, _, _, 2, _, _, 6]  <- Compara 3, 2, 6
    [_, _, 8, _, _, 7, _, _]  <- Compara 8, 7
    
    Após gap 3: [4, 2, 7, 1, 5, 3, 8, 6]
    
    Gap = 1 (Insertion Sort normal):
    [1, 2, 3, 4, 5, 6, 7, 8]  <- Rápido pois já está quase ordenado!
    """
    n = len(arr)
    
    # Inicia com um gap grande (metade do tamanho da lista)
    gap = n // 2
    
    # Continua até o gap chegar a 0
    while gap > 0:
        # Faz um Insertion Sort modificado para este gap
        # É como fazer vários Insertion Sorts em sublistas intercaladas
        for i in range(gap, n):
            # Salva o elemento atual
            temp = arr[i]
            
            # Move elementos do sublista que são maiores que temp
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # Coloca temp na posição correta
            arr[j] = temp
        
        # Reduz o gap pela metade (sequência de Shell clássica)
        gap //= 2
    
    return arr


def medir_tempo_execucao(funcao_sort, arr, nome_algoritmo):
    """
    Função auxiliar para medir o tempo de execução de um algoritmo
    
    Parâmetros:
    - funcao_sort: função do algoritmo de ordenação
    - arr: lista a ser ordenada (será copiada para não modificar o original)
    - nome_algoritmo: nome do algoritmo para exibição
    
    Retorna: tempo de execução em segundos
    """
    # Cria uma cópia da lista para não modificar a original
    arr_copia = copy.deepcopy(arr)
    
    print(f"\n{'='*60}")
    print(f"Executando: {nome_algoritmo}")
    print(f"{'='*60}")
    
    # Marca o tempo inicial
    inicio = time.time()
    
    # Executa o algoritmo
    resultado = funcao_sort(arr_copia)
    
    # Marca o tempo final
    fim = time.time()
    
    # Calcula o tempo decorrido
    tempo_decorrido = fim - inicio
    
    # Verifica se a lista está realmente ordenada
    esta_ordenada = all(resultado[i] <= resultado[i+1] for i in range(len(resultado)-1))
    
    print(f"Tempo de execução: {tempo_decorrido:.6f} segundos")
    print(f"Lista ordenada corretamente: {'✓ SIM' if esta_ordenada else '✗ NÃO'}")
    print(f"Primeiros 10 elementos: {resultado[:10]}")
    print(f"Últimos 10 elementos: {resultado[-10:]}")
    
    return tempo_decorrido


def main():
    """
    Função principal que executa todos os algoritmos e compara os resultados
    """
    print("\n" + "="*60)
    print("COMPARAÇÃO DE ALGORITMOS DE ORDENAÇÃO")
    print("="*60)
    
    # Gera uma lista com 10.000 elementos aleatórios entre 1 e 100.000
    tamanho = 10000
    lista_original = [random.randint(1, 100000) for _ in range(tamanho)]
    
    print(f"\nLista gerada com {tamanho} elementos aleatórios")
    print(f"Primeiros 20 elementos: {lista_original[:20]}")
    print(f"Últimos 20 elementos: {lista_original[-20:]}")
    
    # Dicionário para armazenar os tempos de execução
    tempos = {}
    
    # Lista de algoritmos para testar
    algoritmos = [
        (bubble_sort, "BUBBLE SORT"),
        (insertion_sort, "INSERTION SORT"),
        (selection_sort, "SELECTION SORT"),
        (merge_sort, "MERGE SORT"),
        (quick_sort, "QUICK SORT"),
        (heap_sort, "HEAP SORT"),
        (shell_sort, "SHELL SORT")
    ]
    
    # Executa cada algoritmo e mede o tempo
    for funcao, nome in algoritmos:
        tempo = medir_tempo_execucao(funcao, lista_original, nome)
        tempos[nome] = tempo
    
    # Exibe o ranking de desempenho
    print("\n" + "="*60)
    print("RANKING DE DESEMPENHO (do mais rápido para o mais lento)")
    print("="*60)
    
    # Ordena os algoritmos por tempo de execução
    ranking = sorted(tempos.items(), key=lambda x: x[1])
    
    for posicao, (nome, tempo) in enumerate(ranking, 1):
        print(f"{posicao}º - {nome}: {tempo:.6f} segundos")
    
    print("\n" + "="*60)
    print("ANÁLISE COMPLETA FINALIZADA!")
    print("="*60)
    print("\nOBSERVAÇÕES:")
    print("• Bubble, Insertion e Selection Sort são O(n²) - lentos para grandes listas")
    print("• Merge, Quick e Heap Sort são O(n log n) - muito mais eficientes!")
    print("• Shell Sort é uma melhoria do Insertion Sort com melhor performance")
    print("• Quick Sort geralmente é o mais rápido na prática")
    print("• Merge Sort é estável e tem desempenho consistente")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
