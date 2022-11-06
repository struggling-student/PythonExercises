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

    def do_test(self, tree, expected):
        '''Implementazione del test
            - tree    : file JSON che contiene l'elenco degli archi
            - expected      : numero atteso di alberi nella foresta
            - expectedJSON  : file JSON come deve venire
        '''
        tree1 = copy.deepcopy(tree)
        try:
            isrecursive.decorate_module(program)
            program.es66(tree1)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es66(tree)
        self.assertEqual(type(result), int, "Il risultato non è un intero")
        self.assertEqual(result, expected, f"Il risultato deve essere {expected} invece che {result}")


    @data(
        ([0, [-1, None, None],[1, [0, None, None],[2, None, None],],], 3),
        ([1, [2, [4, [6, None, [8, None, None]], None], [5, [7, None, [9, None, None]], None]],[3, None, None]], 4),
        ([255197, [633928, [504898, None, [444647, [618336, None, [135295, None, [403880, None, [447206, None, [690827, [478339, None, None], [23577, None, None]]]]]], [745301, None, None]]], [692411, [192501, None, [307256, [315871, [136132, None, [231806, [822980, None, [608643, None, None]], [673946, None, [510695, None, None]]]], [949865, [105739, [755766, [837093, None, None], [643702, None, None]], [660710, [100570, None, None], None]], [987925, [142062, [874365, None, None], [543082, None, None]], [179907, [923260, None, None], [653956, None, None]]]]], [666133, [149691, [54130, None, [555642, [690993, None, None], [708084, None, None]]], [197326, [587093, [449743, None, None], [322590, None, None]], [20822, [812525, None, None], [464026, None, None]]]], [552254, [804041, [693303, None, [251073, None, None]], [982051, [675429, None, None], [756408, None, None]]], [562210, [626296, [48420, None, None], None], None]]]]], None]], [99958, [591631, [88838, [416270, [434459, [271515, [249184, None, [859993, None, [64114, None, None]]], [630599, [489990, [579895, None, None], [359467, None, None]], [115230, None, [584075, None, None]]]], [710576, [303763, [124029, [863844, None, None], [714619, None, None]], [700437, [944599, None, None], None]], [667413, [424691, [436215, None, None], [359581, None, None]], [283517, [68964, None, None], [353252, None, None]]]]], [653800, [749255, None, None], [546358, [348473, [414236, [81958, None, None], None], [868324, [582666, None, None], [29587, None, None]]], [742587, [347714, [983971, None, None], [280843, None, None]], [238890, [448496, None, None], [959455, None, None]]]]]], [445851, [175866, [728117, [431763, [203473, [618029, None, None], [921823, None, None]], [134105, [762063, None, None], [546729, None, None]]], [318015, [106081, [22450, None, None], [986144, None, None]], [362911, [581171, None, None], [147867, None, None]]]], None], [700237, [723930, [95391, None, [780996, [756761, None, None], [374668, None, None]]], [791249, [978699, [562210, None, None], [810643, None, None]], [989296, [422502, None, None], None]]], [247756, [36098, [840873, [642928, None, None], [631046, None, None]], [754774, [547171, None, None], [981401, None, None]]], [738838, [630947, [526893, None, None], [435886, None, None]], [767032, [961895, None, None], [380901, None, None]]]]]]], [625356, [535672, [499526, [80346, [782360, [376095, [435914, None, None], [215725, None, None]], [732243, [438742, None, None], [22905, None, None]]], [314041, [743338, [814678, None, None], [232213, None, None]], [441385, [13425, None, None], [973643, None, None]]]], [236358, [709286, [455367, [221430, None, None], [88450, None, None]], [269730, [977459, None, None], [786030, None, None]]], [795129, [187518, [928366, None, None], [6505, None, None]], [807957, [91918, None, None], [267755, None, None]]]]], [950494, None, [233855, [485632, [267405, [969416, None, None], [101275, None, None]], [106433, [676252, None, None], [909043, None, None]]], [453356, [868068, None, [821470, None, None]], None]]]], [259584, [616091, [530, [786634, [962038, [9681, None, None], [533895, None, None]], [90532, [574246, None, None], [456538, None, None]]], [432592, [190483, [153924, None, None], [308937, None, None]], [946589, [345704, None, None], [418919, None, None]]]], [415451, None, [767767, [980872, None, [287700, None, None]], [33221, [620956, None, None], [617270, None, None]]]]], [641367, None, [675444, [170988, [686182, [505783, None, None], [576646, None, None]], [515993, [901821, None, None], [390412, None, None]]], [641117, [342921, [708829, None, None], None], [762138, [150236, None, None], None]]]]]]], [791307, [732861, None, [555901, [412490, [126772, [325366, [591580, [383017, None, None], [764990, None, None]], None], [319008, [928468, [466448, None, None], [7862, None, None]], [226030, [828084, None, None], [163931, None, None]]]], [59079, None, [203341, [316159, None, [68260, None, None]], [107784, None, [653049, None, None]]]]], [772014, [137911, [751853, [844951, [61018, None, None], [486760, None, None]], [677643, [441773, None, None], [301947, None, None]]], [721232, [350726, [233566, None, None], [576712, None, None]], [647949, [227581, None, None], [581532, None, None]]]], [955532, [321400, None, [737101, None, [133686, None, None]]], [117699, None, [189094, [645260, None, None], [880003, None, None]]]]]]], [70507, [105714, [140939, [868867, [648221, [60635, [742069, None, None], None], [671103, [220251, None, None], [834947, None, None]]], [394401, [477635, [825633, None, None], [879608, None, None]], [421941, [142514, None, None], None]]], [86601, [549094, None, [359389, [770909, None, None], [711469, None, None]]], [791957, [299604, [466169, None, None], [440956, None, None]], [170484, [855559, None, None], [341504, None, None]]]]], [453323, [184352, [196611, None, [518385, [80030, None, None], None]], [408392, [416294, [517229, None, None], [710270, None, None]], [861102, [290578, None, None], [421757, None, None]]]], [276421, [665112, [784798, [385068, None, None], [19426, None, None]], [940547, [11382, None, None], None]], [149083, None, [436378, [187477, None, None], [481617, None, None]]]]]], [141156, [735923, [134579, [604073, [762691, [455202, None, None], [385409, None, None]], [350250, [501032, None, None], [514251, None, None]]], None], [608574, [743878, [415525, [347617, None, None], [182870, None, None]], [543604, [734365, None, None], [532386, None, None]]], [128009, [845449, [788794, None, None], [37116, None, None]], [610600, [294578, None, None], [598833, None, None]]]]], [672157, None, [751506, [790732, [791447, [367589, None, None], [93994, None, None]], [707600, [928142, None, None], None]], [13659, [271812, [578842, None, None], [632769, None, None]], [703303, None, [372781, None, None]]]]]]]]]], 14)
    )
    @unpack
    def test(self, lista, expected):
        tree = albero.AlberoBinario.fromList(lista)
        return self.do_test(tree, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
