import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program

@ddt
class Test(testlib.TestCase):

    def do_test(self, fimm,fimm1,h1,w1, expected, expectedImg):
        result   = program.es4(fimm,fimm1,h1,w1)
        self.assertEqual(result, expected, "il valore restituito non e' corretto")
        self.check_img_file(fimm1, expectedImg)
    
    def test_1(self):
        ''' \nPrimo  test della funzione es8 dove  viene passata l'immagine cubo.png con h1=w1= 2 
        e creata l'immagine test8_1.png che deve corrispondere a quella in RisTest1.png'''
        #return self.do_test('cubo.png', 'test8_1.png', 2, 2, (185, 182, 187), 'RisTest1.png')
        return self.do_test('cubo.png', 'test8_1.png', 2, 2, (255, 255, 255), 'RisTest1.png')

    def test_2(self):
        ''' \nSecondo test della funzione es8 dove viene passata l'immagine fotoBN.png con h1=2 e w1=3 
        e creata l'immagine test8_2.png che deve corrispondere a quella in RisTest2.png'''
        #return self.do_test('fotoBN.png', 'test8_2.png', 2, 3, (255, 255, 255), 'RisTest2.png')
        return self.do_test('fotoBN.png', 'test8_2.png', 2, 3, (0, 0, 0), 'RisTest2.png')

    def test_3(self):
        ''' \nTerzo test della funzione es8 dove viene passata l'immagine cubo.png con h=1 e w=3 
        e creata l'immagine test8_3.png che deve corrispondere a quella in RisTest8_1.png'''
        #return self.do_test('cubo.png', 'test8_3.png', 1, 3, (185, 182, 187), 'RisTest3.png')
        return self.do_test('cubo.png', 'test8_3.png', 1, 3, (255, 255, 255), 'RisTest3.png')

if __name__ == "__main__":
    Test.main()
