import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, s1, s2, expected):
        '''Implementazione del test
            - s1        : stringa di caratteri
            - s2        : stringa di caratteri
            - expected  : lista di sottostringhe comuni atteso
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es45(s1, s2)
        self.assertEqual(type(result), list, "Il risultato non è un insieme")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ('aabbccdd', 'acccdzza', ['a', 'c', 'cc', 'ccd', 'cd', 'd']),
        ('python2', 'python3', ['h', 'ho', 'hon', 'n', 'o', 'on', 'p', 'py', 'pyt', 'pyth',
                                'pytho', 'python', 't', 'th', 'tho', 'thon', 'y', 'yt', 'yth', 'ytho', 'ython']),
        ('fondamenti_di_programmazione', 'progettazione_di_algoritmi', ['_', '_d', '_di', '_di_', 'a', 'az', 'azi', 'azio', 'azion', 'azione', 'd', 'di', 'di_', 'e',
                                                                        'g', 'i', 'i_', 'io', 'ion', 'ione', 'm', 'n', 'ne', 'o', 'og', 'on', 'one', 'p', 'pr', 'pro', 'prog', 'r', 'ro', 'rog', 't', 'z', 'zi', 'zio', 'zion', 'zione'])
    )
    @unpack
    def test(self, s1, s2, expected):
        return self.do_test(s1, s2, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
