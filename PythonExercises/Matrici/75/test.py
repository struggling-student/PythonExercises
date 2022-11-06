import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, w, h, listaColori, listaAltezze, larghezzaPalazzo, filePngOut, expected, expectedPng):
        '''Implementazione del test
            - w                 : larghezza dell'immagine
            - h                 : altezza dell'immagine
            - listaColori       : lista dei colori da applicare ai rettangoli
            - listaAltezze      : lista delle altezze dei rettangoli
            - larghezzaPalazzo  : larghezza dei palazzi
            - filePngOut        : file Png dove salvare lì'immagine
            - expected          : numero di pixel appartenenti a più rettangoli atteso
            - expectedPng       : immagine attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es75(
                w, h, listaColori, listaAltezze, larghezzaPalazzo, filePngOut)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.check_img_file(filePngOut, expectedPng)

    @data(
        (1200, 500, [(20, 0, 0), (40, 0, 0), (60, 0, 0), (80, 0, 0), (100, 0, 0), (120, 0, 0), (140, 0, 0), (160, 0, 0), (180, 0, 0), (200, 0, 0), (220, 0, 0)], [
         100, 150, 220, 360, 340, 300, 100, 280, 370, 320, 200], 200, 'test.101.png', [211000], ['expected.101.png']),
        (1200, 500, [(0, 10, 0), (0, 20, 0), (0, 30, 0), (0, 40, 0), (0, 50, 0), (0, 60, 0), (0, 70, 0), (0, 80, 0), (0, 90, 0), (0, 100, 0), (0, 110, 0), (0, 120, 0), (0, 130, 0), (0, 140, 0), (0, 150, 0), (0, 160, 0), (0, 170, 0), (0, 180,
                                                                                                                                                                                                                                          0), (0, 190, 0), (0, 200, 0), (0, 210, 0)], [410, 390, 300, 240, 110, 320, 420, 280, 340, 30, 40, 80, 390, 420, 330, 500, 420, 300, 480, 350, 320], 200, 'test.102.png', [387980, 374500], ['expected.102-1.png', 'expected.102-2.png'])
    )
    @unpack
    def test(self, w, h, listaColori, listaAltezze, larghezzaPalazzo, filePngOut, expected, expectedPng):
        try:
            print("\ntrying first interpretation")
            return self.do_test(w, h, listaColori, listaAltezze, larghezzaPalazzo, filePngOut, expected[0], expectedPng[0])
        except:
            print("\ntrying second interpretation")
            return self.do_test(w, h, listaColori, listaAltezze, larghezzaPalazzo, filePngOut, expected[1], expectedPng[1])


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
