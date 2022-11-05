import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, matrice, expected, expectedMtr):
        '''Implementazione del test
            - matrice       : matrice di caratteri 
            - expected      : matrice di caratteri attesa
            - expectedMtr   : matrice di caratteri uguale a quella in input
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es21(matrice)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.assertEqual(
            matrice, expectedMtr, f"la matrice {expectedMtr} è stata modificata in {matrice}")

    @data(
        ([['q','s','g','g'],['b','a','m','f'],['a','b','n','z']], [['a', 'a', 'g', 'f'], ['b', 'b', 'm', 'g'], ['q', 's', 'n', 'z']], [['q','s','g','g'],['b','a','m','f'],['a','b','n','z']]),
        ([['d','c','a','d'],['c','d','d','a'],['b','a','c','b'],['a','b','b','c']], [['a','a','a','a'], ['b','b','b','b'], ['c','c','c','c'], ['d','d','d','d']], [['d','c','a','d'],['c','d','d','a'],['b','a','c','b'],['a','b','b','c']])
    )
    @unpack
    def test(self, matrice, expected, expectedMtr):
        return self.do_test(matrice, expected, expectedMtr)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
