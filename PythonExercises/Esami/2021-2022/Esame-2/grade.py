# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
from tree import BinaryTree as BinTree

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
import program

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

#### Use DEBUG=True to disable the recursion tests and enable the
#### stack trace: each error will produce a more verbose output
####
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
#DEBUG = True
DEBUG = False
#############################################################################

def error_message(res, expected, msg=None):
    msg_std = f"Valore NON corretto! [NOT OK]\n TUO RISULTATO = {res} \n ma e' ATTESO = {expected}"
    if msg is None:
        msg = msg_std
    else:
        msg = msg + msg_std
    print('*'*50)
    print(msg)

def test_personal_data_entry():
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', "ERROR: Please assign the 'name' variable with YOUR NAME in program.py"
        assert program.surname    != 'SURNAME', "ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py"
        assert program.student_id != 'MATRICULATION NUMBER', "ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py"
    else:
        assert program.nome      != 'NOME', "ERRORE: Indica il tuo NOME in program.py"
        assert program.cognome   != 'COGNOME', "ERRORE: Indica il tuo COGNOME in program.py"
        assert program.matricola != 'MATRICOLA', "ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py"
    return 0

###############################################################################


# ----------------------------------- EX.1 ----------------------------------- #

def do_ex1_tests(dbfile, k, expected):
    res = program.ex1(dbfile, k)
    testlib.check(type(res), type(expected), None, f"Wrong return type! Returned={type(res)}, expected={type(expected)}")

    if res != expected:
        print(f'''{'*'*50}\n[ERROR] The k highest index should be {expected} instead of {res}.\n'''
              f'''[ERROR] I k indici piu alti dovrebbero essere  {expected} invece che {res}.\n{'*'*50}''')
        return 0
    return 2


def test_ex1_1():
    dbfile = 'ex1/ex1_1.txt'
    k = 2
    expected = [3, 6]
    return do_ex1_tests(dbfile, k, expected)

def test_ex1_2():
    dbfile = 'ex1/ex1_2.txt'
    k = 6
    expected = [317, 290, 292, 371, 476, 294]
    return do_ex1_tests(dbfile, k, expected)

def test_ex1_3():
    dbfile = 'ex1/ex1_3.txt'
    k = 1
    expected = [473]
    return do_ex1_tests(dbfile, k, expected)


# ----------------------------------- EX.2 ----------------------------------- #
def do_test_ex2(ID, points, colors, H, W, scores=(2, 1)):
    p = 0
    img_out = f'ex2_your_result_img_{ID}.png'
    img_exp = f'ex2/ex2_{ID}_expected.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run
    res = program.ex2(H, W, points, colors, img_out)
    e = ''
    try:
        testlib.check_img_file(img_out, img_exp)
    except Exception as exc:
        e = exc
    if e:
        print(f'''{'*'*50}\n[ERROR]\n{e}''')
    else:
        p += scores[0]

    if points:
        print(f'''{'*'*50}\n[ERROR] You did not remove all elements of points. Points still contains {points} .\n[ERROR] Non hai rimosso in maniera distruttiva gli elementi di points. Points contiene sempre {points}.\n{'*'*50}''')
    else:
        p += scores[1]
    return p

def test_ex2_1():
    '''ex2/ex2_1_expected.png'''
    ID = 1 
    H = 120
    W = 160
    pts = [[17.0, 48.0], [34.0, 94.0], [6.0, 95.0]]
    colors = [[117, 85, 80], [79, 83, 68], [67, 143, 134]]
    return do_test_ex2(ID, pts, colors, H, W, scores=(2, 0.5))

def test_ex2_2():
    '''ex2/ex2_1_expected.png'''
    ID = 2 
    H = 91
    W = 81
    pts= [[16.997343666984893, 16.94356353511059], [76.49416358869863, 67.29912234948517], [39.72716349802293, 20.694731145572415], [20.60287502340183, 5.280653589472681], [35.18774667020778, 28.373425261463336], [56.403822594052215, 34.37541737561576], [14.54789788233042, 2.245764283611142], [5.447220148523135, 61.82474238836962], [36.74944440903967, 48.82870821089372], [72.63037473626771, 90.1208442131001], [17.568655736276387, 60.340116482109174], [21.329112515709202, 1.87924095138131], [61.42867096072746, 29.121560724844574], [31.060575427923734, 53.53685733337812], [67.31492487413142, 57.237347766794535], [70.68470309123902, 24.892325168222854], [64.64179354691765, 16.89287093184165], [77.17612421472751, 62.56143315129119], [17.456121846198233, 86.2107237344921], [59.199320348382784, 23.10868947614735], [17.27827016676604, 47.156264967690355], [2.0786801624170574, 18.879776865140954], [34.399522968872006, 34.049468210414524], [37.549609373549664, 25.264212272820604], [47.529532063111674, 78.61086013901406], [9.52008033292468, 47.08149875102439], [10.697516613957418, 65.23423098852602], [32.080835927390794, 51.453339379124316], [14.845666733340368, 13.181146100247329], [39.53255873256532, 32.36075914434596]]
    colors= [[68, 95, 137], [115, 120, 103], [98, 144, 109], [130, 76, 85], [108, 99, 123], [94, 63, 120], [88, 89, 58], [63, 57, 130], [72, 129, 139], [58, 149, 56], [131, 121, 134], [139, 116, 110], [66, 106, 73], [74, 54, 99], [137, 80, 104], [75, 70, 147], [107, 73, 77], [79, 83, 103], [101, 136, 57], [59, 104, 50], [133, 86, 131], [70, 53, 92], [115, 70, 86], [118, 130, 97], [60, 144, 141], [93, 113, 81], [70, 120, 59], [110, 141, 85], [133, 126, 68], [124, 148, 147]]
    return do_test_ex2(ID, pts, colors, H, W, scores=(2, 0.5))


def test_ex2_3():
    '''ex2/img_3.png'''
    ID = 3 # ex2/img_3.png
    H = 161
    W = 161
    pts= [[124.06350050894697, 23.658409909460385], [12.803055296467676, 14.426088512415467], [108.19969698398023, 39.50412078630801], [67.70685413549585, 89.73637540315062], [138.5487389864358, 117.05412629652385], [43.52279274343306, 21.168730685871544], [8.915265587812868, 48.55738015143174], [42.201022027588195, 73.43863125487722], [110.00829502317656, 111.99569674785602], [45.64653429972883, 61.1682398999194], [29.16530483964139, 126.95582748134952], [9.152540305751689, 112.21655591772296], [125.36995874651764, 125.16261745764926], [41.767032859602146, 60.18391520714239], [94.60354126661863, 43.92432629033919], [59.70730067408008, 31.725739109887982], [74.0367972847172, 7.182580501912367], [128.7671374158695, 12.38998796484787], [83.53245896187569, 49.396426026776574], [92.98441476185145, 154.46876787418145], [103.93680935741662, 5.693352156634038], [69.29479276079786, 82.11271322323829], [86.32457664725577, 109.7041942072179], [44.692971734814336, 20.74655104007755], [63.22078392408219, 153.98132137014775], [30.128073571886002, 145.54141674344615], [87.55275796244955, 73.5627388849683], [142.0086670470122, 73.83523784474232], [116.59098949445847, 64.24307679419942], [145.5511472570542, 111.0940282507876], [112.63915073433319, 52.76298465069614], [121.84136148063916, 102.40582992698975], [38.64326401413324, 25.846750420126284], [128.2190273972904, 154.42582308867082], [73.76035118886689, 95.14845061711327], [138.0933457151623, 73.61297598997099], [153.25179077007053, 92.69593708922446], [132.14350643291172, 146.32383866445088], [131.2993348217396, 25.665728615281907], [101.25264868893376, 64.14791563776801], [10.096785275758657, 68.26919255426455], [41.64813476919464, 136.69516765699024], [5.362044874018087, 154.39621822001925], [57.21438460398067, 57.42980935480941], [2.62888893207697, 29.822404363025615], [64.602779629381, 149.61591818573694], [16.038003765624683, 152.1935468901318], [139.9876534180078, 73.12014590211584], [52.59884196468987, 37.47180481392815], [98.92881774277677, 5.325009227556405], [2.512576375939343, 69.03611132221629], [10.959925909929954, 40.56249910762096], [35.6069073707195, 40.76378218937916], [21.099892225656497, 1.9378318865223374], [18.592971839338443, 99.5753217815524], [156.8552502637061, 159.4455452513039], [65.85770935506291, 26.235662593503466], [102.84064293601122, 78.93916079434668], [159.29497414279348, 10.513977351436612], [126.10074456852391, 46.43215807037052], [38.86839783232841, 106.66323601676083], [39.61617278354528, 107.20331792702922], [83.28667126956849, 68.27832713817173], [89.30473719448845, 46.21529470706039], [113.7585277099496, 66.79195596270381], [58.04783523822865, 133.41376324347377], [148.91967282446393, 7.407177052854805], [37.45294584559225, 56.11161848830268], [131.20960317860983, 158.6641198505709], [156.00444445192664, 145.6966836335382], [47.74555867530881, 159.71381018973034], [40.156626610088644, 17.050890936039384], [153.10337037991846, 37.5806611303635], [111.05269067751783, 9.395373795874775], [117.64416495952366, 141.9569541857482], [43.86234017001996, 61.028160268465996], [60.26168551466749, 120.55490946396144], [38.28696604878525, 27.668348946670523], [72.33595543872583, 49.01941358774844], [135.10944868364302, 38.27643398851784], [80.8847026557711, 151.7559595513668], [102.07362933689038, 139.63359427945684], [151.37375998611753, 120.87314276370266], [112.63158469618497, 155.84245622328055], [160.09852713327638, 72.7432909098313], [11.410034287657547, 47.13983906192354], [24.529107615724605, 67.2153063421579], [21.13758188419422, 97.262966447362], [61.63209752441451, 144.1571273704018], [155.8149421595588, 88.04846916877696], [44.24659474868305, 95.34909742065572], [144.37854647413, 65.48406867955548], [88.88460254740731, 43.736095584589485], [73.32650806145435, 64.67587919611537], [39.99456787835833, 81.44448779587465], [49.97131298274964, 60.05861308480034], [84.52024120293655, 120.84579869156698], [53.69470199239533, 148.78956142594294], [138.83328604058028, 7.839137652060095], [40.83644640534847, 71.82781753813151]]
    colors = [[84, 100, 70], [93, 50, 116], [147, 62, 65], [83, 73, 62], [55, 88, 51], [60, 56, 56], [88, 125, 135], [100, 101, 52], [126, 79, 59], [122, 55, 103], [115, 93, 129], [112, 126, 97], [126, 71, 68], [139, 63, 144], [142, 135, 56], [98, 90, 76], [80, 55, 65], [113, 87, 109], [145, 146, 130], [82, 112, 60], [62, 143, 114], [79, 140, 72], [69, 55, 86], [133, 55, 142], [126, 76, 133], [62, 57, 102], [130, 79, 50], [137, 129, 124], [53, 111, 117], [66, 123, 134], [106, 112, 106], [98, 67, 107], [59, 112, 129], [128, 83, 54], [66, 121, 112], [73, 141, 57], [72, 148, 80], [130, 77, 97], [61, 137, 128], [80, 140, 84], [104, 131, 85], [121, 109, 87], [118, 103, 63], [69, 58, 146], [131, 119, 51], [79, 55, 130], [90, 72, 80], [69, 54, 70], [124, 117, 136], [110, 143, 91], [90, 110, 131], [101, 90, 109], [144, 79, 147], [144, 87, 138], [66, 149, 89], [79, 115, 73], [122, 50, 137], [87, 113, 76], [139, 139, 56], [138, 129, 91], [67, 130, 93], [119, 69, 72], [61, 61, 83], [57, 76, 98], [121, 104, 146], [132, 137, 71], [52, 58, 60], [55, 88, 88], [115, 109, 86], [55, 55, 88], [85, 138, 99], [129, 134, 59], [54, 99, 74], [144, 52, 133], [53, 127, 61], [63, 131, 76], [120, 97, 148], [71, 70, 92], [107, 67, 139], [135, 105, 118], [148, 61, 148], [147, 69, 61], [147, 75, 147], [145, 95, 56], [139, 138, 88], [101, 66, 73], [140, 53, 140], [96, 79, 52], [55, 121, 65], [128, 85, 102], [57, 101, 101], [79, 105, 61], [117, 127, 105], [138, 118, 136], [107, 143, 61], [128, 132, 139], [53, 87, 57], [79, 128, 61], [123, 61, 66], [110, 113, 109]]
    return do_test_ex2(ID, pts, colors, H, W)



# ----------------------------------- EX.3 ----------------------------------- #


def do_ex3_tests(root, ID, score=3, total=3):
    IDS = {1: (256, 512, 'expected_img_01.png', 'ex3_your_result_img_01.png'),
           2: (256, 1024, 'expected_img_02.png', 'ex3_your_result_img_02.png'),
           3: (256, 1024, 'expected_img_03.png', 'ex3_your_result_img_03.png'),
           4: (256, 512, 'expected_img_04.png', 'ex3_your_result_img_04.png'),
           }
    *HW, expected_path, saved_image = IDS[ID]
    # remove the previouse image each time if it is there
    if os.path.exists(saved_image):
        os.remove(saved_image)

    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex3(root, saved_image)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / "
                            "Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex3(root, saved_image)
    if res != tuple(HW):
        error_message(res, tuple(HW), 'Altezza o Larghezza non sono corrette\n')
        return 0
    testlib.check_img_file(saved_image, expected_path)
    return score


def test_ex3_1():
    r'''
            catRL
            /   \
           o     i
    '''
    lista_z = ['catRL',
               ['image_o.png', None, None],
               ['image_i.png', None, None]
               ]
    return do_ex3_tests(BinTree.fromList(lista_z), ID=1)


def test_ex3_2():
    r'''
               catLR
              /     \
            catRL    o
           /    \
        catRL    ᴐ
        /   \      
       a     i     
    '''

    lista_a = ['catLR',
               ['catRL',
                ['catRL',
                 ['image_a.png', None, None],
                 ['image_i.png', None, None]],
                ['image_c.png', None, None]],
               ['image_o.png', None, None]]
    return do_ex3_tests(BinTree.fromList(lista_a), ID=2)


def test_ex3_3():
    r'''
               catLR
              /     \
            catRL    o
           /    \
        catRL  flip_v
        /   \       \
       a     i       ᴐ
    '''
    lista_b = ['catLR',
               ['catRL',
                ['catRL',
                 ['image_a.png', None, None],
                 ['image_i.png', None, None]],
                ['flip_v', None, ['image_c.png', None, None]]],
               ['image_o.png', None, None]]
    return do_ex3_tests(BinTree.fromList(lista_b), ID=3)

def test_ex3_4():
    r'''
               catLR
              /      \    
            flip_v   flip_v   
           /            \
         flip_v          flip_v
        /                  \
       ᴐ                    flip_v
                             /
                            a
       '''

    lista_d = ['catLR',
               ['flip_v',
                ['flip_v', ['image_c.png', None, None] , None],
                None,
                ],
               ['flip_v',
                None,
                ['flip_v', None, ['flip_v',
                                  ['image_a.png', None, None], None]
                 ],
                ]
               ]
    return do_ex3_tests(BinTree.fromList(lista_d), ID=4, score=1, total=1)


def do_ex4_test(syllables, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex4(syllables)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex4(syllables)
    if not isinstance(res, (list, set)):
        testlib.check(type(res), set, None, f"Wrong return type! Returned={type(res)}, expected=list or set")
    p=0
    if type(res) == list:
        testlib.check(res, expected, None, f"Wrong list! Returned={res}, expected={expected}")
        print("Correct list returned", end=' ')
        p=2
    elif type(res) == set:
        testlib.check(res, set(expected), None, f"Wrong set! Returned={res}, expected={expected}")
        print("Correct set returned", end=' ')
        p=1.5
    return p

def test_ex4_1():
    '''
    syllables = ['bos', 'co', 'sa']
    '''

    syllables  = ['bos', 'co', 'sa']
    expected = ['boscosa', 'bossaco', 'cobossa', 'cosabos', 'sabosco', 'sacobos',
     'bosco', 'bossa', 'cobos', 'sabos', 'cosa', 'saco']
    return do_ex4_test(syllables, expected)

def test_ex4_2():
    '''
    syllables = ['sol','e','a']
    '''

    syllables  = ['sol','e','a']
    expected = ['aesol', 'asole', 'easol', 'esola', 'solae', 'solea', 'asol', 'esol', 'sola', 'sole', 'ae', 'ea']
    return do_ex4_test(syllables, expected)

def test_ex4_3():
    '''
    syllables = ['bar','for','go','y']
    '''

    syllables  = ['bar','for','go','y']
    expected = ['barforgoy', 'barforygo', 'bargofory', 'bargoyfor', 'baryforgo', 'barygofor', 'forbargoy', 'forbarygo', 'forgobary', 'forgoybar', 'forybargo', 'forygobar', 'gobarfory', 'gobaryfor', 'goforbary', 'goforybar', 'goybarfor', 'goyforbar', 'ybarforgo', 'ybargofor', 'yforbargo', 'yforgobar', 'ygobarfor', 'ygoforbar', 'barforgo', 'bargofor', 'forbargo', 'forgobar', 'gobarfor', 'goforbar', 'barfory', 'baryfor', 'forbary', 'forybar', 'ybarfor', 'yforbar', 'barfor', 'bargoy', 'barygo', 'forbar', 'forgoy', 'forygo', 'gobary', 'gofory', 'goybar', 'goyfor', 'ybargo', 'yforgo', 'ygobar', 'ygofor', 'bargo', 'forgo', 'gobar', 'gofor', 'bary', 'fory', 'ybar', 'yfor', 'goy', 'ygo']
    return do_ex4_test(syllables, expected)

def test_ex4_4():
    '''
    syllables = ['co','ca','la','pe','psi']
    '''

    syllables  = ['co','ca','la','pe','psi']
    expected = ['cacolapepsi', 'cacolapsipe', 'cacopelapsi', 'cacopepsila', 'cacopsilape', 'cacopsipela', 'calacopepsi', 'calacopsipe', 'calapecopsi', 'calapepsico', 'calapsicope', 'calapsipeco', 'capecolapsi', 'capecopsila', 'capelacopsi', 'capelapsico', 'capepsicola', 'capepsilaco', 'capsicolape', 'capsicopela', 'capsilacope', 'capsilapeco', 'capsipecola', 'capsipelaco', 'cocalapepsi', 'cocalapsipe', 'cocapelapsi', 'cocapepsila', 'cocapsilape', 'cocapsipela', 'colacapepsi', 'colacapsipe', 'colapecapsi', 'colapepsica', 'colapsicape', 'colapsipeca', 'copecalapsi', 'copecapsila', 'copelacapsi', 'copelapsica', 'copepsicala', 'copepsilaca', 'copsicalape', 'copsicapela', 'copsilacape', 'copsilapeca', 'copsipecala', 'copsipelaca', 'lacacopepsi', 'lacacopsipe', 'lacapecopsi', 'lacapepsico', 'lacapsicope', 'lacapsipeco', 'lacocapepsi', 'lacocapsipe', 'lacopecapsi', 'lacopepsica', 'lacopsicape', 'lacopsipeca', 'lapecacopsi', 'lapecapsico', 'lapecocapsi', 'lapecopsica', 'lapepsicaco', 'lapepsicoca', 'lapsicacope', 'lapsicapeco', 'lapsicocape', 'lapsicopeca', 'lapsipecaco', 'lapsipecoca', 'pecacolapsi', 'pecacopsila', 'pecalacopsi', 'pecalapsico', 'pecapsicola', 'pecapsilaco', 'pecocalapsi', 'pecocapsila', 'pecolacapsi', 'pecolapsica', 'pecopsicala', 'pecopsilaca', 'pelacacopsi', 'pelacapsico', 'pelacocapsi', 'pelacopsica', 'pelapsicaco', 'pelapsicoca', 'pepsicacola', 'pepsicalaco', 'pepsicocala', 'pepsicolaca', 'pepsilacaco', 'pepsilacoca', 'psicacolape', 'psicacopela', 'psicalacope', 'psicalapeco', 'psicapecola', 'psicapelaco', 'psicocalape', 'psicocapela', 'psicolacape', 'psicolapeca', 'psicopecala', 'psicopelaca', 'psilacacope', 'psilacapeco', 'psilacocape', 'psilacopeca', 'psilapecaco', 'psilapecoca', 'psipecacola', 'psipecalaco', 'psipecocala', 'psipecolaca', 'psipelacaco', 'psipelacoca', 'cacolapsi', 'cacopepsi', 'cacopsila', 'cacopsipe', 'calacopsi', 'calapepsi', 'calapsico', 'calapsipe', 'capecopsi', 'capelapsi', 'capepsico', 'capepsila', 'capsicola', 'capsicope', 'capsilaco', 'capsilape', 'capsipeco', 'capsipela', 'cocalapsi', 'cocapepsi', 'cocapsila', 'cocapsipe', 'colacapsi', 'colapepsi', 'colapsica', 'colapsipe', 'copecapsi', 'copelapsi', 'copepsica', 'copepsila', 'copsicala', 'copsicape', 'copsilaca', 'copsilape', 'copsipeca', 'copsipela', 'lacacopsi', 'lacapepsi', 'lacapsico', 'lacapsipe', 'lacocapsi', 'lacopepsi', 'lacopsica', 'lacopsipe', 'lapecapsi', 'lapecopsi', 'lapepsica', 'lapepsico', 'lapsicaco', 'lapsicape', 'lapsicoca', 'lapsicope', 'lapsipeca', 'lapsipeco', 'pecacopsi', 'pecalapsi', 'pecapsico', 'pecapsila', 'pecocapsi', 'pecolapsi', 'pecopsica', 'pecopsila', 'pelacapsi', 'pelacopsi', 'pelapsica', 'pelapsico', 'pepsicaco', 'pepsicala', 'pepsicoca', 'pepsicola', 'pepsilaca', 'pepsilaco', 'psicacola', 'psicacope', 'psicalaco', 'psicalape', 'psicapeco', 'psicapela', 'psicocala', 'psicocape', 'psicolaca', 'psicolape', 'psicopeca', 'psicopela', 'psilacaco', 'psilacape', 'psilacoca', 'psilacope', 'psilapeca', 'psilapeco', 'psipecaco', 'psipecala', 'psipecoca', 'psipecola', 'psipelaca', 'psipelaco', 'cacolape', 'cacopela', 'calacope', 'calapeco', 'capecola', 'capelaco', 'cocalape', 'cocapela', 'colacape', 'colapeca', 'copecala', 'copelaca', 'lacacope', 'lacapeco', 'lacocape', 'lacopeca', 'lapecaco', 'lapecoca', 'pecacola', 'pecalaco', 'pecocala', 'pecolaca', 'pelacaco', 'pelacoca', 'cacopsi', 'calapsi', 'capepsi', 'capsico', 'capsila', 'capsipe', 'cocapsi', 'colapsi', 'copepsi', 'copsica', 'copsila', 'copsipe', 'lacapsi', 'lacopsi', 'lapepsi', 'lapsica', 'lapsico', 'lapsipe', 'pecapsi', 'pecopsi', 'pelapsi', 'pepsica', 'pepsico', 'pepsila', 'psicaco', 'psicala', 'psicape', 'psicoca', 'psicola', 'psicope', 'psilaca', 'psilaco', 'psilape', 'psipeca', 'psipeco', 'psipela', 'cacola', 'cacope', 'calaco', 'calape', 'capeco', 'capela', 'cocala', 'cocape', 'colaca', 'colape', 'copeca', 'copela', 'lacaco', 'lacape', 'lacoca', 'lacope', 'lapeca', 'lapeco', 'pecaco', 'pecala', 'pecoca', 'pecola', 'pelaca', 'pelaco', 'capsi', 'copsi', 'lapsi', 'pepsi', 'psica', 'psico', 'psila', 'psipe', 'caco', 'cala', 'cape', 'coca', 'cola', 'cope', 'laca', 'laco', 'lape', 'peca', 'peco', 'pela']
    return do_ex4_test(syllables, expected)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    #test_ex1_1,  test_ex1_2, test_ex1_3,              # k nearest
    #test_ex2_1, test_ex2_2, test_ex2_3,               # 1-NN
    #test_ex3_1, test_ex3_2, test_ex3_3, test_ex3_4,   # albero con op immagini
    test_ex4_1, test_ex4_2, test_ex4_3, test_ex4_4,   # combinazioni sillabe
    test_personal_data_entry,
]


if __name__ == '__main__':
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
################################################################################
