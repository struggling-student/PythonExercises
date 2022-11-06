import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, d1, d2, expected):
        '''Implementazione del test
            - d1        : dizionario di una matrice sparsa
            - d2        : dizionario di una matrice sparsa
            - expected  : dizionario della una matrice sparsa attesa
        '''
        d1_test = d1
        d2_test = d2
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es52(d1, d2)
        self.assertEqual(type(result), dict, "Il risultato non è un dizionario")
        self.assertEqual(d1, d1_test, "I dizionari in input non vanno modificati")
        self.assertEqual(d2, d2_test, "I dizionari in input non vanno modificati")
        self.assertEqual(result, expected, f"Il risultato deve essere {expected} invece che {result}")
 

    @data(
        ({(0,2): 4,(1,0): 1, (1,1): 2, (2,1):8 }, {(0,0): 5,(1,1): 2, (2,2): 5, (1,0):2 }, {(0,2): 4,(1,0): 3, (1,1): 4, (2,1):8, (0,0):5, (2,2):5 }),
        ({(1,1):1,(2,3):2,(1,3):3}, {(1,1):1,(2,2):2,(2,3):3,(1,2):5}, {(1, 1): 2, (2, 3): 5, (1, 3): 3, (2, 2): 2, (1, 2): 5}),
        ({(1,1):5,(1,2):5,(2,1):5,(2,2):5}, {(3,1):1,(4,2):1,(4,3):1,(3,2):1}, {(1, 1): 5, (1, 2): 5, (2, 1): 5, (2, 2): 5, (3, 1): 1, (4, 2): 1, (4, 3): 1, (3, 2): 1})
    )
    @unpack
    def test(self, d1, d2, expected):
        return self.do_test(d1, d2, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
