import testlib
import isrecursive
import json
import random
from ddt import file_data, ddt, data, unpack

import program

@ddt
class Test(testlib.TestCase):

    def do_test(self, path, expected):
        try:
            isrecursive.decorate_module(program)
            program.es9(path)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)
        
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es9(path)
        self.assertEqual(type(result), list, "Bisogna restituire una lista")
        self.assertEqual(result, expected, "La risposta non e' corretta")
    
    @data(  ('Informatica/Software', [('SistemiOperativi', 287), ('Software', 10), ('BasiDati', 0)]),
            ('Informatica/Hardware', [('Architetture', 12), ('RISC', 5), ('Hardware', 0), ('Processori', 0)]),
            ('Informatica', [('SistemiOperativi', 287), ('Informatica', 23), ('Architetture', 12), ('Software', 10), ('RISC', 5), ('BasiDati', 0), ('Hardware', 0), ('Processori', 0)])
    )
    @unpack
    def test(self, path, lista):
        return self.do_test(path, lista)
    

if __name__ == "__main__":
    Test.main()
