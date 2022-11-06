
# Esempio di test

# IMPORT NECESSARI
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

    def do_test(self, livello, expected):
        '''Implementazione del test
            - livello       : livello dell'albero
            - expected      : albero atteso
        '''
        try:
            isrecursive.decorate_module(program)
            program.es1(livello)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es1(livello)
        self.assertEqual(albero.toLista(result), expected, f"Il risultato deve essere {expected} invece che {result}, input k={livello}")

    @data(  
            (1, [3,[[1,[]],[2,[]]]]),
            (2, [10,[[3,[[1,[]],[2,[]]]],[7,[[3,[]],[4,[]]]]]]),
            (3, [36,[[10,[[3,[[1,[]],[2,[]]]],[7,[[3,[]],[4,[]]]]]],[26,[[11,[[5,[]],[6,[]]]],[15,[[7,[]],[8,[]]]]]]]])
        )
    @unpack
    def test(self, livello, expected):
        return self.do_test(livello, expected)

if __name__ == '__main__':
    Test.main()

