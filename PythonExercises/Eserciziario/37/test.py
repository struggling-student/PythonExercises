import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, listaDiz, expected):
        '''Implementazione del test
            - listaDiz      : lista di dizionari
            - expected      : dizionario atteso
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es37(listaDiz)
        self.assertEqual(type(result), dict,
                         "Il risultato non è un dizionario")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    # ESEMPIO DI BATTERIA DI TEST ELENCATA COME TABELLA

    @data(
        ([{'a': [1, 3, 5], 'b':[2, 3], 'd':[3]}, {'a': [5, 1, 2, 3], 'b':[2], 'd':[3]}, {
         'a': [3, 5], 'c':[4, 1, 2], 'd':[4]}], {'a': {1, 2, 3, 5}, 'b': {2, 3}, 'd': {3, 4}}),
        ([{'a': [1, 2, 3], 'b':[3, 1, 2], 'c':[2, 3, 1]}, {'a': [3, 2, 1], 'b':[4, 3, 2], 'd':[
         1, 3, 2]}], {'a': {1, 2, 3}, 'b': {1, 2, 3, 4}, 'c': {1, 2, 3}, 'd': {1, 2, 3}})
    )
    @unpack
    def test(self, listaDiz, expected):
        return self.do_test(listaDiz, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
