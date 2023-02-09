import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, d1, d2, expected):
        '''Implementazione del test
            - d1            : primo dizionario
            - d2            : secondo dizionario
            - expected      : dizionario atteso
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es18(d1, d2)
        self.assertEqual(type(result),  dict,
                         "Il risultato non è un dizionario")
        self.assertEqual(result, expected,
                         f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ({1: {1, 2, 3}, 2: {1, 2, 3}, 5: {1}}, {1: {3, 4, 5}, 3: {1, 2, 3}, 5: {3}, 8: {6}}, {1: ({3}, {1, 2, 3, 4, 5}), 5: (set(), {1, 3})}),
        ({1: {1, 2, 3}, 2: {1, 2, 3}}, {3: {1, 2, 3}, 4: {1, 2, 3}}, {}),
        ({1: set(), 2: {1, 2}, 3: {1, 2}}, {1: set(), 2: {1, 2}, 4: {1, 2}}, {1: (set(), set()), 2: ({1, 2}, {1, 2})})
    )
    @unpack
    def test(self, d1, d2, expected):
        return self.do_test(d1, d2, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
