import random
from images import save

BLACK = (0, 0, 0)

GROUP_SHAPES = {
    "1x1": [(0, 0)],
    "1x2": [(0, 0), (0, 1)],
    "2x1": [(0, 0), (1, 0)],
    "2x2": [(0, 0), (0, 1), (1, 0), (1, 1)],
}

def random_color():
    return tuple(random.randint(1, 255) for _ in range(3))

def generate_test_image_with_margins(filename, width, height, perc_2x2=0.3, max_attempts=1000):
    """
    Genera un'immagine con blocchi separati da almeno 1 pixel nero attorno.
    Blocchi distribuiti casualmente.
    """
    image = [[BLACK for _ in range(width)] for _ in range(height)]
    used = [[False for _ in range(width)] for _ in range(height)]

    attempts = 0
    while attempts < max_attempts:
        attempts += 1

        block_type = (
            "2x2" if random.random() < perc_2x2
            else random.choice(["1x1", "1x2", "2x1"])
        )
        shape = GROUP_SHAPES[block_type]
        color = random_color()

        # Trova posizione casuale valida
        i = random.randint(0, height - 1)
        j = random.randint(0, width - 1)
        coords = [(i + dx, j + dy) for dx, dy in shape]

        # Verifica che il blocco stia dentro l'immagine
        if not all(0 <= x < height and 0 <= y < width for x, y in coords):
            continue

        # Verifica che il blocco e il margine siano liberi
        blocked = False
        for x, y in coords:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < height and 0 <= ny < width:
                        if used[nx][ny]:
                            blocked = True
                            break
                if blocked:
                    break
            if blocked:
                break

        if blocked:
            continue

        # Inserisci blocco
        for x, y in coords:
            image[x][y] = color
            used[x][y] = True

    save(image, filename)


placed = generate_test_image_with_margins(
    filename="func5/in_test3.png",
    width=4,
    height=50,
    perc_2x2=0.9  # 40% dei blocchi saranno 2x2
)