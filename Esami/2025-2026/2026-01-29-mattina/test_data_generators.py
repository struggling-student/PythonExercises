import os
import json
import random
import images
from program import func5, ex2

def setup_directory(name):
    if not os.path.exists(name):
        os.makedirs(name)
    return name

def generate_func5_data(count):
    folder = setup_directory("func5")
    data = []
    for i in range(count):
        img = [[(0, 0, 0) for _ in range(30)] for _ in range(30)]
        target_color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        
        # Genera da 1 a 4 rettangoli casuali
        num_rects = random.randint(1, 4)
        rects_info = []
        for _ in range(num_rects):
            w, h = random.randint(2, 5), random.randint(2, 5)
            # Assicura spazio per non toccarsi
            x, y = random.randint(0, 24), random.randint(0, 24)
            
            # Controllo sovrapposizione semplice per il generatore
            overlap = False
            for rx, ry, rw, rh in rects_info:
                if not (x + w + 1 < rx or x > rx + rw + 1 or y + h + 1 < ry or y > ry + rh + 1):
                    overlap = True; break
            if overlap: continue
            
            for r in range(y, y + h):
                for c in range(x, x + w):
                    img[r][c] = target_color
            rects_info.append((x, y, w, h))
            
        path = os.path.join(folder, f"input_{i}.png")
        images.save(img, path)
        expected = func5(path, target_color)
        data.append({"path": path, "target": target_color, "expected": expected})
        
    with open(os.path.join(folder, "tests.json"), "w") as f:
        json.dump(data, f, indent=4)
    print(f"[func5] Generati {count} test.")


def generate_ex2_data(count):
    folder = setup_directory("ex2")
    data = []
    keys = ["a", "b", "c", "d", "user", "settings", "data", "info"]
    for i in range(count):
        # Genera una chain casuale
        chain_len = random.randint(2, 5)
        chain = random.sample(keys, chain_len)

        # Costruisce un dizionario che segue DETERMINISTICAMENTE la chain
        # per assicurare che la ricorsione venga triggerata fino in fondo
        def build_forced_dict(current_chain):
            if not current_chain:
                return random.randint(1, 100)

            # Crea il dizionario con la chiave necessaria per proseguire
            d = {current_chain[0]: build_forced_dict(current_chain[1:])}

            # Aggiunge opzionalmente altre chiavi "rumore"
            for _ in range(random.randint(0, 2)):
                noise_key = random.choice(keys)
                if noise_key not in d:
                    d[noise_key] = random.randint(1, 100)
            return d

        d = build_forced_dict(chain)

        # Calcola l'atteso (che sarà sempre len(chain) + 1 se l'ultimo valore non è dict)
        expected = ex2(d, chain)
        data.append({"data": d, "chain": chain, "expected": expected})

    with open(os.path.join(folder, "tests.json"), "w") as f:
        json.dump(data, f, indent=4)
    print(f"[ex2] Generati {count} test (ricorsione forzata).")

if __name__ == "__main__":
    generate_func5_data(6)
    generate_ex2_data(6)
    print("\nGenerazione completata.")
