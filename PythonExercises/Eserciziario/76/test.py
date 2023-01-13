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
            - expected      : lista dei suffissi attesa
        '''
        par2 = copy.deepcopy(parola)
        try:
            isrecursive.decorate_module(program)
            program.es76(par2)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es76(parola)
        self.assertEqual(type(result), list, "Il risultato non è una lista")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")

    @data(
        ("fondamenti", ['fondamenti', 'ondamenti', 'ndamenti',
                        'damenti', 'amenti', 'menti', 'enti', 'nti', 'ti', 'i']),
        ('supercalifragilistichespiralidoso', ['supercalifragilistichespiralidoso', 'upercalifragilistichespiralidoso', 'percalifragilistichespiralidoso', 'ercalifragilistichespiralidoso', 'rcalifragilistichespiralidoso', 'califragilistichespiralidoso', 'alifragilistichespiralidoso', 'lifragilistichespiralidoso', 'ifragilistichespiralidoso', 'fragilistichespiralidoso',
                                               'ragilistichespiralidoso', 'agilistichespiralidoso', 'gilistichespiralidoso', 'ilistichespiralidoso', 'listichespiralidoso', 'istichespiralidoso', 'stichespiralidoso', 'tichespiralidoso', 'ichespiralidoso', 'chespiralidoso', 'hespiralidoso', 'espiralidoso', 'spiralidoso', 'piralidoso', 'iralidoso', 'ralidoso', 'alidoso', 'lidoso', 'idoso', 'doso', 'oso', 'so', 'o']),
        ('3gne.nm/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', ['3gne.nm/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', 'gne.nm/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', 'ne.nm/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', 'e.nm/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '.nm/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', 'nm/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', 'm/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '/&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '&$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '$/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '/"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '"(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '(/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '/&!=g34ny2.-3,y.53n7o2n4tt$"#§*n',
                                                           '&!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '!=g34ny2.-3,y.53n7o2n4tt$"#§*n', '=g34ny2.-3,y.53n7o2n4tt$"#§*n', 'g34ny2.-3,y.53n7o2n4tt$"#§*n', '34ny2.-3,y.53n7o2n4tt$"#§*n', '4ny2.-3,y.53n7o2n4tt$"#§*n', 'ny2.-3,y.53n7o2n4tt$"#§*n', 'y2.-3,y.53n7o2n4tt$"#§*n', '2.-3,y.53n7o2n4tt$"#§*n', '.-3,y.53n7o2n4tt$"#§*n', '-3,y.53n7o2n4tt$"#§*n', '3,y.53n7o2n4tt$"#§*n', ',y.53n7o2n4tt$"#§*n', 'y.53n7o2n4tt$"#§*n', '.53n7o2n4tt$"#§*n', '53n7o2n4tt$"#§*n', '3n7o2n4tt$"#§*n', 'n7o2n4tt$"#§*n', '7o2n4tt$"#§*n', 'o2n4tt$"#§*n', '2n4tt$"#§*n', 'n4tt$"#§*n', '4tt$"#§*n', 'tt$"#§*n', 't$"#§*n', '$"#§*n', '"#§*n', '#§*n', '§*n', '*n', 'n'])
    )
    @unpack
    def test(self, parola, expected):
        return self.do_test(parola, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
