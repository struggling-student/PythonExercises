
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

    def do_test(self, png1, png2, png3, expected, exceptedPng):
        '''Implementazione del test
            - png1          : prima immagine in input
            - png2          : seconda immagine in input
            - png3          : path dove salvare la nuova immagine
            - expected      : numero di pixel neri attesi
            - expectedJSON  : immagine attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es15(png1, png2, png3)
        self.assertEqual(result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.check_img_file(png3, exceptedPng)

    @data(  
            ('foto1.png','foto2.png','test1.png', 5000, 'RisTest1.png'),
            ('foto1.png','foto3.png','test2.png', 6200, 'RisTest2.png'),
            ('foto2.png','foto3.png','test3.png', 6200, 'RisTest3.png')
        )
    @unpack
    def test(self, foto1, foto2, foto3, expected, expectedPng):
        return self.do_test(foto1, foto2, foto3, expected, expectedPng)

# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()

