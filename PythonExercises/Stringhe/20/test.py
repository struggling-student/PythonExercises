import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, stringa, expected):
        '''Implementazione del test
            - stringa       : una stringa
            - expected      : stringa di interi attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es20(stringa)
        self.assertEqual(type(result),  str, "Il risultato non è una stringa")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ('Angelo Monti Andrea Sterbini e Angelo Spognardi', '48 63 39 88 5 48 93'),
        ('Aa bB Cc dD', '2 4 6 8')
    )
    @unpack
    def test(self, stringa, expected):
        return self.do_test(stringa, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
