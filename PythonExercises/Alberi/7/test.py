import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive
import albero

import program

@ddt
class Test(testlib.TestCase):
    def do_test(self, lista, ins, k, expected):
        tree = albero.fromLista(lista)
        try:
            isrecursive.decorate_module(program)
            program.es7(tree,ins,k)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)
        tree = albero.fromLista(lista)        
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es7(tree, ins, k)
        self.assertEqual(result, expected, "il valore restituito non e' corretto")

    def test_1(self):
        '''\nPrimo test della funzione es1 con insieme= {1,2,3,5,9}, k= 2 e albero:
        
                5
        ________|_____________
        |          |           |
        20         4           6
        |     _____|______  
        11   |   |  |  |  |
            10  2  9  8  7
                __|__   
            |     |
            3     1 

        '''
        lista1= [5, [[20, [[11, []]]], [4, [[10, []], [2, [[3, []], [1, []]]], [9, []], 
        [8, []],[7, []]]],[6, []]]]
        return self.do_test(lista1, {1,2,3,5,9}, 2, 2)

    def test_2(self):
        '''\nSecondo test della funzione es1 con insieme= {1,2,3,5,9}, k= 2 e albero:
        
                        7               
                _______|______         
                |              |        
                5              9        
            ___|___        ___|__      
            |       |      |      |     
            10      8      3      1     
        _|_     _|_    _|_    _|_    
        |   |   |   |  |   |  |   |   
        1   2   12  13 15  6  4   0   
                                        
    
        '''
        lista2=[7,[[5,[[10,[[1,[]],[2,[]]]],[8,[[12,[]],[13,[]]]]]],[9,[[3,[[15,[]],[6,[]]]],
        [1,[[4,[]],[0,[]]]]]]]]
        return self.do_test(lista2, {1,2,3,5,9}, 2, 3)
    
    def test_3(self):
        '''\nTerzo test della funzione es1 con insieme= {12,21,29,30,81,94}, k= 1 e albero:
            
                                76                            
                    ______________|_______________              
                |                              |             
                12                              37            
            _______|_______              _________|_____        
        |               |            |      |        |       
        15             80           71     39        100     
        __|__          ___|____     __|__            __|___    
        |     |         |       |   |     |          |      |   
        5     19        47      96  92   67         23      121 
        ___|___    __|___         ____|______     |      |   
        |       |  |      |       |     |     |    |      |   
        181     28 94     29      70    83    8   81     44   
                                                |               
                                            30               
                                            _|_              
                                            |   |             
                                            46  21             

        '''
        lista3= [76, [[12, [[15, [[5, []], [19, [[181, []], [28, []]]]]], 
        [80, [[47, [[94, []], [29, []]]],[96, []]]]]], [37, [[71, [[92, []], 
        [67, [[70, []], [83, []], [8, [[30, [[46, []], [21, []]]]]]]]]],
        [39, []], [100, [[23, [[81, []]]], [121, [[44, []]]]]]]]]]
        #tree3   = albero.fromLista(lista3)
        return self.do_test(lista3, {12,21,29,30,81,94}, 1, 4)


if __name__ == '__main__':
    Test.main()
