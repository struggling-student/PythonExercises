import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, l, expected):
        '''Implementazione del test
            - l         : lista di interi
            - expected  : stringa attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es64(l)
        self.assertEqual(type(result), str, "Il risultato non è una stringa")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ([1, 23, 2000], "    2\n    0\n  2 0\n1 3 0"),
        ([1, 23, 2000, 900002], "      9\n      0\n    2 0\n    0 0\n  2 0 0\n1 3 0 2"),
        ([8000022233, 1, 23, 2000, 900002],
         "8        \n0        \n0        \n0        \n0       9\n2       0\n2     2 0\n2     0 0\n3   2 0 0\n3 1 3 0 2")
    )
    @unpack
    def test(self, l, expected, ):
        return self.do_test(l, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
