import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, path, minp, maxp, expected):
        '''Implementazione del test
            - path      : cartella da cui iniziare la ricerca
            - minp       : dimensione minima del file
            - maxp      : dimensione massima del file
            - expected  : dizionario atteso
        '''
        try:
            isrecursive.decorate_module(program)
            program.es71(path, minp, maxp)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es71(path, minp, maxp)
        self.assertEqual(type(result), dict,
                         "Il risultato non è un dizionario")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")


    @data(
        ('t4', 0, 100, {'looney-tunes.txt': 3, 'minnie.txt': 4}),
        ('t4', 10, 100, {'looney-tunes.txt': 3, }),
        ('t4', 0, 40, {'minnie.txt': 4, })
    )
    @unpack
    def test(self, path, minp, maxp, expected):
        return self.do_test(path, minp, maxp, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
