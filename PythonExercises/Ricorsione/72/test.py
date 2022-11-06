import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, path, jsonFile, expected, expectedJson):
        '''Implementazione del test
            - path          : path della directory di partenza
            - jsonFile      : file json dove salvare il risultato
            - expected      : numero di files massimo atteso
            - expectedJSON  : file json atteso
        '''
        try:
            isrecursive.decorate_module(program)
            program.es72(path, jsonFile)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es72(path, jsonFile)
        self.assertEqual(type(result), int, "Il risultato non è un intero")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.check_json_file(jsonFile, expectedJson)


    @data(
        ('t3', 'test.t3.71.json', 3, 'expected.t3.71.json'),
        ('t4', 'test.t4.72.json', 3, 'expected.t4.72.json')
    )
    @unpack
    def test(self, path, jsonFile, expected, expectedJson):
        return self.do_test(path, jsonFile, expected, expectedJson)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
