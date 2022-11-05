import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, s, k, expected):
        '''Implementazione del test
            - s             : stringa di cifre
            - k             : intero > 0
            - expected      : lista ordinata attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es50(s, k)
        self.assertEqual(type(result), list, "Il risultato non è una lista")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ('9135918246556', 3, ['359', '246', '135']),
        ('1234123412341234', 3, ['234', '123']),
        ('987654321', 3, [])
    )
    @unpack
    def test(self, s, k, expected):
        return self.do_test(s, k, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
