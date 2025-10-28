import random
import string

VOWELS = 'aeiou'
CONSONANTS = ''.join(set(string.ascii_lowercase) - set(VOWELS))

def generate_realistic_word(max_len):
    """
    Genera una parola che alterna consonanti e vocali,
    finisce sempre con una vocale,
    e può contenere consonanti doppie.
    """
    if max_len < 2:
        raise ValueError("La lunghezza minima deve essere almeno 2")

    # Decidi lunghezza: almeno 2, massimo max_len
    length = random.randint(2, max_len)

    word = []
    next_is_vowel = random.choice([True, False])

    # Costruzione normale fino alla penultima lettera
    while len(word) < length - 1:
        if next_is_vowel:
            word.append(random.choice(VOWELS))
        else:
            c = random.choice(CONSONANTS)
            word.append(c)
            # possibilità di doppia consonante
            if len(word) < length - 1 and random.random() < 0.2:
                word.append(c)
        next_is_vowel = not next_is_vowel

    # Assicurati che l'ultima lettera sia una vocale
    word.append(random.choice(VOWELS))

    return ''.join(word)


def random_case(word):
    """Restituisce una parola con casing random per ogni lettera."""
    return ''.join(
        c.upper() if random.random() < 0.5 else c.lower()
        for c in word
    )

def generate_func4_input_file(filepath,
                              num_words=100,
                              max_word_length=8,
                              num_duplicates=0,
                              num_uppercase=0.3,
                              separators=" ,;\t"):
    """
    Genera un file di parole realistiche con duplicati e casing casuale.
    """
    words = set()
    while len(words) < num_words:
        words.add(generate_realistic_word(max_word_length))

    base_words = list(words)

    # Genera parole iniziali con casing casuale
    word_list = [
        random_case(word) if random.random() < num_uppercase else word
        for word in base_words
    ]

    # Aggiungi duplicati con casing casuale sempre nuovo
    for _ in range(num_duplicates):
        base = random.choice(base_words)
        dup_variant = random_case(base)
        word_list.append(dup_variant)

    # Mescola e scrivi nel file
    random.shuffle(word_list)
    sep_list = list(separators)

    with open(filepath, 'w') as f:
        for i, word in enumerate(word_list):
            f.write(word)
            if i < len(word_list) - 1:
                f.write(random.choice(sep_list))
        f.write('\n')


generate_func4_input_file(
    filepath="func4/in_test1.txt",
    num_words=10,
    max_word_length=3,
    num_duplicates=2,
    num_uppercase=0.5,
    separators=" ,;\t\n"
)