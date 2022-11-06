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

    def do_test(self, percorsi, expected):
        '''Implementazione del test
            - percorsi: l'insieme di stringhe in input
            - expected: l'albero atteso, sotto forma di lista di liste
        '''

        testRic = copy.deepcopy(percorsi)
        try:
            isrecursive.decorate_module(program)
            program.es6(testRic)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        # test output
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es6(percorsi)
        tree = albero.AlberoBinario.fromList(expected)
        self.assertEqual(result, tree, "L'albero non è corretto.")

    def test_1(self):
        percorsi = {'achi', 'qpmi', 'gjhi', 'fchi', 'mpmi', 'kmi', 'kjhi'}
        expected = ['i',    ['h',   ['c',   ['a', None, None], ['f', None, None]], ['j',   ['g', None, None], [
            'k', None, None]]], ['m',   ['k',   None, None], ['p',   ['m', None, None], ['q', None, None]]]]
        return self.do_test(percorsi, expected)

    def test_2(self):
        percorsi = {'CFBHV', 'TSHV', 'BHV', 'ONSHV',
                    'FBHV', 'YZWV', 'ZWV', 'WV', 'JNSHV'}
        expected = ['V',    ['H',   ['B',   None, ['F',   ['C', None, None], None]], ['S',   ['N',   [
            'J', None, None], ['O', None, None]], ['T',   None, None]]], ['W',   None, ['Z',   ['Y',   None, None], None]]]
        return self.do_test(percorsi, expected)

    def test_3(self):
        percorsi = {'mljo', 'cejo', 'ljo', 'yzo', 'zo', 'hifejo', 'ifejo', 'tuyzo',
                    'qptuyzo', 'wvuyzo', 'rqptuyzo', 'vuyzo', 'fejo', 'acejo', 'ptuyzo'}
        expected = ['o',    ['j',   ['e',   ['c',   ['a',   None, None], None], ['f',   None, ['i',   ['h', None, None], None]]], ['l',   None, ['m',   None,   None]]], [
            'z',   ['y',   ['u',   ['t',   ['p',   None, ['q',   None, ['r', None, None]]], None], ['v',   None, ['w', None, None]]], None], None]]
        return self.do_test(percorsi, expected)


if __name__ == '__main__':
    Test.main()
