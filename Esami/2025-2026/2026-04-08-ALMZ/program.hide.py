import csv
import json
import tree
import images

# Assegna le variabili con i tuoi dati
nome = "hide"
cognome = "matsumoto"
matricola = "5050"


# %% ----------------------------------- FUNC.1 ----------------------------------- #
def func1(n: int) -> int:
    """Conta il numero di bit impostati a 1 (popcount)."""
    # Utilizziamo il metodo bit_count() disponibile da Python 3.10+
    # o la conversione in stringa binaria per compatibilità
    return bin(n).count('1')


# %% ----------------------------------- FUNC.2 ---------------------------------- #
def func2(message: str, colors: dict) -> str:
    """Sostituisce i tag [color:nome] con <#CODICE>."""
    import re

    def replace_tag(match):
        color_name = match.group(1)
        text = match.group(2)
        code = colors.get(color_name, "UNKNOWN")
        return f"<{code}>{text}</{code}>"

    # Regex per catturare il nome del colore e il testo tra i tag
    pattern = r"\[color:(.*?)\](.*?)\[/color\]"
    return re.sub(pattern, replace_tag, message)


# %% ----------------------------------- FUNC.3 ---------------------------------- #
def func3(inventory: dict, recipe: dict) -> bool:
    """Verifica se i materiali in inventario bastano per la ricetta."""
    for item, qty_needed in recipe.items():
        if item not in inventory or inventory[item] < qty_needed:
            return False
    return True


# %% ----------------------------------- FUNC.4 ---------------------------------- #
def func4(base_stats: dict, equipment: list[dict]) -> dict:
    """Calcola statistiche finali: (Base + Sum(add)) * Product(mult)."""
    final_stats = {k: float(v) for k, v in base_stats.items()}

    # Raggruppiamo i bonus per statistica
    stats_to_process = set(base_stats.keys())
    for item in equipment:
        stats_to_process.add(item['stat'])

    for s in stats_to_process:
        if s not in final_stats:
            final_stats[s] = 0.0

        # 1. Applica tutti gli 'add'
        adds = [e['val'] for e in equipment if e['stat'] == s and e['type'] == 'add']
        final_stats[s] += sum(adds)

        # 2. Applica tutti i 'mult' sul risultato precedente
        muls = [e['val'] for e in equipment if e['stat'] == s and e['type'] == 'mul']
        for m in muls:
            final_stats[s] *= m

    return final_stats


# %% ----------------------------------- FUNC.5 ---------------------------------- #
def func5(path_in: str, path_out: str):
    """
    Ruota una macchia di pixel di 90 gradi in senso orario attorno al baricentro.
    """
    img = images.load(path_in)
    h, w = len(img), len(img[0])

    # 1. Trova i pixel della macchia e calcola il baricentro
    pixels = []
    sum_x = 0
    sum_y = 0
    for r in range(h):
        for c in range(w):
            if img[r][c] != (0, 0, 0):
                pixels.append((c, r, img[r][c]))
                sum_x += c
                sum_y += r

    if not pixels:
        images.save(img, path_out)
        return

    x_bar = round(sum_x / len(pixels))
    y_bar = round(sum_y / len(pixels))

    # 2. Crea immagine di output nera
    new_img = [[(0, 0, 0) for _ in range(w)] for _ in range(h)]

    # 3. Ruota ogni pixel: (x', y') = (y_bar - y + x_bar, x - x_bar + y_bar)
    for x, y, color in pixels:
        new_x = y_bar - y + x_bar
        new_y = x - x_bar + y_bar

        # Verifica bordi
        if 0 <= new_x < w and 0 <= new_y < h:
            new_img[new_y][new_x] = color

    images.save(new_img, path_out)


# %% ----------------------------------- EX.1 ------------------------- #
def check(node):
    if node is None:
        return 0, True

    h_l, bal_l = check(node.left)
    h_r, bal_r = check(node.right)

    # Un nodo è bilanciato se i figli lo sono e la diff. altezza <= 1
    is_bal = bal_l and bal_r and abs(h_l - h_r) <= 1
    height = 1 + max(h_l, h_r)

    return height, is_bal


def ex1(root: tree.BinaryTree) -> bool:
    """Verifica se l'albero è bilanciato in altezza (Ricorsivo)."""



    _, result = check(root)
    return result


# %% ----------------------------------- EX.2 ------------------------- #


def backtrack(node, all_min_path_pixels, parents):
    if node in all_min_path_pixels:
        return
    all_min_path_pixels.add(node)
    for p in parents.get(node, []):
        backtrack(p, all_min_path_pixels, parents)

def ex2(data: list) -> int:
    """
    Calcola ricorsivamente la somma dei numeri PARI in liste annidate.
    """
    total = 0
    for item in data:
        if isinstance(item, list):
            # Chiamata ricorsiva per le sottoliste
            total += ex2(item)
        elif isinstance(item, int):
            # Aggiungi solo se intero e pari
            if item % 2 == 0:
                total += item
    return total


if __name__ == '__main__':
    print('*' * 50)
    print('Esegui grade.py per il test automatico.')
    print('*' * 50)