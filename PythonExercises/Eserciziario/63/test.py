import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, f1, f2, expected, expectedf2):
        '''Implementazione del test
            - f1            : file contenente parole
            - f2            : file di terne da creare
            - expected      : numero di caratteri atteso
            - expectedf2    : file f2 atteso
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es63(f1, f2)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.check_text_file(f2, expectedf2)

    @data(
        ('ftesto1.txt', 'fterne1.txt', 16, 'RisTerne1.txt'),
        ('ftesto2.txt', 'fterne2.txt', 71, 'RisTerne2.txt'),
        ('ftesto3.txt', 'fterne3.txt', 21, 'RisTerne3.txt')
    )
    @unpack
    def test(self, f1, f2, expected, expectedf2):
        return self.do_test(f1, f2, expected, expectedf2)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
