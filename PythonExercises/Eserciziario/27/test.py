import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, tabella, colonna, valore, expected, expectedTab):
        '''Implementazione del test
            - tabella       : tabella sotto forma di lista di dizionari
            - colonna       : nome della colonna
            - valore        : valore da confrontare
            - expected      : differenza attesa
            - expectedTab   : tabella modificata attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es27(tabella, colonna, valore)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.assertEqual(
            tabella, expectedTab, f"Il risultato deve essere {expectedTab} invece che {tabella}")

    @data(
        ([{'C1': 2, 'C2': 1, 'C3': 'd'}, {'C1': 4, 'C2': 7, 'C3': 'a'}, {'C1': 6, 'C2': 1, 'C3': 'b'}, {
         'C1': 8, 'C2': 3, 'C3': 'c'}], 'C2', 1, 2, [{'C1': 2, 'C3': 'd'}, {'C1': 6, 'C3': 'b'}]),
        ([{'C1': 2, 'C2': 1, 'C3': 'd'}, {'C1': 4, 'C2': 7, 'C3': 'a'}, {
         'C1': 6, 'C2': 1, 'C3': 'b'}, {'C1': 8, 'C2': 3, 'C3': 'c'}], 'C1', 3, 4, [])
    )
    @unpack
    def test(self, tabella, colonna, valore, expected, expectedTab):
        return self.do_test(tabella, colonna, valore, expected, expectedTab)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
