import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, dir1, lst, expected):
        '''Implementazione del test
            - dir1          : path di una directory da cui iniziare la ricerca
            - lst           : lista di stringhe 
            - expected      : dizionario atteso
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es80(dir1, lst)
        self.assertEqual(type(result), dict,
                         "Il risultato non è un dizionario")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")


    @data(
        ('A', ['aw', 'ipip'], {'aw': [13, 5]}),
        ('A', ['t', 'op', 'g', 'gc'], {
         'op': [12, 5], 'g': [360, 5], 'gc': [15, 5], 't': [420, 5]}),
        ('A', ['uz', 'zz', 'xx', 'gg', 'ssfb', 'zzn', 'qaiqgnys', 'cbjzrbhdds', 'y', 'r', 'il'], {'gg': [16, 5], 'cbjzrbhdds': [1, 4], 'zzn': [
         2, 4], 'xx': [12, 5], 'il': [13, 5], 'y': [379, 5], 'zz': [15, 5], 'ssfb': [1, 3], 'r': [418, 5], 'uz': [10, 5], 'qaiqgnys': [1, 5]})
    )
    @unpack
    def test(self, dir1, lst, expected):
        return self.do_test(dir1, lst, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
