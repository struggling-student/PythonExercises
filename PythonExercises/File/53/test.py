import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, testo, expected):
        '''Implementazione del test
            - testo    : file di testo contenente un dizionario
            - expected : dizionario atteso
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es53(testo)
        self.assertEqual(type(result), dict,
                         "Il risultato non è un dizionario")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ('ftesto10_1.txt', {1: [3, 4, 5], 6: [6, 7], 8: [9]}),
        ('ftesto10_2.txt', {1: [3, 4, 5], 6: [6, 7],
                            8: [9, 10, 13], 5: [1, 6], 7: [21]}),
        ('ftesto10_3.txt', {1: [2, 3, 4, 4], 6: [7],
                            8: [9, 10, 11, 12, 13], 14: [15, 16, 17, 18]})
    )
    @unpack
    def test(self, testo, expected):
        return self.do_test(testo, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
