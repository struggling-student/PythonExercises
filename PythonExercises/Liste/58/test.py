import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, lista, expected, expectedLst):
        '''Implementazione del test
            - lista         : lista di stringhe con caratteri in {'N', 'S', 'E', 'O'}
            - expected      : numero di caratteri atteso
            - expectedLst   : lista di interi attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es58(lista)
        self.assertEqual(type(result), int, "Il risultato non è un intero")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.assertEqual(
            lista, expectedLst, f"La lista deve diventare {expectedLst} invece che {lista}")

    @data(
        (['NS', 'NEESS', 'NNOOO', 'NNEESSO'], 19, [0, 3, 5, 1]),
        (['NSO', 'NEESSO', 'NNOOOO', 'NNEESSOO'], 23, [1, 2, 6, 0])
    )
    @unpack
    def test(self, lista, expected, expectedLst):
        return self.do_test(lista, expected, expectedLst)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
