import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, path, lst, expected):
        '''Implementazione del test
            - path      : path alla directory in cui fare la ricerca
            - lst       : lista dele estensioni
            - expected  : dizionario atteso
        '''

        try:
            isrecursive.decorate_module(program)
            program.es68(path, lst)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es68(path, lst)
        self.assertEqual(type(result), dict, "Il risultato non è un dizionario")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ('t1', ['txt', 'jpg'], {'txt': 3, 'jpg': 1, }),
        ('t2', ['txt', 'jpg', 'png', 'testo', 'ttt'],
         {'png': 2, 'txt': 5, 'jpg': 2})
    )
    @unpack
    def test(self, path, lst, expected):
        return self.do_test(path, lst, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
