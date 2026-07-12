# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
import json
import images
import tree
from testlib import my_print, COL, check_expected

if not os.path.isfile('program.py'):
    print('WARNING: Save program.py as program.py\n'
          'ATTENZIONE: salvare program.py con nome program.py')
    sys.exit(0)

import program

##########################################
##########################################
##########################################
# set DEBUG = True per disattivare il test di ricorsione e mostrare la stack trace degli errori
# set DEBUG = True to deactivate the recursion test and show error stack trace

# DEBUG = True
DEBUG = False
##########################################
##########################################
##########################################

def test_personal_data_entry(run=None):
    nome      = getattr(program, 'nome',      getattr(program, 'name',       'NOME'))
    cognome   = getattr(program, 'cognome',   getattr(program, 'surname',    'COGNOME'))
    matricola = getattr(program, 'matricola', getattr(program, 'student_id', 'MATRICOLA'))
    if    nome == 'NOME' or cognome == 'COGNOME' or matricola == 'MATRICOLA': 
        raise Exception("PERSONAL DATA NOT COMPLETE")
    return 1e-9

def load_tests(func_name):
    with open(os.path.join(func_name, "tests.json"), 'r') as f:
        return json.load(f)

# --- FUNC 1 (2pt, 4 test da 0.5pt) - Sort + Dict ---
def helper_func1(id_test):
    data = load_tests("func1")[id_test]
    ret = program.func1(data['studenti'])
    expected = [tuple(e) for e in data['expected']]
    if ret != expected:
        msg_lines = [f"func1 test {id_test}: MISMATCH"]
        msg_lines.append(f"  expected ({len(expected)} results): {expected}")
        msg_lines.append(f"  returned ({len(ret)} results):    {ret}")
        if len(ret) != len(expected):
            msg_lines.append(f"  -> LENGTH MISMATCH: got {len(ret)}, expected {len(expected)}")
        else:
            for i, (r, e) in enumerate(zip(ret, expected)):
                if r != e:
                    msg_lines.append(f"  -> index {i}: expected {e}, got {r}")
        raise Exception("\n".join(msg_lines))
    return 0.5

def test_func1_1(run=None): return helper_func1(0)
def test_func1_2(run=None): return helper_func1(1)
def test_func1_3(run=None): return helper_func1(2)
def test_func1_4(run=None): return helper_func1(3)

# --- FUNC 2 (2pt, 4 test da 0.5pt) - Sets ---
def helper_func2(id_test):
    data = load_tests("func2")[id_test]
    ret = program.func2(data['lista1'], data['lista2'])
    expected = data['expected']
    if ret != expected:
        msg_lines = [f"func2 test {id_test}: MISMATCH"]
        msg_lines.append(f"  lista1={data['lista1']}, lista2={data['lista2']}")
        msg_lines.append(f"  expected ({len(expected)} items): {expected}")
        msg_lines.append(f"  returned ({len(ret)} items):    {ret}")
        if len(ret) != len(expected):
            msg_lines.append(f"  -> LENGTH MISMATCH: got {len(ret)}, expected {len(expected)}")
        else:
            for i, (r, e) in enumerate(zip(ret, expected)):
                if r != e:
                    msg_lines.append(f"  -> index {i}: expected '{e}', got '{r}'")
        extra = sorted(set(ret) - set(expected))
        missing = sorted(set(expected) - set(ret))
        if extra:
            msg_lines.append(f"  -> extra items (not expected): {extra}")
        if missing:
            msg_lines.append(f"  -> missing items (expected but not found): {missing}")
        raise Exception("\n".join(msg_lines))
    return 0.5

def test_func2_1(run=None): return helper_func2(0)
def test_func2_2(run=None): return helper_func2(1)
def test_func2_3(run=None): return helper_func2(2)
def test_func2_4(run=None): return helper_func2(3)

# --- FUNC 3 (2pt, 4 test da 0.5pt) - Dict + Sets ---
def helper_func3(id_test):
    data = load_tests("func3")[id_test]
    ret = program.func3(data['coppie'])
    expected = data['expected']
    if ret != expected:
        msg_lines = [f"func3 test {id_test}: MISMATCH"]
        msg_lines.append(f"  expected: {expected}")
        msg_lines.append(f"  returned: {ret}")
        # Check missing keys
        for k in expected:
            if k not in ret:
                msg_lines.append(f"  -> missing key '{k}' (expected {expected[k]})")
        # Check extra keys
        for k in ret:
            if k not in expected:
                msg_lines.append(f"  -> extra key '{k}' (got {ret[k]})")
        # Check value mismatches for shared keys
        for k in expected:
            if k in ret and ret[k] != expected[k]:
                msg_lines.append(f"  -> key '{k}': expected {expected[k]}, got {ret[k]}")
                extra_in_ret = sorted(set(ret[k]) - set(expected[k]))
                missing_in_ret = sorted(set(expected[k]) - set(ret[k]))
                if extra_in_ret:
                    msg_lines.append(f"       extra words: {extra_in_ret}")
                if missing_in_ret:
                    msg_lines.append(f"       missing words: {missing_in_ret}")
        raise Exception("\n".join(msg_lines))
    return 0.5

def test_func3_1(run=None): return helper_func3(0)
def test_func3_2(run=None): return helper_func3(1)
def test_func3_3(run=None): return helper_func3(2)
def test_func3_4(run=None): return helper_func3(3)

# --- FUNC 4 (4pt, 8 test da 0.5pt) - Text File I/O ---
def helper_func4(id_test):
    data = load_tests("func4")[id_test]
    input_path = os.path.join("func4", data['input_file'])
    temp_out = os.path.join("func4", f"_temp_out_{id_test}.txt")
    expected_out = os.path.join("func4", data['expected_file'])
    expected_ret = data['expected_count']

    ret = program.func4(input_path, temp_out)

    if ret != expected_ret:
        raise Exception(f"func4 test {id_test}: returned {ret}, expected {expected_ret}")

    if not os.path.isfile(temp_out):
        raise Exception(f"func4 test {id_test}: output file {temp_out} not created")

    with open(temp_out, 'r') as f:
        actual_lines = f.readlines()
    with open(expected_out, 'r') as f:
        expected_lines = f.readlines()

    if actual_lines != expected_lines:
        msg_lines = [f"func4 test {id_test}: FILE CONTENT MISMATCH"]
        msg_lines.append(f"  expected file: {data['expected_file']}")
        msg_lines.append(f"  returned file: {temp_out}")
        if len(actual_lines) != len(expected_lines):
            msg_lines.append(f"  -> LINE COUNT MISMATCH: got {len(actual_lines)} lines, expected {len(expected_lines)}")
        max_lines = max(len(actual_lines), len(expected_lines))
        for i in range(max_lines):
            actual = actual_lines[i].rstrip('\n') if i < len(actual_lines) else "<missing>"
            expected = expected_lines[i].rstrip('\n') if i < len(expected_lines) else "<missing>"
            if actual != expected:
                msg_lines.append(f"  -> line {i}: expected '{expected}', got '{actual}'")
        raise Exception("\n".join(msg_lines))

    os.remove(temp_out)
    return 0.5

def test_func4_1(run=None): return helper_func4(0)
def test_func4_2(run=None): return helper_func4(1)
def test_func4_3(run=None): return helper_func4(2)
def test_func4_4(run=None): return helper_func4(3)
def test_func4_5(run=None): return helper_func4(4)
def test_func4_6(run=None): return helper_func4(5)
def test_func4_7(run=None): return helper_func4(6)
def test_func4_8(run=None): return helper_func4(7)

# --- FUNC 5 (8pt, 8 test da 1pt) - Image Pattern Recognition ---
def helper_func5(id_test):
    data = load_tests("func5")[id_test]
    input_path = os.path.join("func5", data['input_file'])
    temp_out = os.path.join("func5", f"_temp_out_{id_test}.png")
    expected_count = data['expected_count']
    expected_out = os.path.join("func5", data['expected_file'])

    ret = program.func5(input_path, temp_out)

    if ret != expected_count:
        raise Exception(f"func5 test {id_test}: returned {ret} components, expected {expected_count}")

    if not os.path.isfile(temp_out):
        raise Exception(f"func5 test {id_test}: output file {temp_out} not created")

    # Pixel-perfect comparison
    actual_img = images.load(temp_out)
    expected_img = images.load(expected_out)
    if actual_img != expected_img:
        h = len(actual_img)
        w = len(actual_img[0]) if h else 0
        diff_count = 0
        diff_samples = []
        for r in range(min(h, len(expected_img))):
            for c in range(min(w, len(expected_img[r]) if r < len(expected_img) else 0)):
                if actual_img[r][c] != expected_img[r][c]:
                    diff_count += 1
                    if len(diff_samples) < 5:
                        diff_samples.append(f"({r},{c}): got {actual_img[r][c]}, expected {expected_img[r][c]}")
        msg_parts = [f"func5 test {id_test}: IMAGE MISMATCH"]
        msg_parts.append(f"  expected: {data['expected_file']}")
        msg_parts.append(f"  returned: {temp_out}")
        msg_parts.append(f"  -> {diff_count} pixels differ")
        if diff_samples:
            msg_parts.append(f"  -> first {len(diff_samples)} differing pixels:")
            for s in diff_samples:
                msg_parts.append(f"       {s}")
        if h != len(expected_img) or w != (len(expected_img[0]) if len(expected_img) else 0):
            msg_parts.append(f"  -> SIZE MISMATCH: got {h}x{w}, expected {len(expected_img)}x{len(expected_img[0]) if len(expected_img) else 0}")
        raise Exception("\n".join(msg_parts))

    os.remove(temp_out)
    return 0.8

def test_func5_1(run=None): return helper_func5(0)
def test_func5_2(run=None): return helper_func5(1)
def test_func5_3(run=None): return helper_func5(2)
def test_func5_4(run=None): return helper_func5(3)
def test_func5_5(run=None): return helper_func5(4)
def test_func5_6(run=None): return helper_func5(5)
def test_func5_7(run=None): return helper_func5(6)
def test_func5_8(run=None): return helper_func5(7)
def test_func5_9(run=None): return helper_func5(8)
def test_func5_10(run=None): return helper_func5(9)

# --- EX 1 (7pt, 7 test da 1pt) - Ricorsione: albero ---
def helper_ex1(id_test):
    data = load_tests("ex1")[id_test]
    tree_data = data['tree']

    # Recursion check abilitato dalla proprieta' "recursion" nei dati del test
    if not DEBUG and data.get('recursion', False):
        isrecursive.decorate_module(program)
        try:
            if tree_data is not None:
                albero = tree.BinaryTree.fromList(tree_data)
            else:
                albero = None
            program.ex1(albero)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Ricorsione non usata in ex1!")
        finally:
            isrecursive.undecorate_module(program)

    if tree_data is not None:
        albero = tree.BinaryTree.fromList(tree_data)
    else:
        albero = None
    ret = program.ex1(albero)
    expected = tuple(data['expected'])
    if ret != expected:
        msg_lines = [f"ex1 test {id_test}: MISMATCH"]
        msg_lines.append(f"  tree: {tree_data}")
        msg_lines.append(f"  returned: {ret}")
        msg_lines.append(f"  expected: {expected}")
        if not isinstance(ret, tuple) or len(ret) != 2:
            msg_lines.append(f"  -> expected a tuple of (depth, value), got {type(ret)}")
        else:
            if ret[0] != expected[0]:
                msg_lines.append(f"  -> depth mismatch: got {ret[0]}, expected {expected[0]}")
            if ret[1] != expected[1]:
                msg_lines.append(f"  -> value mismatch: got {ret[1]}, expected {expected[1]}")
        raise Exception("\n".join(msg_lines))
    return 1

def test_ex1_1(run=None): return helper_ex1(0)
def test_ex1_2(run=None): return helper_ex1(1)
def test_ex1_3(run=None): return helper_ex1(2)
def test_ex1_4(run=None): return helper_ex1(3)
def test_ex1_5(run=None): return helper_ex1(4)
def test_ex1_6(run=None): return helper_ex1(5)
def test_ex1_7(run=None): return helper_ex1(6)

# --- EX 2 (7pt, 7 test da 1pt) - Ricorsione: liste annidate ---
def helper_ex2(id_test):
    data = load_tests("ex2")[id_test]
    nested = data['nested']

    if not DEBUG:
        import copy
        isrecursive.decorate_module(program)
        try:
            program.ex2(copy.deepcopy(nested))
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Ricorsione non usata in ex2!")
        finally:
            isrecursive.undecorate_module(program)

    ret = program.ex2(nested)
    expected = data['expected']
    if ret != expected:
        msg_lines = [f"ex2 test {id_test}: MISMATCH"]
        msg_lines.append(f"  nested: {nested}")
        msg_lines.append(f"  expected ({len(expected)} items): {expected}")
        msg_lines.append(f"  returned ({len(ret)} items):    {ret}")
        if len(ret) != len(expected):
            msg_lines.append(f"  -> LENGTH MISMATCH: got {len(ret)}, expected {len(expected)}")
        else:
            for i, (r, e) in enumerate(zip(ret, expected)):
                if r != e:
                    msg_lines.append(f"  -> index {i}: expected {e}, got {r}")
        extra = [x for x in ret if x not in expected]
        missing = [x for x in expected if x not in ret]
        if extra:
            msg_lines.append(f"  -> extra items: {extra}")
        if missing:
            msg_lines.append(f"  -> missing items: {missing}")
        raise Exception("\n".join(msg_lines))
    return 1

def test_ex2_1(run=None): return helper_ex2(0)
def test_ex2_2(run=None): return helper_ex2(1)
def test_ex2_3(run=None): return helper_ex2(2)
def test_ex2_4(run=None): return helper_ex2(3)
def test_ex2_5(run=None): return helper_ex2(4)
def test_ex2_6(run=None): return helper_ex2(5)
def test_ex2_7(run=None): return helper_ex2(6)


##########################################################################################

tests = [
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3, test_func4_4,
    test_func4_5, test_func4_6, test_func4_7, test_func4_8,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_func5_5, test_func5_6, test_func5_7, test_func5_8,
    test_func5_9, test_func5_10,
    test_ex1_1, test_ex1_2, test_ex1_3, test_ex1_4,
    test_ex1_5, test_ex1_6, test_ex1_7,
    test_ex2_1, test_ex2_2, test_ex2_3, test_ex2_4,
    test_ex2_5, test_ex2_6, test_ex2_7,
    test_personal_data_entry,
]

if __name__ == '__main__':
    check_expected()
    results = testlib.run(tests, verbose=True)
    total = sum(v for _, v in results if v and v > 0)
    print(f"\n{'='*50}")
    nome      = getattr(program, 'nome',      getattr(program, 'name',       'NOME'))
    cognome   = getattr(program, 'cognome',   getattr(program, 'surname',    'COGNOME'))
    matricola = getattr(program, 'matricola', getattr(program, 'student_id', 'MATRICOLA'))
    print(f"Student: {nome} {cognome} (matricola: {matricola})")
    if    nome == 'NOME' or cognome == 'COGNOME' or matricola == 'MATRICOLA': 
        raise Exception("PERSONAL DATA NOT COMPLETE")
    print(f"TOTAL SCORE: {total:.1f} / 32.0")
    print(f"{'='*50}")
