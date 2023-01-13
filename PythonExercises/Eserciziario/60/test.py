import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, fileIn, fileOut, expected, expectedMatr):
        '''Implementazione del test
            - fileIn        : file con matrice di interi
            - fileOut       : file dove salvare il risultato
            - expected      : numero di colonne dispari
            - expectedMatr  : come deve venira la matrice
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es60(fileIn, fileOut)
        self.assertEqual(type(result), int, "Il risultato non è un intero")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.check_text_file(fileOut, expectedMatr)

    @data(
        ('matrice1.txt', 'matrice1Ris.txt', 3, 'matrice1RisCheck.txt'),
        ('matrice2.txt', 'matrice2Ris.txt', 4, 'matrice2RisCheck.txt')
    )
    @unpack
    def test(self, fileIn, fileOut, expected, expectedMatr):
        return self.do_test(fileIn, fileOut, expected, expectedMatr)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
