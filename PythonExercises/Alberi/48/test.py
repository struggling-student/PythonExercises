import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive
import albero

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, tree, expected):
        '''Implementazione del test
            - tree          : albero binario sotto forma di lista
            - expected      : numero di nodi atteso
        '''
        tree1 = albero.AlberoBinario.fromList(tree)
        tree2 = copy.deepcopy(tree1)
        try:
            isrecursive.decorate_module(program)
            program.es48(tree2)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es48(tree1)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ([7, [1, [4, [5, [9, None, None], None], None], [
         6, [2, None, [8, None, None]], None]], [3, None, None]], 2),
        ([9, [2, [6, [5, None, None], [5, None, None]], [6, [5, None, None], [5, None, None]]],
          [4, [6, [5, None, None], [5, None, None]], [6, [5, None, None], [5, None, None]]]], 7),
        ([5, None, [1, [5, None, [1, [5, None, None], None]], None]], 0)
    )
    @unpack
    def test(self, tree, expected):
        return self.do_test(tree, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
