import my_html
import os


def es73(dir, htmlFile):
    li = pathToDOM(dir, dir)
    DOM = my_html.HTMLNode('ul', {}, [li])
    with open(htmlFile, mode='w', encoding='utf8') as f:
        f.write(DOM.to_string())
    return DOM


def pathToDOM(path, name):
    DOM = my_html.HTMLNode('li', {}, [
        my_html.HTMLNode('_text_', {}, name)
    ])
    if os.path.isdir(path):
        # li nomefile
        #   ul filecontenuti
        contenuti = []
        files = os.listdir(path)
        files.sort()
        for f in files:
            if f[0] == '.': continue
            fn = "{}/{}".format(path, f)
            contenuti.append(pathToDOM(fn, f))
        DOM.content.append(my_html.HTMLNode('ul', {}, contenuti))
    return DOM
