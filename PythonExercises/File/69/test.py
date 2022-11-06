import copy
import testlib
import json
import os
import random
import shutil
from ddt import file_data, ddt, data, unpack
import isrecursive

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, path, prof, lst, expected, present, absent):
        '''Implementazione del test
            - path          : directory da cui iniziare la ricerca
            - prof          : profondità a cui eliminare i file
            - lst           : lista delle estensioni
            - expected      : numero di file atteso
            - present       : path dei file da non cancellare
            - absent        : path dei file da cancellare
        '''
        dir2 = path + "Copy"
        shutil.rmtree(dir2, ignore_errors=True)
        shutil.copytree(path, dir2)
        try:
            isrecursive.decorate_module(program)
            program.es69(dir2, prof, lst)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)
        shutil.rmtree(dir2, ignore_errors=True)
        shutil.copytree(path, dir2)
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es69(dir2, prof, lst)
        self.assertEqual(type(result), int, "Il risultato non è un intero")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        for f in present:
            self.assertTrue(os.path.exists(f), f"Non dovevi eliminare il file {f}")
        for f in absent:
            self.assertFalse(os.path.exists(f), f"Dovevi eliminare il file {f}")


    @data(
        ('t2', 3, ['jpg', 'png'], 6, ['t2Copy/paperino.jpg', 't2Copy/u1/topolino.txt', 't2Copy/u1/v2/w3/topolino.txt', 't2Copy/u2/v1/w4/x3/minnie.png',
                                      't2Copy/u3/v2/minnie.txt', 't2Copy/u3/v1/w1/minnie.txt'], ['t2Copy/u1/v3/w1/paperino.jpg', 't2Copy/u2/v1/w4/minnie.png'])
    )
    @unpack
    def test(self, path, prof, lst, expected, present, absent):
        return self.do_test(path, prof, lst, expected, present, absent)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
