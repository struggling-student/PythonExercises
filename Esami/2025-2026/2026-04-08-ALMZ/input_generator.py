import os
import csv
import random
import json
from tree import BinaryTree
import images
from collections import deque
from program import func5, ex2


# Configurazione
POINTS = {
    "func5": 6,
    "ex1": 6,
    "ex2": 6
}


def setup_directory(name):
    if not os.path.exists(name):
        os.makedirs(name)
    return name


# --- HELPERS PER CALCOLO ATTESI ---

def get_height(node):
    if not node: return 0
    return 1 + max(get_height(node.left), get_height(node.right))


def is_balanced(node):
    if not node: return True
    lh = get_height(node.left)
    rh = get_height(node.right)
    if abs(lh - rh) > 1: return False
    return is_balanced(node.left) and is_balanced(node.right)



# --- GENERATORI ---


def generate_ex1(count):
    folder = setup_directory("ex1")
    for i in range(count):
        depth = random.randint(2, 5)
        t_obj = BinaryTree.randomTree(depth)
        while t_obj is None: t_obj = BinaryTree.randomTree(depth)

        ans = is_balanced(t_obj)
        with open(os.path.join(folder, f"input_{i}.json"), 'w') as f:
            json.dump({"tree": t_obj.toList(), "expected": ans}, f, indent=4)
    print(f"[ex1] Generati {count} test JSON con 'expected' incluso.")



def generate_func5_data(count):
    folder = setup_directory("func5")
    data = []
    for i in range(count):
        # Aumentiamo la dimensione per gestire meglio più rettangoli
        img = [[(0, 0, 0) for _ in range(50)] for _ in range(50)]
        target_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

        # Genera da 1 a 5 rettangoli casuali che non si toccano
        num_rects = random.randint(1, 5)
        rects_added = []

        for _ in range(num_rects):
            w, h = random.randint(2, 8), random.randint(2, 8)
            # Tentativi per posizionare senza collisioni (semplice)
            for _ in range(20):
                x, y = random.randint(1, 40), random.randint(1, 40)

                # Check collisione (inclusa cornice di 1 pixel per non toccarsi)
                conflict = False
                for rx, ry, rw, rh in rects_added:
                    if not (x + w + 1 < rx or x > rx + rw + 1 or y + h + 1 < ry or y > ry + rh + 1):
                        conflict = True
                        break

                if not conflict:
                    for r in range(y, y + h):
                        for c in range(x, x + w):
                            img[r][c] = target_color
                    rects_added.append((x, y, w, h))
                    break

        path = os.path.join(folder, f"input_{i}.png")
        images.save(img, path)

        # L'atteso viene calcolato salvando il risultato in un file "expected_i.png"
        path_expected = os.path.join(folder, f"expected_{i}.png")
        func5(path, path_expected)

        data.append({
            "path": path,
            "target": target_color,
            "expected": path_expected
        })

    with open(os.path.join(folder, "tests.json"), "w") as f:
        json.dump(data, f, indent=4)
    print(f"[func5] Generati {count} test PNG + file expected.")

def generate_ex2_data(count):
    folder = setup_directory("ex2")
    data = []

    def build_nested_list(depth):
        if depth <= 0:
            # Genera un intero casuale (pari o dispari)
            return random.randint(1, 20)

        lst = []
        # Ogni lista ha da 1 a 4 elementi
        for _ in range(random.randint(1, 4)):
            if random.random() < 0.4:  # 40% probabilità di un'altra sottolista
                lst.append(build_nested_list(depth - 1))
            else:
                lst.append(random.randint(1, 20))
        return lst

    def calculate_expected(lst):
        total = 0
        for item in lst:
            if isinstance(item, list):
                total += calculate_expected(item)
            elif isinstance(item, int):
                if item % 2 == 0:
                    total += item
        return total

    for i in range(count):
        # Genera una struttura nidificata di profondità variabile
        d = build_nested_list(random.randint(2, 4))

        # Calcolo atteso basato sulla nuova specifica (somma pari in liste)
        expected = calculate_expected(d)

        data.append({
            "data": d,
            "expected": expected
        })

    with open(os.path.join(folder, "tests.json"), "w") as f:
        json.dump(data, f, indent=4)
    print(f"[ex2] Generati {count} test nested lists (somma pari) + expected.")



if __name__ == "__main__":
    generate_func5_data(POINTS["func5"])
    generate_ex2_data(POINTS["ex2"])

    generate_ex1(POINTS["ex1"])
    print("\nGenerazione completata.")