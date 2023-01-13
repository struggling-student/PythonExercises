import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, fileJson, filePng, expected, expectedPng):
        '''Implementazione del test
            - fileJson      : JSON contente la matrice codificata
            - filePng       : dove salvare l'immagine
            - expected      : pixel atteso
            - expectedPng   : PNG come deve venire
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es23(fileJson, filePng)
        self.assertEqual(result, expected,
                         f"Il risultato deve essere {expected} invece che {result}")
        self.check_img_file(filePng, expectedPng)

    @data(
        ('italia.json', 'o1.png', (0, 255, 0), 'italia.png'),
        ('3cime.json', 'o2.png', (53, 138, 219), '3cime.png')
    )
    @unpack
    def test(self, fileJson, filePng, expected, expectedPng):
        return self.do_test(fileJson, filePng, expected, expectedPng)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
