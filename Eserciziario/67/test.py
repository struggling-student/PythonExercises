import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, path, expected, ):
        '''Implementazione del test
            - path      : path della directory da esplorare
            - expected  : dizionario delle estensioni atteso
        '''
        try:
            isrecursive.decorate_module(program)
            program.es67(path)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es67(path)
        self.assertEqual(type(result), dict,
                         "Il risultato non è un dizionario")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ('A1', {'www': 4, 'sss': 3, 'nnn': 2, 'uuu': 2, 'zzz': 0, 'txt': 2, 'jjj': 0, 'aaa': 0, 'ppp': 1, 'ooo': 0, 'ccc': 0, 'vvv': 1, 'xxx': 1,
                'iii': 2, 'bbb': 1, 'ggg': 2, 'png': 0, 'ttt': 3, 'hhh': 3, 'kkk': 5, 'fff': 0, 'mmm': 0, 'rtf': 0, 'qqq': 0, 'doc': 0, 'ddd': 0}),
        ('A2', {'zzz': 9, 'png': 7, 'txt': 6, 'www': 9, 'ddd': 7, 'ooo': 6, 'rrr': 4, 'jjj': 5, 'pdf': 6, 'uuu': 7, 'yyy': 5, 'fff': 6, 'bbb': 6, 'doc': 7, 'aaa': 8,
                'ggg': 7, 'iii': 6, 'kkk': 5, 'mmm': 7, 'nnn': 8, 'rtf': 8, 'qqq': 3, 'vvv': 10, 'hhh': 8, 'ppp': 4, 'ccc': 4, 'lll': 5, 'xxx': 6, 'ttt': 6, 'eee': 4, 'sss': 4}),
        ('A3', {'ddd': 13, 'doc': 12, 'yyy': 11, 'mmm': 9, 'uuu': 9, 'lll': 8, 'hhh': 14, 'qqq': 11, 'xxx': 9, 'iii': 7, 'ooo': 9, 'vvv': 11, 'nnn': 7, 'ggg': 10, 'rtf': 10,
                'pdf': 10, 'rrr': 12, 'eee': 10, 'fff': 13, 'ppp': 10, 'sss': 10, 'jjj': 11, 'bbb': 8, 'aaa': 12, 'ccc': 9, 'kkk': 8, 'www': 9, 'txt': 9, 'zzz': 10, 'ttt': 9, 'png': 9})
    )
    @unpack
    def test(self, path, expected):
        return self.do_test(path, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
