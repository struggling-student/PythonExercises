import argparse, csv, glob, time, pprint, json
#from grade import my_print as print
# import deepdiff
import glob
import hashlib
import os

msg_ok  = '[OK]: \t  {points} point(s)\t {duration:.3f} ms\n'
msg_0points  = 'error: {points} points\t {duration:.3f} ms\n'
msg_err = 'error: {exname}\n\t{exmsg}\n'

COL = {'RED': '\u001b[31m',
       'RST': '\u001b[0m',
       'GREEN': '\u001b[32m',
       'YELLOW' : '\u001b[33m',
       'BOLD' : '\033[1m',
       'ENDC' : '\033[0m'}

def my_decorator(func):
    def wrapped_func(*args, **kwargs):
        col = ''
        if any(err in args[0] for err in ['[OK]', 'Correct']):
            col = COL['BOLD']+COL['GREEN']
        if any(err in args[0] for err in ['error', 'Error', 'ERROR',]):
            col = COL['BOLD']+COL['RED']
        if col:
            return func(f'{col}', *args, f'{COL["RST"]}{COL["ENDC"]}', **kwargs, )
        else:
            return func(*args, **kwargs, )
    return wrapped_func
my_print = my_decorator(print)

class NotImplemented(Exception):
    pass

def check_expected():
    files = glob.glob('backup/**', recursive=True)
    delim = "\\" if os.name == 'nt' else '/'
    # print(*files, sep='\n')
    for file_b in files:
        if os.path.isfile(file_b):
            file_e = '/'.join(file_b.split(delim)[1:])
            with open(file_b, mode='rb') as frb, open(file_e, mode='rb') as fre:
                assert hashlib.md5(frb.read()).hexdigest() == hashlib.md5(fre.read()).hexdigest(),\
                    (f"{COL['BOLD']} {COL['RED']}\nWARNING: an expected or input file has been overwritten by mistake!\n"
                     f"expected/input file: {file_e}\ndiffers from:        {file_b}\nWe cannot evaluate your exam,"
                     f"please call the lecturer to fix the issue!{COL['RST']}{COL['ENDC']}")



def run(tests, verbose, logfile=''):
    results = []
    for test in tests:
        results.append(runOne(test, verbose, logfile))
    return results


def runOne(test, verbose, logfile='', stack_trace=False):
    try:
        #test(run=False) # to build doc string
        #doc=test.__doc__ or ''
        #print(f'Running {test.__name__}\t{doc}')
        print(f'Running {test.__name__}')
        start = time.time()
        v = test()
        end = time.time()
        if v:
            print(msg_ok.format(
                            points=v,
                            duration=(end-start)*1000))
        else:
            print(msg_0points.format(
                            points=v,
                            duration=(end-start)*1000))
    except NotImplemented:
        print("Not implemented: (None returned) ", test.__name__)
        v = 0
    except Exception as e:
        import traceback
        print(msg_err.format(
                             exname=e.__class__.__name__,
                             exmsg=str(e) if str(e) else ''))
        if stack_trace:
            print('*'*50+'[BEGIN STACK TRACE]'+'*'*50)
            traceback.print_exc()
            print('*'*50+'[END STACK TRACE]'+'*'*50)
        v = 0
    result = test.__name__, v
    log([result], logfile)
    return result


def description(tests):
    for test in tests:
        print(test.__name__ + ': ' + test.__help__)


def emptyLog(logfile):
    if logfile:
        with open(logfile,'w',newline='',encoding='utf8') as f:
            f.truncate()


def log(results, logfile):
    if logfile:
        with open(logfile, 'a', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerows(results)


def check_list(res, expected, params=None, expl=''):
    if res != expected:
        if isinstance(res, list):
            diff = len(res)-len(expected)
            if diff != 0:
                print(f'''{'*'*50}\n[ERROR]La lista ritornata non è della lunghezza giusta!/ The returned list has an incorrect length! len(returned)={len(res)}, len(expected)={len(expected)}''')
            print('Here the two lists')
            if diff>=0:
                expected = expected + [""]*diff
                zz = zip(res, expected)
                print('{:<30}   {:>30}'.format('RETURNED', 'EXPECTED'))
            else:
                res = res+[""]*(-diff)
                zz = zip(expected, res)
                print('{:<30}   {:>30}'.format('EXPECTED', 'RETURNED'))
            for i, j in zz:
                if i!=j:
                    print(f'\b[ERROR]{i:<30}   {j:>30}')
                else:
                    print(f'{i:<30}   {j:>30}')
        else:
            print(f'''{'*'*50}\n[ERROR]Il valore ritornato non è una lista! / The returned value is not a list!''')
    assert res==expected, '''Il risultato ritornato non è corretto / Incorrect value returned!'''

checkList = check_list

def check_dict(res, expected, params=None, expl=''):
    if res != expected:
        if isinstance(res, dict):
            print(f'''{'*'*50}\n[ERROR] Il dizionario ritornato è sbagliato! / The returned dictionary is incorrect!\nReturned={res}\nexpected={expected}\n{'*'*50}''')
            for k in expected:
                if k not in res:
                    print(f'''\b[ERROR] Manca la chiave {k!r} con valore {expected[k]!r}!''')
                    print(f'''\b[ERROR] Key {k!r} with value {expected[k]!r} is missing!''')
                elif expected[k] != res[k]:
                        print(f'''\b[ERROR] La chiave {k!r} dovrebbe avere il valore {expected[k]!r} invece che {res[k]!r}''')
                        print(f'''\b[ERROR] Key {k!r} should have the value {expected[k]!r} instead of {res[k]!r}''')
            diff = set(res.keys()) - set(expected.keys())
            if diff:
                for extra_key in diff:
                    print(f'''\b[ERROR] La chiave {extra_key!r} è di troppo.''')
                    print(f'''\b[ERROR] La key {extra_key!r} is unexpected.''')
        else:
            print(f'''{'*'*50}\n[ERROR] Il valore ritornato non è un dizionario! / The returned value is not a dictionary!\nReturned={type(res)!r}\nexpected={type(expected)!r}.{'*'*50}''')
    assert res==expected, '''Il risultato ritornato non è corretto / Incorrect value returned!'''

checkDict = check_dict

def check_val(res, expected, expl=''):
    if not expl:
        expl = f'''{'*'*50}\n[ERROR] Il valore ritornato è sbagliato! / The returned value is incorrect!\nReturned={res}\nexpected={expected}\n{'*'*50}'''
    assert res == expected, expl

def check10(a, b, params=None, expl=''):
    msg = ''
    if params:
        msg += '\twhen input={}'.format(params)
    msg += '\n\t\t%r != %r' % (a, b)
    if expl:
        msg += "\t<- correct %s value" % expl
    assert a == b,  msg


def check(a, b, params=None, expl='', other=None):
    msg = ''
    if params:
        msg += 'when input={}'.format(params)
    if other:
        msg += '\n\t\t%r != %r ' % (other[0], other[1])
    else:
        msg += '\n\t%r != %r\n' % (a, b)
    if expl:
        msg += "%s\n" % expl
    if (a == None) | (a == type(None)):
        raise NotImplemented()
    # if a != b:
    #     pprint.pprint(deepdiff.DeepDiff(a, b))
    assert a == b,  msg


def check1(a, b, params=None, expl='', other=None):
    msg = ''
    if params:
        msg += 'when input={}'.format(params)
    if other:
        msg += '\n\t\t%r != %r ' % (other[0], other[1])
    else:
        msg += '\n\t%r \n\t!= \n\t%r\n\n' % (a, b)
    if expl:
        msg += "\t<-  %s\n\n\n" % expl
    if a == None:
        raise NotImplemented()
    assert a == b,  msg


def check_text_file(a,b):
    with open(a, 'r', encoding='utf8') as f: txt_a = f.read()
    with open(b, 'r', encoding='utf8') as f: txt_b = f.read()
    lines_a = [l.strip() for l in txt_a.splitlines()]
    lines_b = [l.strip() for l in txt_b.splitlines()]
    assert lines_a == lines_b, 'text differ: ' + a + ' ' + b


def check_json_file(a,b, params=None, expl='', other=''):
    with open(a, 'r', encoding='utf8') as f: da = json.load(f)
    with open(b,' r', encoding='utf8') as f: db = json.load(f)
    check(da, db, params, expl, other)


def image_load(filename):
    '''Load the PNG image from the PNG file under 'filename',
       convert it into tuple-matrix format and return it'''
    import png
    with open(filename, 'rb') as f:
        # Read the image as an RGB-file with 256 colours (without transparency)
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        # Convert the list of lists into tuples. Notice that the PNG colours
        # are triples in the png_img array, so we read them by a step of three.
        w *= 3
        return [[(line[i], line[i + 1], line[i + 2])
                 for i in range(0, w, 3)]
                for line in png_img]
    # return img


def check_img_file(a, b):
    img_a = image_load(a)
    img_b = image_load(b)
    ha = len(img_a)
    hb = len(img_b)
    assert ha == hb, 'Images have different heights: {} != {}'.format(ha, hb)
    assert ha > 0 and hb > 0, 'An image has a height of 0: {} {}'.format(ha, hb)
    wa = len(img_a[0])
    wb = len(img_b[0])
    assert wa == wb, 'Images have different widths: {} != {}'.format(wa, wb)
    assert wa > 0 and wb > 0, 'An image has a height of 0: {} {}'.format(wa, wb)
    for y in range(ha):
        for x in range(wa):
            ca = img_a[y][x]
            cb = img_b[y][x]
            assert ca == cb, \
                   'Images differ at coordinates {},{} : {} != {}'.format(
                       x, y, ca, cb)


def runtests(tests, verbose=True, logfile='', stack_trace=False):
    if logfile:
        emptyLog(logfile)
        for test in tests:
            runOne(test, verbose, logfile, stack_trace)
        with open(logfile, newline='', encoding='utf8') as f:
            tot = 0
            reader = csv.reader(f)
            for row in reader:
                tot += float(row[1])
        print('Total score:', tot)
    else:
        for test in tests:
            runOne(test, verbose, logfile, stack_trace)


import tempfile, os, os.path


class randomized_filename:

    def __init__(self, filename):
        name, ext = filename.split('.')
        self.filename = filename
        self.randomized = next(tempfile._get_candidate_names()) + '.' + ext

    def __enter__(self):
        if os.path.isfile(self.filename):
            print(self.filename, ' -> ', self.randomized)
            os.rename(self.filename, self.randomized)
        return self.randomized

    def __exit__(self, type, value, traceback):
        if os.path.isfile(self.randomized):
            print(self.filename, ' <- ', self.randomized)
            os.rename(self.randomized, self.filename)

def check_exam_constraints():
    grades = {}
    total  = 0
    with open('grade.csv') as F:
        for line in F:
            test, points = line.split(',')
            _, name, *_ = test.split('_')
            #if name == 'personal': continue
            total += float(points)
            grades[name] = grades.get(name, 0) + float(points)
    #%% Constraint for the exam
    constraint1 = len([name for name,grade in grades.items() if grade>0 and name.startswith('func')]) >= 3
    constraint2 = len([name for name,grade in grades.items() if grade>0 and name.startswith('ex')]) >= 1
    constraint3 = total >= 18
    constraint4 = 'personal' in grades and grades['personal'] >= 0
    constraint5 = all((constraint1, constraint2, constraint3, constraint4))
    if not constraint4:
        print(f'YOU HAVE NOT FILLED YOUR PERSONAL DETAILS: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    elif not constraint1:
        print(f'YOU HAVE NOT PASSED AT LEAST 3 FUNC EXERCISES: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    elif not constraint2:
        print(f'YOU HAVE NOT PASSED AT LEAST 1 RECURSIVE EXERCISE: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    elif not constraint3:
        print(f'THE FINAL GRADE IS LESS THAN 18: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    else:
        print(f"YOU HAVE {COL['GREEN']}PASSED{COL['RST']} THE EXAM WITH {COL['BOLD']+COL['GREEN']}{total}{COL['RST']} POINTS")
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    print(f"Personal info present:       {COL['BOLD']} {COL['GREEN'] if constraint4 else COL['RED']} {constraint4}{COL['RST']}{COL['ENDC']}")
    print(f"Three func problems solved:  {COL['BOLD']} {COL['GREEN'] if constraint1 else COL['RED']} {constraint1}{COL['RST']}{COL['ENDC']}")
    print(f"One ex problem solved:       {COL['BOLD']} {COL['GREEN'] if constraint2 else COL['RED']} {constraint2}{COL['RST']}{COL['ENDC']} ")
    print(f"Total >= 18:                 {COL['BOLD']} {COL['GREEN'] if constraint3 else COL['RED']} {constraint3}{COL['RST']}{COL['ENDC']}")
    print(f"Exam passed:                 {COL['BOLD']} {COL['GREEN'] if constraint5 else COL['RED']} {constraint5}{COL['RST']}{COL['ENDC']}")
