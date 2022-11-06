import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, tabella, expected, expectedTab):
        '''Implementazione del test
            - tabella       : tabella di interi sotto forma di lista di liste
            - expected      : lista di interi attesa
            - expectedTab   : tabella modificata con '*'
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es56(tabella)
        self.assertEqual(type(result), list, "Il risultato non è una lista")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.assertEqual(
            tabella, expectedTab, f"La tabella deve essere modificata in {expected} invece che {result}")


    @data(
        ([[3, 2, 1, 3], [2, 1, 3, 5], [1, 3, 2, 1]], [1, 3], [
         ['*', 2, '*', '*'], [2, '*', '*', 5], ['*', '*', 2, '*']]),
        ([[10, 10, 10, 10], [10, 10, 10, 10], [10, 10, 10, 10]], [10], [
         ['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                                         11, 12], [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                                                           13, 14, 15, 16], [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']])
    )
    @unpack
    def test(self, tabella, expected, expectedTab):
        return self.do_test(tabella, expected, expectedTab)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
