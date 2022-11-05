import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, parola, expected):
        '''Implementazione del test
            - parola    : stringa di caratteri
            - expected  : stringa palindroma attesa
        '''
        parola1 = parola
        try:
            isrecursive.decorate_module(program)
            program.es46(parola1)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es46(parola)
        self.assertEqual(type(result), str, "Il risultato non è una stringa")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ("zzzcdcaaabvv", "aaa"),
        ("adbbabbcbbaad", "abbcbba"),
        ("monti_sterbini_spognardi", "ini")
    )
    @unpack
    def test(self, parola, expected):
        return self.do_test(parola, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
