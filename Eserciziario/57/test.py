import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, griglia, expected):
        '''Implementazione del test
            - griglia    : matrice di interi sotto forma di lista di liste
            - expected   : tupla di 4 liste attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es57(griglia)
        self.assertEqual(type(result), tuple, "Il risultato non è una tupla")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ([[1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 4, 1]],
         ([2, 2, 2, 1], [1, 2, 2, 2], [3, 2, 1, 4], [4, 1, 2, 3])),
        ([[1, 2, 3, 4], [4, 1, 'c', 3], [3, 4, 1, 2], [2, 3, 4, 1]], ([], [], [], [])),
        ([[1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 2, 1], [2, 3, 4, 1]], ([], [], [], [])),
        ([[1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 6, 1]], ([], [], [], [])),
        ([[3, 2, 1, 4], [2, 3, 4, 1], [1, 4, 3, 2], [4, 1, 2, 3]],
         ([2, 3, 2, 1], [1, 2, 3, 2], [1, 2, 3, 2], [2, 3, 2, 1])),
        ([[3, 2, 1, 4], [1, 3, 4, 2], [2, 4, 3, 1], [4, 1, 2, 3]],
         ([2, 3, 2, 1], [1, 2, 3, 2], [1, 2, 3, 2], [2, 3, 2, 1]))
    )
    @unpack
    def test(self, griglia, expected):
        return self.do_test(griglia, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
