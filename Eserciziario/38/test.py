import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, labirinto, expected, expectedLab):
        '''Implementazione del test
            - labirinto     : labirinto sotto forma di matrice
            - expected      : posizione della matrice attesa
            - expectedlab   : controllo che la matrice non è cambiata
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es38(labirinto)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.assertEqual(
            labirinto, expectedLab, "Il labirinto  originale  e' stato modificato")

    @data(
        ([[0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1, 0], [
         0, 0, 1, 1, 0, 1, 0], [1, 0, 0, 1, 0, 1, 1], [0, 1, 1, 0, 1, 0, 0]], (4, 5)),
        ([[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]], (7, 6))
    )
    @unpack
    def test(self, lab, expected):
        return self.do_test(lab, expected, lab)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
