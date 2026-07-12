#!/usr/bin/env python3
# -*- coding: utf-8 -*-

nome = "hide"
cognome = "matsumoto"
matricola = "5050"

import tree
import images


def func1(moves: str) -> tuple[int, int]:
    score = 0
    combos = 0
    for i, ch in enumerate(moves):
        if ch != "F":
            continue
        if i >= 4 and moves[i - 4:i] == "UUDD":
            score += 50
            combos += 1
        else:
            score += 10
    return score, combos


def func2(hand: list[int]) -> tuple[int, int]:
    counts = {}
    for r in hand:
        counts[r] = counts.get(r, 0) + 1
    pairs = 0
    trips = 0
    for c in counts.values():
        if c == 2:
            pairs += 1
        elif c == 3:
            trips += 1
    return pairs, trips


def func3(expr: str) -> int:
    # parsing semplice: leggiamo termini con segno +/-
    s = expr.replace(" ", "")
    if not s:
        return 0

    i = 0
    total = 0
    sign = 1

    def read_int():
        nonlocal i
        j = i
        if j < len(s) and s[j] == "-":
            j += 1
        while j < len(s) and s[j].isdigit():
            j += 1
        v = int(s[i:j])
        i = j
        return v

    while i < len(s):
        if s[i] == "+":
            sign = 1
            i += 1
            continue
        if s[i] == "-":
            sign = -1
            i += 1
            continue

        # term: either int or XdY
        # read X
        x = 0
        while i < len(s) and s[i].isdigit():
            x = x * 10 + int(s[i])
            i += 1

        if i < len(s) and s[i] == "d":
            i += 1
            y = 0
            while i < len(s) and s[i].isdigit():
                y = y * 10 + int(s[i])
                i += 1
            # max of XdY is X*Y
            term = x * y
        else:
            term = x

        total += sign * term

    return total


def func4(path: str, deck_size: int, top_n: int) -> list[int]:
    deck = list(range(1, deck_size + 1))

    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            parts = line.split()
            cmd = parts[0]

            if cmd == "CUT":
                k = int(parts[1])
                if k >= 0:
                    deck = deck[k:] + deck[:k]
                else:
                    k = -k
                    deck = deck[-k:] + deck[:-k]

            elif cmd == "REVERSE":
                deck.reverse()

            elif cmd == "SWAP":
                a = int(parts[1])
                b = int(parts[2])
                deck[a], deck[b] = deck[b], deck[a]

            else:
                raise ValueError(f"Comando sconosciuto: {cmd}")

    return deck[:top_n]


def func5(path_in: str, path_out: str, c1: tuple[int, int, int], c2: tuple[int, int, int]) -> tuple[int, int]:
    img = images.load(path_in)
    h = len(img)
    w = len(img[0]) if h else 0

    c1_count = 0
    c2_count = 0

    out = [[(0, 0, 0) for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            px = img[y][x]
            if px == c1:
                c1_count += 1
                out[y][x] = c2
            elif px == c2:
                c2_count += 1
                out[y][x] = c1
            else:
                out[y][x] = px

    images.save(out, path_out)
    return c1_count, c2_count



def rec(i: int, t: int, memo, rolls) -> int:
    if t == 0:
        return 1
    if t < 0:
        return 0
    if i == len(rolls):
        return 0
    key = (i, t)
    if key in memo:
        return memo[key]
    v = rolls[i]
    total = 0
    k = 0
    while k * v <= t:
        total += rec(i + 1, t - k * v, memo, rolls)
        k += 1
    memo[key] = total
    return total

def ex1(rolls: list[int], target: int) -> int:
    rolls = sorted(rolls)

    memo: dict[tuple[int, int], int] = {}

    return rec(0, target, memo, rolls)


def ex2(root: tree.BinaryTree) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.value
    left_best = ex2(root.left) if root.left is not None else None
    right_best = ex2(root.right) if root.right is not None else None
    if left_best is None:
        return root.value + right_best
    if right_best is None:
        return root.value + left_best
    return root.value + max(left_best, right_best)


if __name__ == "__main__":
    print("Esegui grade.py per i test.")