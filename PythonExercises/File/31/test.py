import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, f1, f2, expected, expectedGen):
        '''Implementazione del test
            - f1            : file di testo in input
            - f2            : path dove salvare il risultato
            - expected      : numero di caratteri trasformati atteso
            - expectedGen   : stringa generata attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es31(f1, f2)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        with open(f2, 'r', encoding='utf8') as f:
            testo = f.read()
        self.assertEqual(
            testo, expectedGen, f"Il tetso generato deve essere {expected} invece che {result}")

    @data(
        ('ftesto3.txt', 'risposta3.txt', 7, 'MoNtI, SterBINI e SPoGNArDI'),
        ('ftesto4.txt', 'risposta4.txt', 8, '''SalvE, Ho Una doManda:\nMa lo zERo E' Un nUMERo paRi o diSpaRi?\nSo cHE pUo' SEMbRaRE Una banaliTa', a naSo diREi cHE lo zERo E' Un nUMERo paRi\nMa non SapREi coME GiUSTificaRE la RiSpoSTa.\nConfido nEl voSTRo aiUTo!''')
    )
    @unpack
    def test(self, f1, f2, expected, expectedGen):
        return self.do_test(f1, f2, expected, expectedGen)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
