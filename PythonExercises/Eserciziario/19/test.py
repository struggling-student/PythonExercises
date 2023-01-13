import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, ftesto, expectedMatrice, expectedCornice):
        '''Implementazione del test
            - ftesto             : file di testo
            - expectedMatrice    : matrice attesa
            - expectedCornice    : valore cornice atteso
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es19(ftesto)
        m, c = result
        self.assertEqual(type(result),  tuple, "Il risultato non è una tupla")
        self.assertEqual(len(result),  2, "La tupla deve avere due elementi")
        self.assertEqual(
            m, expectedMatrice, f"Il risultato deve essere {expectedMatrice} invece che {m}")
        self.assertEqual(
            c, expectedCornice, f"Il risultato deve essere {expectedCornice} invece che {c}")

    @data(
        ('fm10_1.txt', [[1, 20,  3, 40,  5],
                        [60,  7,  8,  9, 10],
                        [11, 12, 13, 14, 15]], 204),
        ('fm10_2.txt', [[1],
                        [2],
                        [3],
                        [4],
                        [5]], 15),
        ('fm10_3.txt', [[1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5]], 54)
    )
    @unpack
    def test(self, ftesto, expectedMatrice, expectedCornice):
        return self.do_test(ftesto, expectedMatrice, expectedCornice)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
