# +
# TODO: find the file in PYTHONPATH

import ast  

from contextlib import contextmanager
from testlib import my_print

@contextmanager
def import_decorated(modulename):
    "with context that decorates a module, does stuff, and then remove the decorated module"
    try:
        remove_import(modulename)
        decorated_code = decorate_file(f"{modulename}.py")
        import_from_string(modulename, decorated_code)
        yield
    except Exception as e:
        print(e)
    finally:
        remove_import(modulename)

class RecursionDetectedError(Exception):
    "Exception raised when a function calls itself"
    pass

# set DETECT=True to raise RecursionDetectedError when re-entering the same function
DETECT = True
DETECT = False

def norecurse(func):
    '''Decorator that raise a RecursionDetectedError if the function calls itself'''
    func.called = False
    def wrap(*args, **kwargs):
        if func.called and DETECT:
            my_print("[OK] Recursion detected! in " + func.__name__)
            func.called = False # if you are going to continue execution
            raise RecursionDetectedError
        func.called = True
        result = func(*args, **kwargs)
        func.called = False
        return result
    return wrap

class DecorateFunction(ast.NodeTransformer):
    "AST tree transformer that adds the decorator to all module functions"
    def __init__(self, decorator='norecurse'):
        self.decorator=decorator
    def visit_FunctionDef(self,node:ast.FunctionDef):
        node.decorator_list.append(ast.Name(id=self.decorator, ctx=ast.Load()))
        self.generic_visit(node)
        return node

def decorate_file(filename):
    "Decorate all function in filename with the norecurse decorator"
    with open(filename) as F:
        code = F.read()
    try:
        tree = ast.parse(code, type_comments=True)
    except Exception as e:
        print(f"Compile errors in file {filename!r}")
        raise
    decorated = DecorateFunction('norecurse').visit(tree)
    return 'from isrecursive2 import norecurse\n' + ast.unparse(decorated)

import importlib.util
import sys

def import_from_string(module_name, source_code):
    spec   = importlib.util.spec_from_loader(module_name, loader=None)
    module = importlib.util.module_from_spec(spec)
    exec(source_code, module.__dict__)
    sys.modules[module_name] = module  # Register the module in sys.modules
    globals()[module_name]   = module  # and as a global var
    return module

def remove_import(module_name):
    "remove the module from memory for following undecorated import"
    if module_name in sys.modules:
        del sys.modules[module_name]
    if module_name in globals():
        del globals()[module_name]

if __name__ == '__main__':
    print(decorate_file('rec.py'))

    import rec
    print('calling recursive inner function before with:',             rec.fact(4))        # run without decorator
    print('calling recursive inner function in a method before with:', rec.REC(4).rec())   # run without decorator

    try:
        with import_decorated('rec'):
            #print('calling recursive inner function inside with')
            #print(rec.fact(3))
            print('calling recursive inner function in a method, inside with:')
            rec.REC(4).rec()
    except Exception as e:
        print(e)
        pass

    # re import it without decorators
    import rec
    print('calling recursive inner function after with:',             rec.fact(5))        # run without decorator
    print('calling recursive inner function in a method after with:', rec.REC(6).rec())   # run without decorator


