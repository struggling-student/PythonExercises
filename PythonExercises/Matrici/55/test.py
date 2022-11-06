import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, sel, m, n, matr, expected, expectedMatr):
        '''Implementazione del test
            - sel           : carattere tra 'r' e 'c'
            - m             : intero, numero di riga o colonna
            - n             : intero, numero di riga o colonna
            - matr          : matrice di interi
            - expected      : tupla (min, max) attesa
            - expectedMatr  : matrice modificata attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es55(sel, m, n, matr)
        self.assertEqual(type(result), tuple, "Il risultato non è una tupla")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.assertEqual(
            matr, expectedMatr, f"La matrice deve diventare {expectedMatr} invece che {matr}")

    @data(
        ('c', 0, 2, [[2, 0, -4], [5, 10, 20], [5, 1, -1]],
         (-4, 20), [[-4, 0, 2], [20, 10, 5], [-1, 1, 5]]),
        ('r', 0, 2, [[2, 0, -4, -20], [5, 100, 20, 3], [5, 1, -1, 1]],
         (-20, 100), [[5, 1, -1, 1], [5, 100, 20, 3], [2, 0, -4, -20]])
    )
    @unpack
    def test(self, sel, m, n, matr, expected, expectedMatr):
        return self.do_test(sel, m, n, matr, expected, expectedMatr)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
