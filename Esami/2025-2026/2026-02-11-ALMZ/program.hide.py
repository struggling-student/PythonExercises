#!/usr/bin/env python3
# -*- coding: utf-8 -*-

nome = "hide"
cognome = "matsumoto"
matricola = "5050"

import tree
import images


def func1(s: str) -> str:
    if not s:
        return ""
    out = []
    cur = s[0]
    cnt = 1
    for ch in s[1:]:
        if ch == cur:
            cnt += 1
        else:
            out.append(cur + str(cnt))
            cur = ch
            cnt = 1
    out.append(cur + str(cnt))
    return "".join(out)


def func2(a: list[int], b: list[int]) -> list[int]:
    ca = {}
    for x in a:
        ca[x] = ca.get(x, 0) + 1
    cb = {}
    for x in b:
        cb[x] = cb.get(x, 0) + 1
    out = []
    for x in ca:
        if x in cb:
            out.extend([x] * min(ca[x], cb[x]))
    return out


def func3(tokens: list[str]) -> int:
    st: list[int] = []
    for t in tokens:
        if t in {"+", "-", "*", "//"}:
            b = st.pop()
            a = st.pop()
            if t == "+":
                st.append(a + b)
            elif t == "-":
                st.append(a - b)
            elif t == "*":
                st.append(a * b)
            else:
                st.append(a // b)
        else:
            st.append(int(t))
    return st[-1]


def func4(path: str) -> dict[str, int]:
    res: dict[str, int] = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, qty = line.split(",", 1)
            name = name.strip()
            qty_i = int(qty.strip())
            res[name] = res.get(name, 0) + qty_i
    return res


def func5(path_in: str) -> tuple[tuple[int, int, int], int]:
    img = images.load(path_in)
    counts: dict[tuple[int, int, int], int] = {}
    for row in img:
        for px in row:
            if px != (0, 0, 0):
                counts[px] = counts.get(px, 0) + 1
    if not counts:
        return (0, 0, 0), 0
    best_color = None
    best_count = -1
    for c, k in counts.items():
        if k > best_count or (k == best_count and c < best_color):
            best_color = c
            best_count = k
    return best_color, best_count


def rec1(i: int, bal: int, memo, s) -> bool:
    if bal < 0:
        return False
    if i == len(s):
        return bal == 0
    key = (i, bal)
    if key in memo:
        return memo[key]
    ch = s[i]
    if ch == "(":
        ans = rec1(i + 1, bal + 1, memo, s)
    elif ch == ")":
        ans = rec1(i + 1, bal - 1, memo, s)
    else:  # '*'
        ans = rec1(i + 1, bal, memo, s) or rec1(i + 1, bal + 1, memo, s) or rec1(i + 1, bal - 1, memo, s)
    memo[key] = ans
    return ans
def ex1(s: str) -> bool:
    memo: dict[tuple[int, int], bool] = {}
    return rec1(0, 0, memo, s)

def rec(node: tree.BinaryTree, level: int) -> int:
    if node is None:
        return 0
    add = node.value if (level % 2 == 1) else 0
    return add + rec(node.left, level + 1) + rec(node.right, level + 1)

def ex2(root: tree.BinaryTree) -> int:

    return rec(root, 0)


if __name__ == "__main__":
    print("Esegui grade.py per i test.")