import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program

@ddt
class Test(testlib.TestCase):

    def do_test(self, insieme, expected):
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es8(insieme)
        self.assertEqual(type(result), list, "Bisogna restituire una lista")
        self.assertEqual(result, expected, "La risposta non e' corretta")

    @data(  
        ({  'aaaa', 'acde', 'aacd', 'aaaade'},  ['aaaaaade', 'aaaaade', 'aaaacd', 'aaaade', 'aacde']),
        ({  'baxyy', 'abcabc', 'abccba', 'yyxab'}, ['abcabccba', 'abccbaxyy', 'baxyyxab', 'yyxabcabc', 'yyxabccba']),
        ({  'xabc', 'xab', 'xxyy', 'yyxx'}, ['xabc', 'xxyyxx', 'yyxxyy'])
        )
    @unpack
    def test(self, insieme, expected):
        return self.do_test(insieme, expected)



if __name__ == '__main__':
    Test.main()

