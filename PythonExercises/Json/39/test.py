import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, n, fjson, expected, expectedJson):
        '''Implementazione del test
            - n             : ordine della matrice a spirale
            - fjson         : file json dove salvare la matrice
            - expected      : somma delle colonne pari della matrice
            - expectedJson  : file json per controllare la correttezza della matrice
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es39(n, fjson)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.check_json_file(fjson, expectedJson)

    @data(
        (4, 'f4a.json', 74, 'Ris4a.json'),
        (10, 'f4b.json', 2569, 'Ris4b.json')
    )
    @unpack
    def test(self, n, fjson, expected, expectedJson):
        return self.do_test(n, fjson, expected, expectedJson)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
