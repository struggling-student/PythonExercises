import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, f1, expected):
        '''Implementazione del test
            - f1          : file json con la lista di interi
            - expected      : lista di tuple attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es32(f1)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ('file1.json', [(2, 0), (0, 6), (4, 4), (1, 0), (7, 16)]), 
        ('file2.json', [(6, 8), (15, 0), (0, 0), (0, 10), (25, 20)])
    )
    @unpack
    def test(self, f1, expected):
        return self.do_test(f1, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
