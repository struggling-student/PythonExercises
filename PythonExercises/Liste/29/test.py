import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, tabella1, tabella2, col, expected, expectedTab):
        '''Implementazione del test
            - tabella1      : tabella sotto forma di lista di dizionari
            - tabella2      : tabella sotto forma di lista di dizionari
            - col           : nome colonna ordinata
            - expected      : numero di righe aggiunte atteso
            - expectedTab   : tabella attesa
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es29(tabella1, tabella2, col)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.assertEqual(tabella1, expectedTab,"La tabella1 non è stata modificata correttamente")

    @data(
        ([{'C1': 1, 'C2': 'x'},{'C1': 3, 'C2': 'a'},{'C1': 4, 'C2':'a'},{'C1': 5, 'C2': 'a'},{'C1': 7, 'C2': 'b'}], [{'C1': 2, 'C2': 'a'},{'C1': 3, 'C2': 'b'},{'C1': 5, 'C2':'a'},{'C1': 6, 'C2': 'b'},{'C1': 7, 'C2': 'a'}], 'C1', 2, [{'C1': 1, 'C2': 'x'},{'C1': 2, 'C2': 'a'}, {'C1': 3,'C2':'a'},{'C1': 4, 'C2': 'a'},{'C1': 5, 'C2': 'a'},{'C1': 6, 'C2': 'b'}, {'C1': 7, 'C2':'b'}]),
        ([{'C1': 1, 'C2': 'x'},{'C1': 2, 'C2': 'a'},{'C1': 3, 'C2':'a'}], [{'C1': 3, 'C2': 'b'},{'C1': 4, 'C2': 'b'},{'C1': 5, 'C2':'a'}], 'C1', 2, [{'C1': 1, 'C2': 'x'},{'C1': 2, 'C2': 'a'}, {'C1': 3,'C2':'a'},{'C1': 4, 'C2': 'b'}, {'C1': 5, 'C2':'a'}]),
        ([{'C1': 1, 'C2': 'x'},{'C1': 2, 'C2': 'a'},{'C1': 3, 'C2':'a'}], [{'C1': 1, 'C2': 'y'},{'C1': 2, 'C2': 'z'},{'C1': 3, 'C2':'t'}], 'C1', 0, [{'C1': 1, 'C2': 'x'},{'C1': 2, 'C2': 'a'},{'C1': 3, 'C2':'a'}])
    )
    @unpack
    def test(self, tabella1, tabella2, col, expected, expectedTab):
        return self.do_test(tabella1, tabella2, col, expected, expectedTab)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
