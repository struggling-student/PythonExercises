import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, path, ext, par, expected):
        '''Implementazione del test
            - path          : path della directory da cui partire con la ricerca
            - ext           : estensioni dei file da non cercare
            - par           : lista di parole da cercare
            - expected      : dizionario atteso
        '''
        try:
            isrecursive.decorate_module(program)
            program.es70(path, ext, par)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es70(path, ext, par)
        self.assertEqual(type(result), dict,
                         "Il risultato non è un dizionario")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ('t3', ['txt', 'testo'], ['PaperIno', 'MINNIE', 'EdI'],
         {'paperino': 2, 'minnie': 2, 'edi': 1, }),
        ('t3', ['testo'], ['Paperino', 'Pippo', 'Pluto', 'Clarabella', 'Orazio'], {
         'paperino': 3, 'pippo': 1, 'clarabella': 1, 'orazio': 1, })
    )
    @unpack
    def test(self, path, ext, par, expected):
        return self.do_test(path, ext, par, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
