import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, k, lista, fout, expected, expectedPng):
        '''Implementazione del test
            - k             : lato dell'immagine quadrata da creare
            - lista         : lista di quadrati sottoforma di sestuple (x, y, l, r, g, b)
            - fout          : path dove salvare l'immagine png
            - expected      : numero di pixel neri attesi
            - expectedPng   : immagine png attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es65(k, lista, fout)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.check_img_file(fout, expectedPng)

    @data(
        (100, [(20, 50, 20, 0, 255, 0), (30, 60, 20, 255, 0, 0), (60, 50, 20,
                                                                  255, 0, 0), (70, 60, 20, 0, 255, 0)], 'out1.png', 8600, 'prova1.png'),
        (100, [(30, 60, 40, 0, 150, 0), (10, 40, 30, 0, 200, 0), (60, 20, 50, 0, 100, 0),
               (30, 10, 40, 0, 150, 0), (80, 90, 20, 0, 250, 0)], 'out2.png', 4300, 'prova2.png'),
        (500, [(361, 88, 132, 148, 202, 114), (309, 346, 213, 26, 7, 162), (279, 234, 219, 157, 147, 255), (119, 238, 51, 78, 143, 144), (421, 156, 234, 87, 148, 121), (257, 423, 250, 41, 100, 23), (486, 312, 209, 254, 210, 218), (456, 90, 220, 235, 211, 4), (424, 191, 120, 192, 201, 241), (169, 419, 239, 221, 134, 61), (121, 4, 200,
                                                                                                                                                                                                                                                                                                                                   228, 158, 69), (238, 377, 163, 35, 225, 225), (74, 259, 84, 166, 98, 8), (283, 369, 195, 234, 249, 13), (22, 270, 104, 153, 242, 170), (329, 259, 75, 216, 232, 64), (256, 432, 178, 98, 147, 44), (453, 262, 197, 150, 105, 98), (323, 205, 117, 158, 53, 204), (136, 185, 139, 245, 141, 234)], 'out3.png', 89517, 'risTest2c.png')
    )
    @unpack
    def test(self, k, lista, fout, expected, expectedPng):
        return self.do_test(k, lista, fout, expected, expectedPng)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
