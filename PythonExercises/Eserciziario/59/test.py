import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, ftesto, expected):
        '''Implementazione del test
            - fileInJSON    : file con stringhe di interi per ongi riga
            - expected      : stringa attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es59(ftesto)
        self.assertEqual(type(result), str, "Il risultato non è una stringa")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ('matrice1.txt', '0000'),
        ('matrice3.txt', '110010')
    )
    @unpack
    def test(self, ftesto, expected):
        return self.do_test(ftesto, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
