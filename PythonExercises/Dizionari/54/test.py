import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, lista, expected, expectedLista):
        '''Implementazione del test
            - lista         : lista di interi e stringhe
            - expected      : dizionario atteso
            - expectedLista : lista risultante di interi
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es54(lista)
        self.assertEqual(type(result), dict,
                         "Il risultato non è un dizionario")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.assertEqual(
            lista, expectedLista, f"La lista deve essere modificata in {expectedLista} invece che {lista}")

    @data(
        ([1, 'a', 2, 'b', 'a', 8, 'd', 8], {
         'a': 2, 'b': 1, 'd': 1}, [1, 2, 8, 8]),
        (['a', 'a', 'a', 'a'], {'a': 4}, [])
    )
    @unpack
    def test(self, lista, expected, expectedLista):
        return self.do_test(lista, expected, expectedLista)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
