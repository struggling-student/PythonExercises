import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, f1, f2, expected, expectedIsto):
        '''Implementazione del test
            - f1            : file di testo
            - f2            : file dove salvare l'istogramma
            - expected      : numero di righe dell'istogramma
            - expectedIsto  : istogramma atteso
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es33(f1, f2)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        with open(f2, 'r', encoding='utf8') as f:
            testo = f.read()
        self.assertEqual(
            testo, expectedIsto, f"L'istogramma deve essere {expectedIsto} invece che {testo}")

    @data(
        ('ftesto3.txt', 'istogramma1.txt', 11,
         'iiii\nnnn\nee\noo\nrr\ntt\na\nb\nd\ng\np'),
        ('ftesto4.txt', 'istogramma2.txt', 20, 
         'aaaaaaaaaaaaaaaaaaaaa\noooooooooooooooooooo\neeeeeeeeeeeeeeee\niiiiiiiiiiiiii\nrrrrrrrrrrrrrr\nnnnnnnnnnnnnn\nuuuuuuuuu\nssssssss\nmmmmmmm\nllllll\npppppp\nddddd\nttttt\ncccc\nhhh\nbb\nff\nvv\nzz\ng')
    )
    @unpack
    def test(self, f1, f2, expected, expectedIsto):
        return self.do_test(f1, f2, expected, expectedIsto)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
