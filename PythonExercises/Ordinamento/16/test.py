import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, stringa, k, expected):
        '''Implementazione del test
            - stringa       : stringa di caratteri
            - k             : un intero
            - expected      : lista di sottostringhe di stringa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es16(stringa, k)
        self.assertEqual(type(result), list, "Il risultato non è una lista")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ('aabbb', 1, ['bbb', 'aa', 'bb', 'a', 'b']),
        ('bcafedg', 3, ['afe', 'bca', 'caf', 'edg', 'fed']),
        ('ccaabbdd', 3, ['aabbdd', 'ccaabb', 'aabbd',
                         'abbdd', 'caabb', 'ccaab', 'abbd', 'caab'])
    )
    @unpack
    def test(self, stringa, k, expected):
        return self.do_test(stringa, k, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
