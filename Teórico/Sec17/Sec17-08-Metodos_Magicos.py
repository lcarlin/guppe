"""
Seção 17 -
*   Metodos Mágicos são todos os métodos que utilizam o DUnder (__INIT__, __MAIN__ )
Dunder -> Double UnderScore -
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================

"""
class Livro:
    def __init__(self, titulo, autor, paginas ):
        self.titulo =titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'Titulo: {self.titulo}; Autor: {self.autor}; Pags: {self.paginas};'

    def __str__(self):
        return f'Titulo: {self.titulo}; Autor: {self.autor}; Pags: {self.paginas};'

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um objecto livro foi apagado de A Memorias ')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, otro):
        if isinstance(otro, int):
            msg = ''
            for n in range(otro):
                msg += ' ' + str(self)

            return msg

        return 'Dá não pra fazer isso '




def main ():
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    livro1 = Livro('Pitão Pedras', 'Universidade Geka', 450)
    livro2 = Livro('IA com Pitão', 'Universidade Geka' , 369)

    print(livro1)
    print(livro2)

    print(len(livro2))

## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()
