sal_carlos = float(input('Salário carlos: '))
renda_joao = sal_joao = sal_carlos / 3
renda_carlos = sal_carlos + (sal_carlos * (2/100))
total_meses = 0
while True:
    renda_joao += (sal_joao * (5/100))
    total_meses += 1
    if renda_joao >= renda_carlos:
        print(f'Salário João R$: {renda_joao:.2f}'
              f'\nSalário Carlos: {renda_carlos:.2f}'
              f'\nTempo que João levou pra ultrapassar o ssalário de Carlos + 5%: {total_meses} meses.')
        break