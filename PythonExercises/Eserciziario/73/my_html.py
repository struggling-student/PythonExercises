
import html

class HTMLNode(object):
    def __eq__(self, other):
        return  isinstance(other, type(self))  and \
                self.tag     == other.tag    and \
                self.attr    == other.attr   and \
                self.closed  == other.closed and \
                self.content == other.content

    @classmethod
    def fromList(cls, lista):
        tag, attr, content, closed = lista
        if isinstance(content, list):
            content = [cls.fromList(sublist) for sublist in content]
        return cls(tag, attr, content, closed)

    def __init__(self,tag,attr,content,closed=True):
        self.tag = tag
        # dizionario degli attributi
        self.attr = attr
        # testo per nodi _text_ o lista dei figli
        self.content = content  
        # True se il nodo ha la chiusura
        self.closed = closed    
    
    # per distinguere i nodi testo
    def istext(self):           
        return self.tag == '_text_'
    
    def open_tag(self):
        '''Ritorna la stringa del tag di inizio.'''
        if self.istext():
            return self.tag
        s = '<'+self.tag
        for k in sorted(self.attr):
            v = self.attr[k]
            if v is not None:   # filtro gli attributi senza valore
                # usiamo escape per i valori 
                s += ' {}="{}"'.format(k, html.escape(v,True))
        s += '>' if self.closed else '/>'
        return s
    
    def close_tag(self):
        '''Ritorna la stringa del tag di fine.'''
        return '</'+self.tag+'>'
    
    def to_string(self):
        '''Ritorna la stringa del documento HTML che
        corrisponde all'albero di questo nodo.'''
        if self.istext():
            # usiamo escape per i caratteri speciali
            return html.escape(self.content,False)
        s = self.open_tag()
        doc = self.open_tag()
        if self.closed:
            for child in self.content:
                doc += child.to_string()
            doc += self.close_tag()
        return doc
                
    def __str__(self):
        '''Ritorna una rappresentazione semplice
        del nodo'''
        if self.istext(): return self.tag
        else: return '<{}>'.format(self.tag)

import html.parser

class _MyHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        '''Crea un parser per la class HTMLNode'''
        # inizializza la class base super()
        super().__init__()
        self.root = None
        self.stack = []
    def handle_starttag(self, tag, attrs):
        '''Metodo invocato per tag aperti'''
        closed = tag not in ['img','br','meta','link', 'input', 'wbr', 'hr']
        node = HTMLNode(tag,dict(attrs),[],closed)
        if not self.root:
            self.root = node
        if self.stack: 
            self.stack[-1].content.append(node)
        if closed:
            self.stack.append(node)
    def handle_endtag(self, tag):
        '''Metodo invocato per tag chiusi'''
        if self.stack and self.stack[-1].tag == tag:
            self.stack[-1].opentag = False
            self.stack = self.stack[:-1]
    def handle_data(self, data):
        '''Metodo invocato per il testo'''
        if not self.stack: return
        self.stack[-1].content.append(
            HTMLNode('_text_',{},data))
    def handle_comment(self, data):
        '''Metodo invocato per commenti HTML'''
        pass
    def handle_entityref(self, name):
        '''Metodo invocato per caratteri speciali'''
        if name in name2codepoint:
            c = unichr(name2codepoint[name])
        else:
            c = '&'+name
        if not self.stack: return
        self.stack[-1].content.append(
            HTMLNode('_text_',{},c))
    def handle_charref(self, name):
        '''Metodo invocato per caratteri speciali'''
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        if not self.stack: return
        self.stack[-1].content.append(
            HTMLNode('_text_',{},c))
    def handle_decl(self, data):
        '''Metodo invocato per le direttive HTML'''
        pass

def parse(html):
    '''Esegue il parsing HTML del testo html e
    ritorna la radice dell'albero.'''
    parser = _MyHTMLParser()
    parser.feed(html)
    return parser.root

def fparse(fhtml):
    '''Esegue il parsing HTML del file fhtml e
    ritorna la radice dell'albero .'''
    with open(fhtml, encoding='utf8') as f:
        root = parse(f.read())
        return root

