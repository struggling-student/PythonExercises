import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, file, ls, expected):
        '''Implementazione del test
            - file      : file di testo
            - ls        : lista di caratteri
            - expected  : lista di tuple attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es24(file, ls)
        self.assertEqual(type(result), list, "Il risultato non è una lista")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ('test10a.txt', ['o', 'i', 'S'], [('o', '31.58%'), ('S', '5.26%'), ('i', '5.26%')]),
        ('test10b.txt', ['M', 'm', 'i'], [('i', '7.17%'), ('M', '3.11%'), ('m', '3.11%')]),
        ('test10c.txt', ['a', 'Q', 'p'], [('a', '9.30%'), ('p', '2.97%'), ('Q', '0.00%')])
    )
    @unpack
    def test(self, file, ls, expected):
        return self.do_test(file, ls, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
