import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, ls, c, expected, expectedLst):
        '''Implementazione del test
            - ls            : lista di strignhe
            - c             : un carattere
            - expected      : lista attesa
            - expectedLst   : come deve essere modificata la lista
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es51(ls, c)
        self.assertEqual(
            ls, expectedLst, f"La lista in input deve diventare {expectedLst} invece che {ls}")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        (['Angelo', 'Andrea', 'Fabio', 'Francesco',
          'Lucio', 'Luca', 'Ugo'], 'a', 5, ['Lucio', 'Ugo']),
        (['Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio', 'Luca', 'Ugo'],
         'G', 2, ['Andrea', 'Fabio', 'Francesco', 'Lucio', 'Luca']),
        (['Angelo', 'Andrea', 'Fabio', 'Francesco', 'Lucio', 'Luca', 'Ugo'],
         'f', 2, ['Angelo', 'Andrea', 'Lucio', 'Luca', 'Ugo'])
    )
    @unpack
    def test(self, ls, c, expected, expectedLst):
        return self.do_test(ls, c, expected, expectedLst)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
