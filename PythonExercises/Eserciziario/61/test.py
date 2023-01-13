import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, ftesto, op, sel, expected):
        '''Implementazione del test
            - ftesto    : matrice in input
            - op        : codice operazione {'sum', 'min', 'max'}
            - sel       : codice selezione {'col', 'row', 'dp', 'ds'}
            - expected  : lista di interi attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es61(ftesto, op, sel)
        self.assertEqual(type(result), list, "Il risultato non è una lista")
        self.assertEqual(
            result, expected, f"Il risultato per l'operazione {op} e il selettore {sel} deve essere {expected} invece che {result}")

    @data(
        ('matrice4.txt', {'maxrow': [2, 20, 5], 'minrow': [-4, 5, -1], 'sumrow': [-2, 35, 5], 'maxcol': [5,  10, 20], 'mincol': [
         2,  0, -4], 'sumcol': [12, 11, 15], 'maxdp': [10], 'mindp': [-1], 'sumdp': [11], 'maxds': [10], 'minds': [-4], 'sumds': [11]}),
        ('matrice5.txt', {'maxrow': [3, 20, 6, 20], 'minrow': [-4, 5, -1, -8], 'sumrow': [-2, 44, 11, 7], 'maxcol': [5,  10, 20, 20],
                          'mincol': [-8, 0, -7, -1], 'sumcol': [5, 13, 8, 34], 'maxdp': [20], 'mindp': [-1], 'sumdp': [32], 'maxds': [20], 'minds': [-8], 'sumds': [12]})
    )
    @unpack
    def test(self, testo, vector):
        for op in ['max', 'min', 'sum']:
            for sel in ['row', 'col', 'dp', 'ds']:
                self.do_test(testo, op, sel, vector[op+sel])


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
