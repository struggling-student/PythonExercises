import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, filePNG, fileJSON, expected, expectedJSON):
        '''Implementazione del test
            - fileInJSON    : file PNG
            - fileOutJSON   : file JSON da creare
            - expected      : stringa attesa
            - expectedJSON  : file JSON come deve venire
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es22(filePNG, fileJSON)
        self.assertEqual(type(result), str, "Il risultato non è una stringa")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")
        self.check_json_file(fileJSON, expectedJSON)

    @data(
        ("italia.png", "o1.json","000255000", "t1.json"),
        ("3cime.png", "o2.json","053138219", "t2.json")
    )
    @unpack
    def test(self, filePNG, fileJSON, expected, expectedJSON):
        return self.do_test(filePNG, fileJSON, expected, expectedJSON)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
