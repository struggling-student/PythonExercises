
# Esempio di test

# IMPORT NECESSARI
import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program

@ddt
class Test(testlib.TestCase):

    def do_test(self, file, k, expected):
        '''Implementazione del test
            - file: file di testo
            - k: intero 
            - expected      : numero atteso di alberi nella foresta
        '''

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es10(file, k)
        self.assertEqual(type(result), str, "Il risultato non è una Stringa")
        self.assertEqual(result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(  
            ('ft9.txt', 3, 'are'),
            ('ft9.txt', 6, 'figlia'),
            ('ft9.txt', 10, '')
            )
    @unpack
    def test(self, file, k, expected):
        return self.do_test(file, k, expected)

if __name__ == '__main__':
    Test.main()

