
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

    def do_test(self, lista, k, expected, expectedLst):
        '''Implementazione del test
            - lista         : lista di parole
            - k             : intero positivo
            - expected      : numero atteso di parole cancellate
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es17(lista, k)
        self.assertEqual(type(result), int,
                         "Il risultato non è un intero")
        self.assertEqual(result, expected,
                         f"Il risultato deve essere {expected} invece che {result}")
        self.assertEqual(lista, expectedLst,
                         f"Il risultato deve essere {expectedLst} invece che {result}")

    @data(
        (['ananas', 'pera', 'banana', 'melone', 'kiwi',
          'albicocca'], 3, 3, ['pera', 'melone', 'kiwi']),
        (['Angelo', 'Andrea', 'Osvaldo', 'Anna',
          'Monica', 'Adele'], 2, 4, ['Angelo', 'Monica']),
        (['uAaa', 'uaAa', 'uaaA', 'Bcc', 'cBc', 'ccB'], 3, 3, ['Bcc', 'cBc', 'ccB'])
    )
    @unpack
    def test(self, lista, k, expected, expectedLst):
        return self.do_test(lista, k, expected, expectedLst)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
