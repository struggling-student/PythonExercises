import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, img1, img2, img3, expected, expectedImg):
        '''Implementazione del test
            - img1          : file prima immagine
            - img2          : file seconda immagine
            - img3          : dove salvare la nuova immagine
            - expected      : numero pixel atteso
            - expectedJSON  : immagine attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es49(img1, img2, img3)
        self.assertEqual(result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.check_img_file(img3, expectedImg)


    @data(
        ('foto1.png','foto2.png','test1.png', 30003, 'RisTest1.png'),
        ('foto1.png','foto3.png','test2.png', 2573, 'RisTest2.png'),
        ('foto3.png','foto1.png','test3.png', 2630, 'RisTest3.png')
    )
    @unpack
    def test(self, img1, img2, img3, expected, expectedImg):
        return self.do_test(img1, img2, img3, expected, expectedImg)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
