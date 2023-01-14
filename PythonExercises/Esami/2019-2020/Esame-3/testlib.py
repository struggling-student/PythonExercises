import argparse, csv, glob, time, pprint, json
# import deepdiff

# msg_ok =  '{test:<30} ok -> {points} points'
msg_ok =  '{test:<30} ok\t{durata:.3f} ms\t{doc}'
msg_err = '{test:<30} {doc}\n\terror -> {exname}\n\t{exmsg}'

class NotImplemented(Exception):
    pass

def run(tests,verbose, logfile=''):
    results = []
    for test in tests:
        results.append(runOne(test,verbose,logfile))
    return results

def runOne(test, verbose, logfile=''):
    try:
        start = time.time()
        v = test()
        end = time.time()
        print(msg_ok.format(test=test.__name__,
                            points=v,
                            doc=test.__doc__ or '',
                            durata=(end-start)*1000))
    except NotImplemented:
        print("Not implemented: (None returned) ", test.__name__)
        v = 0
    except Exception as e:
        import traceback
        print(msg_err.format(test=test.__name__,
                             exname=e.__class__.__name__,
                             doc=test.__doc__ or '',
                             exmsg=str(e) if str(e) else ''))
        # SCOMMENTATE LA RIGA SEGUENTE PER VEDERE LA STACK TRACE DELL'ERRORE
        #traceback.print_exc()
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

def log(results,logfile):
    if logfile:
        with open(logfile,'a',newline='',encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerows(results)

def check10(a,b, params=None, expl=''):
    msg = ''
    if params:
        msg += '\twhen input={}'.format(params)
    msg += '\n\t\t%r != %r' % (a, b)
    if expl:
        msg += "\t<- correct %s value" % expl
    assert a == b,  msg

def check(a,b, params=None, expl='', altro=None):
    msg = ''
    if params:
        msg += 'when input={}'.format(params)
    if altro:
        msg += '\n\t\t%r != %r ' % (altro[0], altro[1])
    else:
        msg += '\n\t%r \n\t!= \n\t%r\n\n' % (a, b)
    if expl:
        msg += "\t<-  %s\n\n\n" % expl
    if (a == None) | (a == type(None)):
        raise NotImplemented()
    # if a != b:
    #     pprint.pprint(deepdiff.DeepDiff(a, b))
    assert a == b,  msg

def check1(a,b, params=None, expl='', altro=None):
    msg = ''
    if params:
        msg += 'when input={}'.format(params)
    if altro:
        msg += '\n\t\t%r != %r ' % (altro[0], altro[1])
    else:
        msg += '\n\t%r \n\t!= \n\t%r\n\n' % (a, b)
    if expl:
        msg += "\t<-  %s\n\n\n" % expl
    if a == None:
        raise NotImplemented()
    assert a == b,  msg

def check_text_file(a,b):
    with open(a,'rU', encoding='utf8') as f: txt_a = f.read()
    with open(b,'rU', encoding='utf8') as f: txt_b = f.read()
    lines_a = [l.strip() for l in txt_a.splitlines()]
    lines_b = [l.strip() for l in txt_b.splitlines()]
    assert lines_a == lines_b, 'text differ: ' + a + ' ' + b

def check_json_file(a,b, params=None, expl='', altro=''):
    with open(a,'rU', encoding='utf8') as f: da = json.load(f)
    with open(b,'rU', encoding='utf8') as f: db = json.load(f)
    check(da, db, params, expl, altro)

def image_load(filename):
    '''Carica l'immagine in formato PNG dal file
    filename, la converte nel formato a matrice
    di tuple e la ritorna'''
    import png
    with open(filename,'rb') as f:
        # legge l'immagine come RGB a 256 valori
        r = png.Reader(file=f)
        iw, ih, png_img, _ = r.asRGB8()
        # converte in lista di liste di tuple
        img = []
        for png_row in png_img:
            row = []
            # l'immagine PNG ha i colori in
            # un'unico array quindi li leggiamo
            # tre alla volta in una tupla
            for i in range(0,len(png_row),3):
                row.append( ( png_row[i+0],
                              png_row[i+1],
                              png_row[i+2] ) )
            img.append( row )
    return img

def check_img_file(a,b):
    img_a = image_load(a)
    img_b = image_load(b)
    ha = len(img_a)
    hb = len(img_b)
    assert ha == hb, 'images of different heigth: {} != {}'.format(ha, hb)
    assert ha > 0 and hb > 0, 'one of the images has 0 height : {} {}'.format(ha, hb)
    wa = len(img_a[0])
    wb = len(img_b[0])
    assert wa == wb, 'images of different width: {} != {}'.format(wa, wb)
    assert wa > 0 and wb > 0, 'one of the images has 0 width : {} {}'.format(wa, wb)
    for y in range(ha):
        for x in range(wa):
            ca = img_a[y][x]
            cb = img_b[y][x]
            assert ca == cb, 'images differ at coordinates {},{} : {} != {}'.format(x,y,ca, cb)

def runtests(tests,verbose=True,logfile=''):
    if logfile:
        emptyLog(logfile)
        for test in tests:
            runOne(test, verbose, logfile)
        with open(logfile,newline='',encoding='utf8') as f:
            tot = 0
            reader = csv.reader(f)
            for row in reader:
                tot += float(row[1])
        print('Total score:', tot)
    else:
        for test in tests:
            runOne(test, verbose, logfile)

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
    
