import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, fname, expected):
        '''Implementazione del test
            - fname         : file contenente la sequenza di interi
            - expected      : numero intero atteso 
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es41(fname)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    # ESEMPIO DI BATTERIA DI TEST ELENCATA COME TABELLA
    @data(
        ('fsequenza1.txt', 2),
        ('fsequenza2.txt', 7)
    )
    @unpack
    def test(self, fname, expected):
        return self.do_test(fname, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
