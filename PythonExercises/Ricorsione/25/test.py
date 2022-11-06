import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, n, expected):
        '''Implementazione del test
            - n             : numero di riga del triangolo di tartaglia
            - expected      : lista di interi attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es25(n)
        self.assertEqual(type(result), list, "Il risultato non è una lista")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        (1, [1, 1]),
        (3, [1, 3, 3, 1]),
        (9, [1, 9, 36, 84, 126, 126, 84, 36, 9, 1])
    )
    @unpack
    def test(self, n, expected):
        return self.do_test(n, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
