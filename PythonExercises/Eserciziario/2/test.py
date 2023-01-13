import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program

@ddt
class Test(testlib.TestCase):
    
    def do_test(self, ls, ftesto, expected, expectedLs):
        '''Implementazione del test:
            - ls: lista di stringhe 
            - ftesto: path ad un file di testo
            - expected: il risultato atteso
            - expectedLs: la lista modificata attesa
        '''
        with    self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result   = program.es2(ls, ftesto)
        self.assertEqual(result, expected, "La risposta non è corretta")
        self.assertEqual(ls, expectedLs, "La lista ls non è stata modificata correttamente")
    
    def test_1(self):
        ''' \nPrimo test della funzione es4 con ls=['b', 'abba', 'babc','ccc', 'bba', 'bb' ]
        e  file di testo 'ft1.txt' '''
        ls = ['b', 'abba', 'babc','ccc', 'bba', 'bb' ]
        res_ls = ['b', 'babc', 'bba', 'bb']
        return self.do_test(ls, "ft1.txt", 2, res_ls)

    def test_2(self):
        ''' \nSecondo test della funzione es4 con ls=[ 'bab', 'abba','bc', 'cc', 'ccc' ] e  
        file di testo 'ft1.txt' '''
        ls = [ 'bab', 'abba','bc', 'cc', 'ccc' ]
        res_ls = []
        return self.do_test(ls, "ft1.txt", 5, res_ls)
    
    def test_3(self):
        ''' \nTerzo test della funzione es4 con ls=['b', 'ab', 'ba', 'b', 'c' 'c' 'cc']
        e  file di testo 'ftesto.txt' '''
        ls = ['b', 'ab', 'ba', 'b', 'c' 'c' 'cc']
        res_ls = ['b', 'ab', 'ba', 'b', 'cccc']
        return self.do_test(ls, "ft1.txt", 0, res_ls)

if __name__ == "__main__":
    Test.main()
