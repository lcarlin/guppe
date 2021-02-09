# Ler o código do produto do cardápio e a quantidade, calcula somente um pedido.
#
# produto               codigo      preço
# cachorro quente       100         1.20
# Bauru Simples         101         1.30
# Bauru com Ovo         102         1.50
# Hamburguer            103         1.20
# Cheeseburger          104         1.70
# Suco                  105         2.20
# Refrigerante          106         1.00

menu = [[100, 'cachorro quente', 1.20],
        [101, 'Bauru Simples', 1.30],
        [102, 'Bauru com Ovo', 1.50],
        [103, 'Hamburger', 1.20],
        [104, 'Cheeseburger', 1.70],
        [105, 'Suco', 2.20],
        [106, 'Refrigerante', 1.00]]

# Apresenta na tela MENU
print('========== MENU DA LANCHONETE ==========')
print('COD.     PROD.   PREÇO')
for m in range(len(menu)):  # alterei (0, 7) para len(menu)
    print(
        f'{menu[m][0]}   {menu[m][1]}{" " * (30 - len(menu[m][1]))}{menu[m][2]}')  # alterei print(menu) utilizando " " * 30 - len para preencher de espaços
print('=' * 40)

produto = int(input('Digite o código do produto: '))
quantidade = int(input('Digite a quantidade: '))

# Calcula preço
for i in range(0, 7):
    if produto in menu[i]:
        print(f'{quantidade} x {menu[i][1]} = {quantidade * (menu[i][2]):.2f}')
    else:
        print('Produto não cadastrado!')
        break