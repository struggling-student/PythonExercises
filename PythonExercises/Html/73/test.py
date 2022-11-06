import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive
import my_html

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, path, html, expectedHtml):
        '''Implementazione del test
            - path          : directory da cui partire per la costruzione dell'albero
            - html          : file dove salvare il risultato
            - expectedHtml  : albero di HTMLNode per il confronto del risultato
        '''
        try:
            isrecursive.decorate_module(program)
            program.es73(path, html)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            program.es73(path, html)
        self.check_text_file(html, expectedHtml)


    @data(
        ('t2', 'test.t2.81.html', 'expected.t2.81.html'),
        ('t4', 'test.t4.82.html', 'expected.t4.82.html')
    )
    @unpack
    def test(self, path, html, expectedHtml):
        return self.do_test(path, html, expectedHtml)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
