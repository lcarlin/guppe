numero_alunos = 5


def registra_nomes(_numero_alunos):
    _nomes = []

    for _i in range(_numero_alunos):
        _nome = input("Nome do aluno:\n")

        if len(_nome) < 40:
            _nome += ' ' * (40 - len(_nome))
        elif len(_nome) > 40:
            _nome += '\b' * (len(_nome) - 40)

        print(_nome)

        _nomes.append(_nome)

    return _nomes


def registra_notas(_numero_alunos):
    _notas = []

    for _i in range(_numero_alunos):
        _nota = float(input("Nota do aluno:\n"))
        _notas.append(_nota)

    return _notas


def escreve_arquivo(_nomes, _notas, _numero_alunos):
    with open("Arquivos_Exercicios/Notas_Binário.bin", 'wb') as _arq:
        for _aluno in range(numero_alunos):
            _finais = f"Nome: {_nomes[_aluno]} Nota: {_notas[_aluno]}\n"
            _arq.write(_finais.encode('utf-8'))

    return _arq.name


def encontra_maior(_arquivo, _notas):
    _maior_nota = max(_notas)
    _indice_nota = _notas.index(_maior_nota)

    with open(_arquivo, 'rb') as _arq:
        _dados = _arq.read().decode('utf-8').split('\n')

        return _dados[_indice_nota]


nomes = ["Maciel dos Santos Abreu de Lima Souza Silva", "Silvia Araújo Pereira", "Julio Tavares",
         "Aline Souza Pires", "Caio de Andrade e Lima Silva"]
notas = [2.0, 6.4, 9.1, 8.7, 10.0]  # Listas usadas para teste de gravação.

arquivo = escreve_arquivo(nomes, notas, numero_alunos)
print(encontra_maior(arquivo, notas))