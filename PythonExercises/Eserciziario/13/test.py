import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program

@ddt
class Test(testlib.TestCase):

    def do_test(self, file1, file2, expected, expectedImg):
        '''Implementazione del test
            - fileInJSON    : file JSON che contiene l'elenco degli archi
            - fileOutJSON   : file JSON da creare
            - expected      : numero atteso di alberi nella foresta
            - expectedJSON  : file JSON come deve venire
        '''

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
            result = program.es13(file1, file2)
        self.assertEqual(result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.check_img_file(file2, expectedImg)


    @data(  
            ('Foto1.png','testFoto1.png', 448, 'RisFoto1.png'),
            ('Foto2.png','testFoto2.png', 4, 'RisFoto2.png'),
            ('Foto3.png','testFoto3.png', 290, 'RisFoto3.png')
        )
    @unpack
    def test(self, file1, file2, expected, expectedImg):
        return self.do_test(file1, file2, expected, expectedImg)

if __name__ == '__main__':
    Test.main()

