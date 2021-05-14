"""
Seção 20: TEste com Python
    05 - Uma Introdução ao Unit Test
Teste unitário é a forma de se testar unidades individuais de codigo fontes
Unidades indicivuais podem ser : funções, metodos, classes, modulos, etc
Teste unitário não nos referimos apenas a Puthon é referenta à area de desenvolvimento de código
====================================================================================================================
Para criar nossos testes, criamos classes que herdam de UnitTest.TestCase e a partir dai ganhamos todos os
'assertions' presentes no modulo
para rodar os tests utilizamos unittest.main()
====================================================================================================================
https://docs.python.org/3/library/unittest.html
====================================================================================================================
Method                     Checks that          New in
assertEqual(a, b)          a == b
assertNotEqual(a, b)       a != b
assertTrue(x)              bool(x) is True
assertFalse(x)             bool(x) is False
assertIs(a, b)             a is b               3.1
assertIsNot(a, b)          a is not b           3.1
assertIsNone(x)            x is None            3.1
assertIsNotNone(x)         x is not None        3.1
assertIn(a, b)             a in b               3.1
assertNotIn(a, b)          a not in b           3.1
assertIsInstance(a, b)     isinstance(a, b)     3.2
assertNotIsInstance(a, b)  not isinstance(a, b) 3.2
====================================================================================================================
Por convenção todos os Testes em um TestCase deve ter seu nome iniciado com " test_ "
====================================================================================================================
Para executar o unit Tst commodo verbose:
python modulo_pitão -v
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
====================================================================================================================
"""

def main():
    print('-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-')
    print('===========================================================')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('-----------------------------------------------------------')
    print('***********************************************************')

## e é aqui que a brincadeitra começa
if __name__ == '__main__':
    main()

## Exemplo de caso de uso de UnitTest
import unittest
from atividades import comer, dormir
class AtividadesTestes(unittest.TestCase):
    def test_comer(self):
        """TEstanto o retorno com comida sauldave"""
        self.assertEqual(comer('quiabo', True), 'Estou comendo quiabo porque quero manter a forma.')

    def test_comer_gostosa(self):
        """TEstanto o retorno com comida HGostosa"""
        self.assertEqual(comer(comida='pizza', eh_saudavel=False), 'Estou comendo pizza poque só se vive uma vez')

    def test_dormir_pouco(self):
        """TEstanto o retorno com dormindo pouco """
        self.assertEqual(dormir(4), 'Continuo cansado após dormir por 4 horas. :-(')

    def test_domir_muito(self):
        """TEstanto o retorno codormindo bastante """
        self.assertEqual(dormir(10),'Dormi muito e estou atrasado para o trabalho' )

def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma. '
    else:
        final = 'a gente só vive uma vez'

    return f'Estou comendo {comida} porque {final}'

def dormir(num_horas):
    if num_horas > 8 :
        return f'Dormi muito e estou atrasado para o trabalho'
    else:
        return  f'Continuo cansado após domir por {num_horas} horas :-('
