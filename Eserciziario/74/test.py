import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, filePng, centro, spessore, colori, pngFileOut, expected, expectedPng):
        '''Implementazione del test
            - filePng       : file dove prendere l'immagine da modificare
            - centro        : coordinate (x, y) del centro degli anelli
            - spessore      : spessore degli anelli
            - colori        : lista dei cori per ogni anello
            - pngFileOut    : dove salvare l'immagine modificata
            - expected      : lista del numero di pixel colorati per anello attesa
            - expectedPng   : immagine modificata attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es74(
                filePng, centro, spessore, colori, pngFileOut)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.check_img_file(pngFileOut, expectedPng)

    @data(
        ('3cime.png', (100, 90), 30, [(50, 0, 0), (100, 0, 0), (150, 0, 0), (200, 0, 0), (
            250, 0, 0)], 'test.91.png', [2809, 8468, 14156, 12005, 6583], 'expected.91.png'),
        ('3cime.png', (100, 90), 10, [(0, 20, 0), (0, 40, 0), (0, 60, 0), (0, 80, 0), (0, 100, 0), (0, 120, 0), (0, 140, 0), (0, 160, 0), (
            0, 180, 0), (0, 200, 0)], 'test.92.png', [305, 940, 1564, 2204, 2812, 3452, 4084, 4708, 5364, 5048], 'expected.92.png')
    )
    @unpack
    def test(self, filePng, centro, spessore, colori, pngFileOut, expected, expectedPng):
        return self.do_test(filePng, centro, spessore, colori, pngFileOut, expected, expectedPng)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
