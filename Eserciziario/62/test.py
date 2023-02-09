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
            - matrice       : matrice di interi sotto forma di lista di liste
            - expected      : nuova matrice di interi
            - expectedMtr   : la matrice in input non deve cambiare
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es62(matrice)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.assertEqual(
            matrice, expectedMtr, f"La matrice originale {expectedMtr} è stata modificata in {matrice}")

    @data(
        ([[2, 0, -4], [5, 10, 20], [5, 1, -1]],
         [[5, 10, 20], [2, 0, -4], [5, 1, -1]]),
        ([[2, 0, -4], [5, 10, 10], [25, 1, -1]],
         [[-1, 1, 25], [10, 10, 5], [-4, 0, 2]]),
        ([[52, 0,  -4, 19], [5, 10, 10, 52], [25, 1, -95, -80], [-95, 14, 17, 42]],
         [[19, 0,  -4, 52], [42, 14, 17, -95], [-80, 1, -95, 25], [52, 10, 10, 5]])
    )
    @unpack
    def test(self, matrice, expected):
        return self.do_test(matrice, expected, matrice)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
