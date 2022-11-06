import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, parola, expected):
        '''Implementazione del test
            - parola        : stringa di caratteri
            - expected      : lista delle sottostringhe crescenti attesa
        '''
        par2 = copy.deepcopy(parola)
        try:
            isrecursive.decorate_module(program)
            program.es78(par2)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es78(parola)
        self.assertEqual(type(result), list, "Il risultato non è una lista")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ("fondamenti", ['a', 'ae', 'aei', 'aen', 'aent', 'aet', 'ai', 'am', 'amn', 'amnt', 'amt', 'an', 'ant', 'at', 'd', 'de', 'dei', 'den', 'dent', 'det', 'di', 'dm', 'dmn', 'dmnt', 'dmt', 'dn', 'dnt',
                        'dt', 'e', 'ei', 'en', 'ent', 'et', 'f', 'fi', 'fm', 'fmn', 'fmnt', 'fmt', 'fn', 'fnn', 'fnnt', 'fnt', 'fo', 'fot', 'ft', 'i', 'm', 'mn', 'mnt', 'mt', 'n', 'nn', 'nnt', 'nt', 'o', 'ot', 't']),
        ('RocamBOleSCaMeNTE', ['B', 'BC', 'BCE', 'BCM', 'BCMN', 'BCMNT', 'BCMT', 'BCMe', 'BCN', 'BCNT', 'BCT', 'BCa', 'BCae', 'BCe', 'BE', 'BM', 'BMN', 'BMNT', 'BMT', 'BMe', 'BN', 'BNT', 'BO', 'BOS', 'BOST', 'BOSa', 'BOSae', 'BOSe', 'BOT', 'BOa', 'BOae', 'BOe', 'BOee', 'BOl', 'BS', 'BST', 'BSa', 'BSae', 'BSe', 'BT', 'Ba', 'Bae', 'Be', 'Bee', 'Bl', 'C', 'CE', 'CM', 'CMN', 'CMNT', 'CMT', 'CMe', 'CN', 'CNT', 'CT', 'Ca', 'Cae', 'Ce',
                               'E', 'M', 'MN', 'MNT', 'MT', 'Me', 'N', 'NT', 'O', 'OS', 'OST', 'OSa', 'OSae', 'OSe', 'OT', 'Oa', 'Oae', 'Oe', 'Oee', 'Ol', 'R', 'RS', 'RST', 'RSa', 'RSae', 'RSe', 'RT', 'Ra', 'Raa', 'Raae', 'Rae', 'Raee', 'Ral', 'Ram', 'Rc', 'Rce', 'Rcee', 'Rcl', 'Rcm', 'Re', 'Ree', 'Rl', 'Rm', 'Ro', 'S', 'ST', 'Sa', 'Sae', 'Se', 'T', 'a', 'aa', 'aae', 'ae', 'aee', 'al', 'am', 'c', 'ce', 'cee', 'cl', 'cm', 'e', 'ee', 'l', 'm', 'o']),
        ('Ass7oRibASs8', ['7', '78', '7A', '7AS', '7ASs', '7As', '7R', '7RS', '7RSs', '7Rb', '7Rbs', '7Ri', '7Ris', '7Rs', '7S', '7Ss', '7b', '7bs', '7i', '7is', '7o', '7os', '7s', '8', 'A', 'AA', 'AAS', 'AASs', 'AAs', 'AR', 'ARS',
                          'ARSs', 'ARb', 'ARbs', 'ARi', 'ARis', 'ARs', 'AS', 'ASs', 'Ab', 'Abs', 'Ai', 'Ais', 'Ao', 'Aos', 'As', 'Ass', 'Asss', 'R', 'RS', 'RSs', 'Rb', 'Rbs', 'Ri', 'Ris', 'Rs', 'S', 'Ss', 'b', 'bs', 'i', 'is', 'o', 'os', 's', 'ss', 'sss'])
    )
    @unpack
    def test(self, parola, expected):
        return self.do_test(parola, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
