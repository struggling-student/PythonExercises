import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, lista, expected, expectedLst):
        '''Implementazione del test
            - lista         :lista che può essere vuota, contenere interi o contenere liste uguali a se stessa
            - expected      : tupla di 3 valori attesa
            - expectedLst   : come deve diventare la lista
        '''
        lista1 = copy.deepcopy(lista)
        try:
            isrecursive.decorate_module(program)
            program.es79(lista1)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es79(lista)
        self.assertEqual(type(result), tuple, "Il risultato non è una tupla")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.assertEqual(
            lista, expectedLst, f"la lista invertita deve essere {expectedLst} invece che {lista}")

    @data(
        ([3, 3, 5, [[1, 8, [9, 3]], 3, [2, [9, [5, 6], [9]]]]], (13, 66, [
         1, 2, 3, 5, 6, 8, 9]), [[[[[9], [6, 5], 9], 2], 3, [[3, 9], 8, 1]], 5, 3, 3]),
        ([1, 2, 3, 6, 7, [[76, 84, 87], 6, 7, 6, 8, [], [7, 8, 9]], [10, 11, 12], [13, 14, 15, 16], 17], (23, 425, [1, 2, 3, 6, 7, 8, 9, 10, 11,
         12, 13, 14, 15, 16, 17, 76, 84, 87]), [17, [16, 15, 14, 13], [12, 11, 10], [[9, 8, 7], [], 8, 6, 7, 6, [87, 84, 76]], 7, 6, 3, 2, 1]),
        ([49, 48, 47, 46, 45, 44, [43, 42, 41], [], [40, 39, 38], [], [37, 36, 35, 34, 33, 32], [], [], [], [], [], [], [], [31, 30, 29, 28, 27, 26, 25], [24], 23, 22, 21, 20, 19, 18, [17, 16, 15, 14, 13], 12, 11, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0], (50, 1225, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
         25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), [0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, 12, [13, 14, 15, 16, 17], 18, 19, 20, 21, 22, 23, [24], [25, 26, 27, 28, 29, 30, 31], [], [], [], [], [], [], [], [32, 33, 34, 35, 36, 37], [], [38, 39, 40], [], [41, 42, 43], 44, 45, 46, 47, 48, 49])
    )
    @unpack
    def test(self, lista, expected, expectedLst):
        return self.do_test(lista, expected, expectedLst)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
