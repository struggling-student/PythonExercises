import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, f1, f2, f3, expected, expectedDec):
        '''Implementazione del test
            - f1            : file con la stringa codificata
            - f2            : file che contiene le codifiche dei caratteri
            - f3            : file dove salvare la stringa decodificata
            - expected      : numero di caratteri '?' atteso
            - expectedDec   : Stringa decodificata attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es30(f1, f2, f3)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        with open(f3,'r', encoding='utf8') as f:
            testo_dec = f.read()
        self.assertEqual(
            testo_dec, expectedDec, f"La decodifica {testo_dec} deve essere invece {expectedDec}")
        

    @data(
        ('ftesto1.txt','ftesto1b.txt','risposta1.txt', 2,'tutt?      a    n?nna?'),
        ('ftesto2.txt','ftesto2b.txt','risposta2.txt', 2, '?hi stu?ia passa!')
    )
    @unpack
    def test(self, f1, f2, f3, expected, expectedDec):
        return self.do_test(f1, f2, f3, expected, expectedDec)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
