import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, lista, expected, expectedLst):
        '''Implementazione del test
            - lista       : lista in input
            - expected    : lista ordinata attesa
            - expectedLst : uguale alla lista in input per verificare che non sia stata cambiata
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es47(lista)
        self.assertEqual(type(result), list, "Il risultato non è una lista")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.assertEqual(
            lista, expectedLst, f"La lista in input è stata modificata")

    @data(
        (['uuu', 'ccc', 'a', 'aa', 'd', 'z', 'zzz', 'uuu', 'z',
          'z', 'uuu'], ['z', 'd', 'a', 'aa', 'zzz', 'uuu', 'ccc']),
        (['a', 'a', 'bb', 'bb', 'ccc', 'ccc', 'dddd', 'dddd',
          'eeeee', 'eeeee'], ['a', 'bb', 'ccc', 'dddd', 'eeeee']),
        (['a', 'b', 'c', 'd', 'rr', 'ss', 'ttt', 'uuu', 'vv', 'n', 'm', 'l'],
         ['n', 'm', 'l', 'd', 'c', 'b', 'a', 'vv', 'ss', 'rr', 'uuu', 'ttt'])
    )
    @unpack
    def test(self, lista, expected):
        return self.do_test(lista, expected, lista)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
