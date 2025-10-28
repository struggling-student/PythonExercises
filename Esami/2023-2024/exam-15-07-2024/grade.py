# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys
import tree
from testlib import my_print, COL, check_expected

############ check that you have renamed the file as program.py   ###########
if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
#############################################################################

import program

#############################################################################
#### Use DEBUG=True to disable the recursion tests and enable the
#### stack trace: each error will produce a more verbose output
####
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
DEBUG = True
DEBUG = False
#############################################################################

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #

# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

def test_personal_data_entry(run=True):
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', f"{COL['YELLOW']}ERROR: Please assign the 'name' variable with YOUR NAME in program.py{COL['RST']}"
        assert program.surname    != 'SURNAME', f"{COL['YELLOW']}ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py{COL['RST']}"
        assert program.student_id != 'MATRICULATION NUMBER', f"{COL['YELLOW']}ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py{COL['RST']}"
        print(f'{COL["GREEN"]}Student info: {program.name} {program.surname} {program.student_id}{COL["RST"]}')
    else:
        assert program.nome      != 'NOME', f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
        assert program.cognome   != 'COGNOME', f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
        assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
        print(f'{COL["GREEN"]}Informazioni studente: {program.nome} {program.cognome} {program.matricola}{COL["RST"]}')
    return 1e-9

def add_docstring(f, local):
    S = ''
    if 'run' in local: del local['run']
    for key, val in local.items():
        S += f'\n{key} = {val}'
    f.__doc__ = S


###############################################################################


def do_func1_tests(L, expected):
    res = program.func1(L)
    testlib.check(res, expected)
    return 0.5


def test_func1_1(run=True):
    '''
    L = ['cAsa', 'xyzzY', 'gAtto', 'topO', 'ragno', 'canE', 'tappEto', 'Oca']
    expected = [(7, 3), (3, 2), (4, 2), (4, 2), (4, 2), (5, 2), (5, 2), (5, 0)]
    '''
    L = ['cAsa', 'xyzzY', 'gAtto', 'topO', 'ragno', 'canE', 'tappEto', 'Oca']
    expected = [(7, 3), (3, 2), (4, 2), (4, 2), (4, 2), (5, 2), (5, 2), (5, 0)]
    return do_func1_tests(L, expected)

def test_func1_2(run=True):
    '''
    L = ['clusTeR', 'StoRAge', 'nEgLIGeE', 'bUzE', 'hoLd']
    expected = [(8, 4), (7, 3), (4, 2), (7, 2), (4, 1)]
    '''
    L = ['clusTeR', 'StoRAge', 'nEgLIGeE', 'bUzE', 'hoLd']
    expected = [(8, 4), (7, 3), (4, 2), (7, 2), (4, 1)]
    return do_func1_tests(L, expected)

def test_func1_3(run=True):
    '''
    L = ['cORMoranT', 'maRsHLaNd', 'MatRIX', 'povERtY', 'ECoNoMIc', 'Elbow', 'pILGRim', 'Bug', 'MilLet', 'THREat', 'hOMIcidE', 'reGIstRY', 'sliPPErS', 'YACHT', 'LIFetime']
    expected = [(8, 4), (8, 4), (8, 4), (9, 3), (5, 2), (6, 2), (6, 2), (6, 2), (7, 2), (7, 2), (8, 2), (8, 2), (9, 2), (3, 1), (5, 1)]
    '''
    L = ['cORMoranT', 'maRsHLaNd', 'MatRIX', 'povERtY', 'ECoNoMIc', 'Elbow', 'pILGRim', 'Bug', 'MilLet', 'THREat', 'hOMIcidE', 'reGIstRY', 'sliPPErS', 'YACHT', 'LIFetime']
    expected = [(8, 4), (8, 4), (8, 4), (9, 3), (5, 2), (6, 2), (6, 2), (6, 2), (7, 2), (7, 2), (8, 2), (8, 2), (9, 2), (3, 1), (5, 1)]
    return do_func1_tests(L, expected)

def test_func1_4(run=True):
    '''
    L = ['tREaSUrE', 'fOg', 'tROUBLESHoOT', 'FelonY', 'eXPeCT', 'SolITAIRE', 'PReMISe', 'reViEW', 'tRAnquIl', 'eYELaShEs', 'DivalEnt', 'angUISH', 'KaRaTe', 'dRinKInG', 'FOrtNigHt', 'goldfiSH', 'SummIt', 'taPe', 'lOCaTioN', 'aBoRiginaL', 'cOffIN', 'pIN', 'SHocKINg', 'BOred', 'sOUR']
    expected = [(9, 5), (10, 5), (12, 5), (8, 4), (8, 4), (9, 4), (6, 3), (6, 3), (7, 3), (7, 3), (8, 3), (8, 3), (4, 2), (4, 2), (5, 2), (6, 2), (6, 2), (6, 2), (6, 2), (8, 2), (8, 2), (8, 2), (9, 2), (3, 1), (3, 1)]
    '''
    L = ['tREaSUrE', 'fOg', 'tROUBLESHoOT', 'FelonY', 'eXPeCT', 'SolITAIRE', 'PReMISe', 'reViEW', 'tRAnquIl', 'eYELaShEs', 'DivalEnt', 'angUISH', 'KaRaTe', 'dRinKInG', 'FOrtNigHt', 'goldfiSH', 'SummIt', 'taPe', 'lOCaTioN', 'aBoRiginaL', 'cOffIN', 'pIN', 'SHocKINg', 'BOred', 'sOUR']
    expected = [(9, 5), (10, 5), (12, 5), (8, 4), (8, 4), (9, 4), (6, 3), (6, 3), (7, 3), (7, 3), (8, 3), (8, 3), (4, 2), (4, 2), (5, 2), (6, 2), (6, 2), (6, 2), (6, 2), (8, 2), (8, 2), (8, 2), (9, 2), (3, 1), (3, 1)]
    return do_func1_tests(L, expected)

################################################################################

def do_func2_tests(D, expected):
    res = program.func2(D)
    testlib.check_list(res, expected)
    return 0.5

def test_func2_1(run=True):
    '''
    D = {1: ['casa', 'gatto', 'topo', 'ragno'], 2: ['tappeto', 'cane', 'oca']}
    expected = {(2, 'cane', 'tappeto'), (1, 'casa', 'topo')}
    '''
    D = {1: ['casa', 'gatto', 'topo', 'ragno'], 2: ['tappeto', 'cane', 'oca']}
    expected = {(2, 'cane', 'tappeto'), (1, 'casa', 'topo')}
    return do_func2_tests(D, expected)

def test_func2_2(run=True):
    '''
    D = {1: ['mama', 'samurai', 'dynamics', 'plier'], 2: ['controversy', 'somersault', 'dog', 'elfin'], 3: ['peanut', 'lumber', 'harm', 'cornet'], 4: ['corduroy', 'hybridisation', 'rebellion', 'retreat'], 5: ['instinct', 'elicit', 'piracy', 'divergent'], 6: ['justify', 'alcohol', 'perspective', 'undesirable'], 7: ['seep', 'ability', 'TV', 'propose'], 8: ['facelift', 'privilege', 'attitude', 'build'], 9: ['moonlight', 'larva', 'curler', 'broker'], 10: ['consequence', 'plaster', 'fame', 'signet'], 11: ['reminder', 'affect', 'authority', 'chassis']}
    expected = {(5, 'divergent', 'piracy'), (7, 'TV', 'seep'), (2, 'controversy', 'somersault'), (10, 'consequence', 'signet'), (8, 'attitude', 'privilege'), (1, 'dynamics', 'samurai'), (4, 'corduroy', 'retreat'), (6, 'alcohol', 'undesirable'), (3, 'cornet', 'peanut'), (11, 'affect', 'reminder'), (9, 'broker', 'moonlight')}
    '''
    D = {1: ['mama', 'samurai', 'dynamics', 'plier'], 2: ['controversy', 'somersault', 'dog', 'elfin'], 3: ['peanut', 'lumber', 'harm', 'cornet'], 4: ['corduroy', 'hybridisation', 'rebellion', 'retreat'], 5: ['instinct', 'elicit', 'piracy', 'divergent'], 6: ['justify', 'alcohol', 'perspective', 'undesirable'], 7: ['seep', 'ability', 'TV', 'propose'], 8: ['facelift', 'privilege', 'attitude', 'build'], 9: ['moonlight', 'larva', 'curler', 'broker'], 10: ['consequence', 'plaster', 'fame', 'signet'], 11: ['reminder', 'affect', 'authority', 'chassis']}
    expected = {(5, 'divergent', 'piracy'), (7, 'TV', 'seep'), (2, 'controversy', 'somersault'), (10, 'consequence', 'signet'), (8, 'attitude', 'privilege'), (1, 'dynamics', 'samurai'), (4, 'corduroy', 'retreat'), (6, 'alcohol', 'undesirable'), (3, 'cornet', 'peanut'), (11, 'affect', 'reminder'), (9, 'broker', 'moonlight')}
    return do_func2_tests(D, expected)

def test_func2_3(run=True):
    '''
    D = {1: ['mortal', 'pint', 'glasses', 'overheard', 'sunglasses', 'apricot', 'lid', 'stupidity'], 2: ['itch', 'try', 'encouraging', 'ray', 'cleft', 'great-grandfather', 'hate', 'selective'], 3: ['seeker', 'executive', 'hydraulics', 'incarnation', 'dissonance', 'pheasant', 'tribe', 'medication'], 4: ['perfume', 'tic', 'melon', 'album', 'son', 'comfort', 'hearsay', 'robotics'], 5: ['gutter', 'become', 'minimalism', 'spyglass', 'attendant', 'sled', 'skyscraper', 'sunday'], 6: ['lieu', 'ordination', 'extract', 'navigate', 'revolution', 'validity', 'repayment', 'schnitzel'], 7: ['moonlight', 'beset', 'lapdog', 'eager', 'routine', 'wall', 'bush', 'mixer'], 8: ['exception', 'coil', 'yoyo', 'relieved', 'command', 'timpani', 'manager', 'judicious'], 9: ['tassel', 'papa', 'sofa', 'inside', 'load', 'signal', 'grotesque', 'harald'], 10: ['grid', 'antennae', 'hum', 'preservation', 'congo', 'danger', 'roof', 'shoulder'], 11: ['ivory', 'horde', 'high-rise', 'bullet', 'art', 'concept', 'tattoo', 'cynic'], 12: ['matter', 'dishwasher', 'voter', 'codling', 'sauce', 'waterfront', 'desire', 'strait'], 13: ['abounding', 'equality', 'cirrus', 'sightseeing', 'kiwi', 'theory', 'institute', 'mousse'], 14: ['garment', 'general', 'map', 'unify', 'attack', 'bridge', 'panty', 'large'], 15: ['fratricide', 'chutney', 'laboratory', 'dynamo', 'auto', 'agriculture', 'octet', 'addiction'], 16: ['communicant', 'psychoanalyst', 'happy', 'polish', 'heyday', 'event', 'connection', 'julienne'], 17: ['sleep', 'gelatin', 'leveret', 'bondsman', 'walking', 'blade', 'saving', 'legal'], 18: ['pickle', 'polo', 'thing', 'jeweller', 'world', 'knock', 'lush', 'code'], 19: ['important', 'everything', 'rumor', 'war', 'deed', 'rationale', 'aromatic', 'semantics'], 20: ['grove', 'canoe', 'producer', 'caliber', 'trove', 'stupid', 'pinafore', 'pathetic'], 21: ['clutch', 'tray', 'espalier', 'rainmaker', 'metaphor', 'deathwatch', 'domain', 'twitter'], 22: ['sitar', 'concert', 'dogsled', 'adhesive', 'nut', 'soliloquy', 'organization', 'transaction'], 23: ['magnet', 'corner', 'photo', 'wreck', 'reading', 'genetics', 'vanish', 'cart']}
    expected = {(10, 'antennae', 'shoulder'), (7, 'beset', 'wall'), (5, 'attendant', 'sunday'), (15, 'addiction', 'octet'), (19, 'aromatic', 'war'), (3, 'dissonance', 'tribe'), (16, 'communicant', 'psychoanalyst'), (11, 'art', 'tattoo'), (9, 'grotesque', 'tassel'), (12, 'codling', 'waterfront'), (17, 'blade', 'walking'), (20, 'caliber', 'trove'), (14, 'attack', 'unify'), (1, 'apricot', 'sunglasses'), (4, 'album', 'tic'), (18, 'code', 'world'), (22, 'adhesive', 'transaction'), (23, 'cart', 'wreck'), (6, 'extract', 'validity'), (2, 'cleft', 'try'), (13, 'abounding', 'theory'), (8, 'coil', 'yoyo'), (21, 'clutch', 'twitter')}
    '''
    D = {1: ['mortal', 'pint', 'glasses', 'overheard', 'sunglasses', 'apricot', 'lid', 'stupidity'], 2: ['itch', 'try', 'encouraging', 'ray', 'cleft', 'great-grandfather', 'hate', 'selective'], 3: ['seeker', 'executive', 'hydraulics', 'incarnation', 'dissonance', 'pheasant', 'tribe', 'medication'], 4: ['perfume', 'tic', 'melon', 'album', 'son', 'comfort', 'hearsay', 'robotics'], 5: ['gutter', 'become', 'minimalism', 'spyglass', 'attendant', 'sled', 'skyscraper', 'sunday'], 6: ['lieu', 'ordination', 'extract', 'navigate', 'revolution', 'validity', 'repayment', 'schnitzel'], 7: ['moonlight', 'beset', 'lapdog', 'eager', 'routine', 'wall', 'bush', 'mixer'], 8: ['exception', 'coil', 'yoyo', 'relieved', 'command', 'timpani', 'manager', 'judicious'], 9: ['tassel', 'papa', 'sofa', 'inside', 'load', 'signal', 'grotesque', 'harald'], 10: ['grid', 'antennae', 'hum', 'preservation', 'congo', 'danger', 'roof', 'shoulder'], 11: ['ivory', 'horde', 'high-rise', 'bullet', 'art', 'concept', 'tattoo', 'cynic'], 12: ['matter', 'dishwasher', 'voter', 'codling', 'sauce', 'waterfront', 'desire', 'strait'], 13: ['abounding', 'equality', 'cirrus', 'sightseeing', 'kiwi', 'theory', 'institute', 'mousse'], 14: ['garment', 'general', 'map', 'unify', 'attack', 'bridge', 'panty', 'large'], 15: ['fratricide', 'chutney', 'laboratory', 'dynamo', 'auto', 'agriculture', 'octet', 'addiction'], 16: ['communicant', 'psychoanalyst', 'happy', 'polish', 'heyday', 'event', 'connection', 'julienne'], 17: ['sleep', 'gelatin', 'leveret', 'bondsman', 'walking', 'blade', 'saving', 'legal'], 18: ['pickle', 'polo', 'thing', 'jeweller', 'world', 'knock', 'lush', 'code'], 19: ['important', 'everything', 'rumor', 'war', 'deed', 'rationale', 'aromatic', 'semantics'], 20: ['grove', 'canoe', 'producer', 'caliber', 'trove', 'stupid', 'pinafore', 'pathetic'], 21: ['clutch', 'tray', 'espalier', 'rainmaker', 'metaphor', 'deathwatch', 'domain', 'twitter'], 22: ['sitar', 'concert', 'dogsled', 'adhesive', 'nut', 'soliloquy', 'organization', 'transaction'], 23: ['magnet', 'corner', 'photo', 'wreck', 'reading', 'genetics', 'vanish', 'cart']}
    expected = {(10, 'antennae', 'shoulder'), (7, 'beset', 'wall'), (5, 'attendant', 'sunday'), (15, 'addiction', 'octet'), (19, 'aromatic', 'war'), (3, 'dissonance', 'tribe'), (16, 'communicant', 'psychoanalyst'), (11, 'art', 'tattoo'), (9, 'grotesque', 'tassel'), (12, 'codling', 'waterfront'), (17, 'blade', 'walking'), (20, 'caliber', 'trove'), (14, 'attack', 'unify'), (1, 'apricot', 'sunglasses'), (4, 'album', 'tic'), (18, 'code', 'world'), (22, 'adhesive', 'transaction'), (23, 'cart', 'wreck'), (6, 'extract', 'validity'), (2, 'cleft', 'try'), (13, 'abounding', 'theory'), (8, 'coil', 'yoyo'), (21, 'clutch', 'twitter')}
    return do_func2_tests(D, expected)

def test_func2_4(run=True):
    '''
    D = {1: ['penicillin', 'washcloth', 'yoyo', 'voice', 'optimist', 'republic', 'adventurous', 'scare', 'dust', 'bathrobe', 'guest', 'cycle', 'install', 'self-esteem', 'accordance'], 2: ['vampire', 'chronometer', 'hawk', 'object', 'ossified', 'county', 'silkworm', 'liquor', 'body', 'information', 'date', 'discipline', 'phenomenon', 'farrow', 'grove'], 3: ['storey', 'skywalk', 'ptarmigan', 'proximal', 'mariachi', 'sharp', 'internet', 'founder', 'fedelini', 'uneven', 'parser', 'orientation', 'advise', 'sincere', 'universe'], 4: ['interval', 'sun', 'give', 'destroy', 'train', 'booking', 'bricklaying', 'agonizing', 'hashtag', 'thousand', 'wary', 'pince-nez', 'generator', 'font', 'tote'], 5: ['nestmate', 'prejudice', 'respond', 'pioneer', 'bibliography', 'pig', 'congo', 'climate', 'tremor', 'interferometer', 'icon', 'overcome', 'bran', 'resonant', 'hospitable'], 6: ['album', 'metallurgist', 'pub', 'pomegranate', 'manor', 'pith', 'investor', 'pull', 'tender', 'misty', 'basics', 'monitoring', 'necktie', 'mind', 'agency'], 7: ['zebrafish', 'reporting', 'humor', 'sweatshirt', 'similarity', 'version', 'employment', 'ark', 'vampire', 'participant', 'senator', 'expansionism', 'pajamas', 'anesthesiologist', 'jam'], 8: ['vibe', 'earplug', 'deceive', 'philosophy', 'uplift', 'sexuality', 'loneliness', 'cenotaph', 'bread', 'machine', 'disclaimer', 'oxford', 'crude', 'schooner', 'behest'], 9: ['addiction', 'invincible', 'contain', 'woodwind', 'instruct', 'eyeliner', 'continuity', 'negligee', 'plaster', 'cormorant', 'decade', 'anarchy', 'medium', 'trip', 'lung'], 10: ['rating', 'rehospitalisation', 'study', 'indication', 'destroyer', 'falling-out', 'chubby', 'election', 'monasticism', 'everything', 'half-sister', 'ritzy', 'robot', 'moonscape', 'exhaust'], 11: ['tabulate', 'wave', 'fascinated', 'tomato', 'beastie', 'boulder', 'specialist', 'draconian', 'parka', 'bather', 'milkshake', 'electronics', 'bucket', 'corner', 'sword'], 12: ['slider', 'tenuous', 'boundary', 'cut', 'processing', 'proportion', 'mascara', 'clap', 'dimension', 'snorer', 'ginger', 'correspondent', 'motivate', 'mundane', 'notation'], 13: ['sorghum', 'exocrine', 'bustle', 'steamroller', 'shawl', 'overweight', 'knife-edge', 'tangerine', 'husband', 'trash', 'aside', 'rainstorm', 'purpose', 'grenade', 'sad'], 14: ['congress', 'gaming', 'recognize', 'chauvinist', 'verdant', 'woozy', 'get', 'vice', 'birth', 'bitter', 'underclothes', 'bother', 'aftermath', 'downforce', 'sundae'], 15: ['anything', 'jeweller', 'neon', 'field', 'affinity', 'pressurization', 'monkey', 'redirect', 'melatonin', 'mayor', 'adventurous', 'termite', 'crunch', 'thirst', 'expansion'], 16: ['zombie', 'violin', 'baseball', 'jockey', 'curl', 'anarchy', 'heron', 'croissant', 'shallot', 'mistake', 'landform', 'accusation', 'hoe', 'magical', 'tournament'], 17: ['dining', 'morphology', 'destroy', 'eminent', 'perpendicular', 'adoption', 'aquarium', 'consolidate', 'tacit', 'oak', 'triangle', 'nick', 'aquifer', 'pepperoni', 'meat'], 18: ['lottery', 'principal', 'hypothesize', 'loggia', 'health', 'phenomenon', 'tambourine', 'versed', 'chalice', 'abnormal', 'tripod', 'gravy', 'frog', 'everybody', 'broom'], 19: ['chronograph', 'e-mail', 'saloon', 'freezing', 'locust', 'proceedings', 'grip', 'name', 'bond', 'mentor', 'fishnet', 'price', 'cement', 'adapter', 'quixotic'], 20: ['representation', 'congo', 'nutmeg', 'unibody', 'pull', 'ruler', 'abacus', 'upbeat', 'screeching', 'astronomy', 'year', 'trumpet', 'cowbell', 'woebegone', 'hare'], 21: ['julienne', 'communicate', 'neighborhood', 'dashing', 'monastery', 'fit', 'boundless', 'reduction', 'hare', 'spork', 'flippant', 'aloof', 'cape', 'scarecrow', 'phone'], 22: ['gumshoe', 'dial', 'aim', 'crazy', 'remains', 'expose', 'ill', 'cooing', 'system', 'proximal', 'brassiere', 'ferret', 'horse', 'help', 'perpetual'], 23: ['might', 'toothbrush', 'octagon', 'cliff', 'detour', 'carve', 'hedge', 'manufacturing', 'slipper', 'pouch', 'grouper', 'authorization', 'sanction', 'prey', 'marines'], 24: ['spread', 'grocery', 'storage', 'float', 'embryo', 'reinforce', 'synonymous', 'herb', 'momentous', 'sideboard', 'mere', 'joke', 'almighty', 'underpass', 'brandy'], 25: ['squirrel', 'composition', 'timer', 'spin', 'dazzling', 'quinoa', 'plate', 'laboratory', 'lieutenant', 'soprano', 'honesty', 'soliloquy', 'test', 'ferret', 'garden'], 26: ['encirclement', 'cyst', 'toffee', 'monastery', 'dickey', 'working', 'objection', 'daffodil', 'anthropology', 'boyhood', 'chili', 'march', 'glider', 'lapdog', 'mustache'], 27: ['decoration', 'examiner', 'rot', 'joke', 'wolf', 'moment', 'freak', 'peaceful', 'tavern', 'curd', 'belligerent', 'slider', 'keep', 'basin', 'deathwatch'], 28: ['contest', 'challenge', 'suppression', 'teacher', 'shoreline', 'tablet', 'anything', 'ceramic', 'gifted', 'unadvised', 'exclamation', 'copying', 'employment', 'fantasy', 'hold'], 29: ['meek', 'wet-bar', 'woman', 'step-son', 'captain', 'reproduce', 'purchase', 'clipboard', 'reach', 'aggressive', 'wetsuit', 'series', 'tonic', 'warmth', 'trunk'], 30: ['yeast', 'directory', 'precision', 'year', 'hear', 'reply', 'artichoke', 'barrage', 'allegation', 'centurion', 'noodles', 'present', 'screw', 'calico', 'diaphragm'], 31: ['handrail', 'moustache', 'bank', 'exuberant', 'dressing', 'watchful', 'accident', 'stitcher', 'majority', 'resolute', 'pastor', 'arrangement', 'trail', 'counterpart', 'politics'], 32: ['edition', 'symbol', 'omniscient', 'chiffonier', 'gearshift', 'epithelium', 'rumor', 'illustrate', 'knit', 'kindhearted', 'destruction', 'nectarine', 'room', 'numberless', 'container'], 33: ['cell', 'lad', 'park', 'enforce', 'goose', 'toothpaste', 'curtailment', 'course', 'activation', 'hypnotic', 'pyridine', 'moccasins', 'con', 'tense', 'presidency'], 34: ['hierarchy', 'slider', 'impala', 'cup', 'diagram', 'savings', 'off-ramp', 'examination', 'onerous', 'measly', 'gaiters', 'dispatch', 'menopause', 'ludicrous', 'violet'], 35: ['kitten', 'innate', 'calm', 'rhetorical', 'birdbath', 'commercial', 'steeple', 'infant', 'describe', 'dipstick', 'expect', 'sweep', 'dissemination', 'civilian', 'kill'], 36: ['parcel', 'beg', 'apse', 'mentor', 'section', 'takeover', 'say', 'folk', 'window', 'gravy', 'hobbit', 'temporary', 'brash', 'abolishment', 'toot'], 37: ['pink', 'dawn', 'danger', 'eddy', 'transplantation', 'overload', 'linkage', 'jodhpurs', 'hunting', 'trip', 'hedge', 'music', 'jazzy', 'partnership', 'speech'], 38: ['precious', 'condemned', 'nit', 'alto', 'interval', 'daybed', 'comfortable', 'sunday', 'retrospectivity', 'mapping', 'cholesterol', 'tan', 'machinery', 'tremor', 'determine'], 39: ['lace', 'shipping', 'lawsuit', 'maelstrom', 'zephyr', 'metro', 'anime', 'neonate', 'hyphenation', 'cheek', 'ambience', 'corduroy', 'commandment', 'conductor', 'ironclad'], 40: ['tensor', 'bottle', 'labored', 'jaded', 'puzzled', 'zoom', 'park', 'raft', 'moon', 'diffuse', 'custom', 'subcomponent', 'basket', 'silk', 'magazine'], 41: ['sale', 'parser', 'bark', 'browsing', 'music-making', 'husband', 'block', 'congressman', 'bear', 'inquisitive', 'watchmaker', 'cricketer', 'journey', 'crush', 'win'], 42: ['communist', 'bare', 'infrastructure', 'nutrient', 'construction', 'tomb', 'telescreen', 'honorable', 'funeral', 'meantime', 'therapist', 'remote', 'seaweed', 'armour', 'diploma'], 43: ['tenth', 'colt', 'building', 'production', 'odd', 'diagnose', 'opportunist', 'barbecue', 'transportation', 'wiry', 'ceiling', 'basketball', 'expose', 'audit', 'cloth'], 44: ['postage', 'endoderm', 'thermometer', 'prison', 'balloon', 'nutrient', 'epee', 'pavilion', 'justify', 'gold', 'deserted', 'assessment', 'blowgun', 'background', 'estrogen']}
    expected = {(42, 'armour', 'tomb'), (4, 'agonizing', 'wary'), (29, 'aggressive', 'woman'), (30, 'allegation', 'yeast'), (35, 'birdbath', 'sweep'), (40, 'basket', 'zoom'), (25, 'composition', 'timer'), (20, 'abacus', 'year'), (17, 'adoption', 'triangle'), (36, 'abolishment', 'window'), (21, 'aloof', 'spork'), (38, 'alto', 'tremor'), (14, 'aftermath', 'woozy'), (5, 'bibliography', 'tremor'), (9, 'addiction', 'woodwind'), (22, 'aim', 'system'), (11, 'bather', 'wave'), (12, 'boundary', 'tenuous'), (10, 'chubby', 'study'), (16, 'accusation', 'zombie'), (24, 'almighty', 'underpass'), (2, 'body', 'vampire'), (3, 'advise', 'universe'), (7, 'anesthesiologist', 'zebrafish'), (37, 'danger', 'trip'), (1, 'accordance', 'yoyo'), (15, 'adventurous', 'thirst'), (27, 'basin', 'wolf'), (31, 'accident', 'watchful'), (43, 'audit', 'wiry'), (6, 'agency', 'tender'), (23, 'authorization', 'toothbrush'), (19, 'adapter', 'saloon'), (26, 'anthropology', 'working'), (34, 'cup', 'violet'), (44, 'assessment', 'thermometer'), (41, 'bark', 'win'), (18, 'abnormal', 'versed'), (33, 'activation', 'toothpaste'), (32, 'chiffonier', 'symbol'), (8, 'behest', 'vibe'), (39, 'ambience', 'zephyr'), (28, 'anything', 'unadvised'), (13, 'aside', 'trash')}
    '''
    D = {1: ['penicillin', 'washcloth', 'yoyo', 'voice', 'optimist', 'republic', 'adventurous', 'scare', 'dust', 'bathrobe', 'guest', 'cycle', 'install', 'self-esteem', 'accordance'], 2: ['vampire', 'chronometer', 'hawk', 'object', 'ossified', 'county', 'silkworm', 'liquor', 'body', 'information', 'date', 'discipline', 'phenomenon', 'farrow', 'grove'], 3: ['storey', 'skywalk', 'ptarmigan', 'proximal', 'mariachi', 'sharp', 'internet', 'founder', 'fedelini', 'uneven', 'parser', 'orientation', 'advise', 'sincere', 'universe'], 4: ['interval', 'sun', 'give', 'destroy', 'train', 'booking', 'bricklaying', 'agonizing', 'hashtag', 'thousand', 'wary', 'pince-nez', 'generator', 'font', 'tote'], 5: ['nestmate', 'prejudice', 'respond', 'pioneer', 'bibliography', 'pig', 'congo', 'climate', 'tremor', 'interferometer', 'icon', 'overcome', 'bran', 'resonant', 'hospitable'], 6: ['album', 'metallurgist', 'pub', 'pomegranate', 'manor', 'pith', 'investor', 'pull', 'tender', 'misty', 'basics', 'monitoring', 'necktie', 'mind', 'agency'], 7: ['zebrafish', 'reporting', 'humor', 'sweatshirt', 'similarity', 'version', 'employment', 'ark', 'vampire', 'participant', 'senator', 'expansionism', 'pajamas', 'anesthesiologist', 'jam'], 8: ['vibe', 'earplug', 'deceive', 'philosophy', 'uplift', 'sexuality', 'loneliness', 'cenotaph', 'bread', 'machine', 'disclaimer', 'oxford', 'crude', 'schooner', 'behest'], 9: ['addiction', 'invincible', 'contain', 'woodwind', 'instruct', 'eyeliner', 'continuity', 'negligee', 'plaster', 'cormorant', 'decade', 'anarchy', 'medium', 'trip', 'lung'], 10: ['rating', 'rehospitalisation', 'study', 'indication', 'destroyer', 'falling-out', 'chubby', 'election', 'monasticism', 'everything', 'half-sister', 'ritzy', 'robot', 'moonscape', 'exhaust'], 11: ['tabulate', 'wave', 'fascinated', 'tomato', 'beastie', 'boulder', 'specialist', 'draconian', 'parka', 'bather', 'milkshake', 'electronics', 'bucket', 'corner', 'sword'], 12: ['slider', 'tenuous', 'boundary', 'cut', 'processing', 'proportion', 'mascara', 'clap', 'dimension', 'snorer', 'ginger', 'correspondent', 'motivate', 'mundane', 'notation'], 13: ['sorghum', 'exocrine', 'bustle', 'steamroller', 'shawl', 'overweight', 'knife-edge', 'tangerine', 'husband', 'trash', 'aside', 'rainstorm', 'purpose', 'grenade', 'sad'], 14: ['congress', 'gaming', 'recognize', 'chauvinist', 'verdant', 'woozy', 'get', 'vice', 'birth', 'bitter', 'underclothes', 'bother', 'aftermath', 'downforce', 'sundae'], 15: ['anything', 'jeweller', 'neon', 'field', 'affinity', 'pressurization', 'monkey', 'redirect', 'melatonin', 'mayor', 'adventurous', 'termite', 'crunch', 'thirst', 'expansion'], 16: ['zombie', 'violin', 'baseball', 'jockey', 'curl', 'anarchy', 'heron', 'croissant', 'shallot', 'mistake', 'landform', 'accusation', 'hoe', 'magical', 'tournament'], 17: ['dining', 'morphology', 'destroy', 'eminent', 'perpendicular', 'adoption', 'aquarium', 'consolidate', 'tacit', 'oak', 'triangle', 'nick', 'aquifer', 'pepperoni', 'meat'], 18: ['lottery', 'principal', 'hypothesize', 'loggia', 'health', 'phenomenon', 'tambourine', 'versed', 'chalice', 'abnormal', 'tripod', 'gravy', 'frog', 'everybody', 'broom'], 19: ['chronograph', 'e-mail', 'saloon', 'freezing', 'locust', 'proceedings', 'grip', 'name', 'bond', 'mentor', 'fishnet', 'price', 'cement', 'adapter', 'quixotic'], 20: ['representation', 'congo', 'nutmeg', 'unibody', 'pull', 'ruler', 'abacus', 'upbeat', 'screeching', 'astronomy', 'year', 'trumpet', 'cowbell', 'woebegone', 'hare'], 21: ['julienne', 'communicate', 'neighborhood', 'dashing', 'monastery', 'fit', 'boundless', 'reduction', 'hare', 'spork', 'flippant', 'aloof', 'cape', 'scarecrow', 'phone'], 22: ['gumshoe', 'dial', 'aim', 'crazy', 'remains', 'expose', 'ill', 'cooing', 'system', 'proximal', 'brassiere', 'ferret', 'horse', 'help', 'perpetual'], 23: ['might', 'toothbrush', 'octagon', 'cliff', 'detour', 'carve', 'hedge', 'manufacturing', 'slipper', 'pouch', 'grouper', 'authorization', 'sanction', 'prey', 'marines'], 24: ['spread', 'grocery', 'storage', 'float', 'embryo', 'reinforce', 'synonymous', 'herb', 'momentous', 'sideboard', 'mere', 'joke', 'almighty', 'underpass', 'brandy'], 25: ['squirrel', 'composition', 'timer', 'spin', 'dazzling', 'quinoa', 'plate', 'laboratory', 'lieutenant', 'soprano', 'honesty', 'soliloquy', 'test', 'ferret', 'garden'], 26: ['encirclement', 'cyst', 'toffee', 'monastery', 'dickey', 'working', 'objection', 'daffodil', 'anthropology', 'boyhood', 'chili', 'march', 'glider', 'lapdog', 'mustache'], 27: ['decoration', 'examiner', 'rot', 'joke', 'wolf', 'moment', 'freak', 'peaceful', 'tavern', 'curd', 'belligerent', 'slider', 'keep', 'basin', 'deathwatch'], 28: ['contest', 'challenge', 'suppression', 'teacher', 'shoreline', 'tablet', 'anything', 'ceramic', 'gifted', 'unadvised', 'exclamation', 'copying', 'employment', 'fantasy', 'hold'], 29: ['meek', 'wet-bar', 'woman', 'step-son', 'captain', 'reproduce', 'purchase', 'clipboard', 'reach', 'aggressive', 'wetsuit', 'series', 'tonic', 'warmth', 'trunk'], 30: ['yeast', 'directory', 'precision', 'year', 'hear', 'reply', 'artichoke', 'barrage', 'allegation', 'centurion', 'noodles', 'present', 'screw', 'calico', 'diaphragm'], 31: ['handrail', 'moustache', 'bank', 'exuberant', 'dressing', 'watchful', 'accident', 'stitcher', 'majority', 'resolute', 'pastor', 'arrangement', 'trail', 'counterpart', 'politics'], 32: ['edition', 'symbol', 'omniscient', 'chiffonier', 'gearshift', 'epithelium', 'rumor', 'illustrate', 'knit', 'kindhearted', 'destruction', 'nectarine', 'room', 'numberless', 'container'], 33: ['cell', 'lad', 'park', 'enforce', 'goose', 'toothpaste', 'curtailment', 'course', 'activation', 'hypnotic', 'pyridine', 'moccasins', 'con', 'tense', 'presidency'], 34: ['hierarchy', 'slider', 'impala', 'cup', 'diagram', 'savings', 'off-ramp', 'examination', 'onerous', 'measly', 'gaiters', 'dispatch', 'menopause', 'ludicrous', 'violet'], 35: ['kitten', 'innate', 'calm', 'rhetorical', 'birdbath', 'commercial', 'steeple', 'infant', 'describe', 'dipstick', 'expect', 'sweep', 'dissemination', 'civilian', 'kill'], 36: ['parcel', 'beg', 'apse', 'mentor', 'section', 'takeover', 'say', 'folk', 'window', 'gravy', 'hobbit', 'temporary', 'brash', 'abolishment', 'toot'], 37: ['pink', 'dawn', 'danger', 'eddy', 'transplantation', 'overload', 'linkage', 'jodhpurs', 'hunting', 'trip', 'hedge', 'music', 'jazzy', 'partnership', 'speech'], 38: ['precious', 'condemned', 'nit', 'alto', 'interval', 'daybed', 'comfortable', 'sunday', 'retrospectivity', 'mapping', 'cholesterol', 'tan', 'machinery', 'tremor', 'determine'], 39: ['lace', 'shipping', 'lawsuit', 'maelstrom', 'zephyr', 'metro', 'anime', 'neonate', 'hyphenation', 'cheek', 'ambience', 'corduroy', 'commandment', 'conductor', 'ironclad'], 40: ['tensor', 'bottle', 'labored', 'jaded', 'puzzled', 'zoom', 'park', 'raft', 'moon', 'diffuse', 'custom', 'subcomponent', 'basket', 'silk', 'magazine'], 41: ['sale', 'parser', 'bark', 'browsing', 'music-making', 'husband', 'block', 'congressman', 'bear', 'inquisitive', 'watchmaker', 'cricketer', 'journey', 'crush', 'win'], 42: ['communist', 'bare', 'infrastructure', 'nutrient', 'construction', 'tomb', 'telescreen', 'honorable', 'funeral', 'meantime', 'therapist', 'remote', 'seaweed', 'armour', 'diploma'], 43: ['tenth', 'colt', 'building', 'production', 'odd', 'diagnose', 'opportunist', 'barbecue', 'transportation', 'wiry', 'ceiling', 'basketball', 'expose', 'audit', 'cloth'], 44: ['postage', 'endoderm', 'thermometer', 'prison', 'balloon', 'nutrient', 'epee', 'pavilion', 'justify', 'gold', 'deserted', 'assessment', 'blowgun', 'background', 'estrogen']}
    expected = {(42, 'armour', 'tomb'), (4, 'agonizing', 'wary'), (29, 'aggressive', 'woman'), (30, 'allegation', 'yeast'), (35, 'birdbath', 'sweep'), (40, 'basket', 'zoom'), (25, 'composition', 'timer'), (20, 'abacus', 'year'), (17, 'adoption', 'triangle'), (36, 'abolishment', 'window'), (21, 'aloof', 'spork'), (38, 'alto', 'tremor'), (14, 'aftermath', 'woozy'), (5, 'bibliography', 'tremor'), (9, 'addiction', 'woodwind'), (22, 'aim', 'system'), (11, 'bather', 'wave'), (12, 'boundary', 'tenuous'), (10, 'chubby', 'study'), (16, 'accusation', 'zombie'), (24, 'almighty', 'underpass'), (2, 'body', 'vampire'), (3, 'advise', 'universe'), (7, 'anesthesiologist', 'zebrafish'), (37, 'danger', 'trip'), (1, 'accordance', 'yoyo'), (15, 'adventurous', 'thirst'), (27, 'basin', 'wolf'), (31, 'accident', 'watchful'), (43, 'audit', 'wiry'), (6, 'agency', 'tender'), (23, 'authorization', 'toothbrush'), (19, 'adapter', 'saloon'), (26, 'anthropology', 'working'), (34, 'cup', 'violet'), (44, 'assessment', 'thermometer'), (41, 'bark', 'win'), (18, 'abnormal', 'versed'), (33, 'activation', 'toothpaste'), (32, 'chiffonier', 'symbol'), (8, 'behest', 'vibe'), (39, 'ambience', 'zephyr'), (28, 'anything', 'unadvised'), (13, 'aside', 'trash')}
    return do_func2_tests(D, expected)

################################################################################

def do_func3_tests(L1, L2, expected):
    res = program.func3(L1, L2)
    testlib.check_val(res, expected)
    return 0.5


def test_func3_1(run=True):
    '''
    L1 = ['casa', 'gatto', 'cane', 'oca', 'elefante']
    L2 = ['paperino', 'cane', 'gatto', 'ragno', 'topo', 'cip', 'map']
    expected = {'elefante': {'paperino'}, 'oca': {'cip', 'map'}, 'casa': {'topo'}}
    '''
    L1 = ['casa', 'gatto', 'cane', 'oca', 'elefante']
    L2 = ['paperino', 'cane', 'gatto', 'ragno', 'topo', 'cip', 'map']
    expected = {'elefante': {'paperino'}, 'oca': {'cip', 'map'}, 'casa': {'topo'}}
    return do_func3_tests(L1, L2, expected)

def test_func3_2(run=True):
    '''
    L1 = ['oat', 'jute', 'itch', 'recliner', 'waistband', 'spiral', 'debate', 'guacamole', 'inspection', 'torte', 'quack', 'constellation', 'health', 'diamond', 'minority', 'postbox', 'browser', 'reminiscent', 'remove', 'fanatical']
    L2 = ['spiral', 'torte', 'touch', 'browser', 'leash', 'critique', 'primary', 'quack', 'junket', 'waistband', 'remove', 'debate', 'pottery', 'jute', 'complete', 'constellation', 'armor', 'diamond', 'enacted', 'lewd']
    expected = {'inspection': set(), 'oat': set(), 'guacamole': set(), 'reminiscent': set(), 'recliner': {'complete', 'critique'}, 'itch': {'lewd'}, 'health': {'junket'}, 'minority': {'complete', 'critique'}, 'postbox': {'primary', 'enacted', 'pottery'}, 'fanatical': set()}
    '''
    L1 = ['oat', 'jute', 'itch', 'recliner', 'waistband', 'spiral', 'debate', 'guacamole', 'inspection', 'torte', 'quack', 'constellation', 'health', 'diamond', 'minority', 'postbox', 'browser', 'reminiscent', 'remove', 'fanatical']
    L2 = ['spiral', 'torte', 'touch', 'browser', 'leash', 'critique', 'primary', 'quack', 'junket', 'waistband', 'remove', 'debate', 'pottery', 'jute', 'complete', 'constellation', 'armor', 'diamond', 'enacted', 'lewd']
    expected = {'inspection': set(), 'oat': set(), 'guacamole': set(), 'reminiscent': set(), 'recliner': {'complete', 'critique'}, 'itch': {'lewd'}, 'health': {'junket'}, 'minority': {'complete', 'critique'}, 'postbox': {'primary', 'enacted', 'pottery'}, 'fanatical': set()}
    return do_func3_tests(L1, L2, expected)

def test_func3_3(run=True):
    '''
    L1 = ['turmeric', 'establish', 'axis', 'eliminate', 'sew', 'altar', 'waterskiing', 'meddle', 'survival', 'colloquy', 'zebrafish', 'bizarre', 'curtain', 'match', 'ham', 'track', 'humanity', 'crude', 'alive', 'investigation', 'script', 'passport', 'cohort', 'breakfast', 'sting', 'wrong', 'whimsical', 'restructure', 'deodorant', 'Early']
    L2 = ['script', 'font', 'riverbed', 'zoology', 'bizarre', 'eliminate', 'altar', 'repulsive', 'Early', 'breakfast', 'match', 'curtain', 'meddle', 'husky', 'ham', 'survival', 'axis', 'autumn', 'camp', 'gun', 'income', 'hint', 'dilapidation', 'mug', 'whimsical', 'horde', 'cohort', 'lighten', 'land', 'turmeric']
    expected = {'colloquy': {'riverbed'}, 'crude': {'husky', 'horde'}, 'sew': {'mug', 'gun'}, 'zebrafish': {'repulsive'}, 'track': {'husky', 'horde'}, 'humanity': {'riverbed'}, 'restructure': set(), 'passport': {'riverbed'}, 'wrong': {'husky', 'horde'}, 'alive': {'husky', 'horde'}, 'establish': {'repulsive'}, 'investigation': set(), 'sting': {'husky', 'horde'}, 'waterskiing': set(), 'deodorant': {'repulsive'}}
    '''
    L1 = ['turmeric', 'establish', 'axis', 'eliminate', 'sew', 'altar', 'waterskiing', 'meddle', 'survival', 'colloquy', 'zebrafish', 'bizarre', 'curtain', 'match', 'ham', 'track', 'humanity', 'crude', 'alive', 'investigation', 'script', 'passport', 'cohort', 'breakfast', 'sting', 'wrong', 'whimsical', 'restructure', 'deodorant', 'Early']
    L2 = ['script', 'font', 'riverbed', 'zoology', 'bizarre', 'eliminate', 'altar', 'repulsive', 'Early', 'breakfast', 'match', 'curtain', 'meddle', 'husky', 'ham', 'survival', 'axis', 'autumn', 'camp', 'gun', 'income', 'hint', 'dilapidation', 'mug', 'whimsical', 'horde', 'cohort', 'lighten', 'land', 'turmeric']
    expected = {'colloquy': {'riverbed'}, 'crude': {'husky', 'horde'}, 'sew': {'mug', 'gun'}, 'zebrafish': {'repulsive'}, 'track': {'husky', 'horde'}, 'humanity': {'riverbed'}, 'restructure': set(), 'passport': {'riverbed'}, 'wrong': {'husky', 'horde'}, 'alive': {'husky', 'horde'}, 'establish': {'repulsive'}, 'investigation': set(), 'sting': {'husky', 'horde'}, 'waterskiing': set(), 'deodorant': {'repulsive'}}
    return do_func3_tests(L1, L2, expected)

def test_func3_4(run=True):
    '''
    L1 = ['convention', 'mankind', 'thrust', 'row', 'flanker', 'clammy', 'captor', 'samurai', 'dissemination', 'implication', 'briefing', 'price', 'echidna', 'lynx', 'iceberg', 'secure', 'husband', 'zephyr', 'rot', 'changeable', 'clarinet', 'steak', 'display', 'raiment', 'extract', 'pink', 'ring', 'iron', 'rely', 'tall', 'feeding', 'information', 'formula', 'confusion', 'arithmetic', 'persimmon', 'broad', 'shakedown', 'accomplishment', 'learning']
    L2 = ['clammy', 'briefing', 'rot', 'shakedown', 'mankind', 'changeable', 'flanker', 'presentation', 'sonata', 'tilt', 'dissemination', 'row', 'knee', 'display', 'vicinity', 'tugboat', 'chili', 'creep', 'iceberg', 'supply', 'rate', 'category', 'rely', 'extract', 'clarinet', 'knuckle', 'convention', 'erratic', 'telling', 'wok', 'arithmetic', 'captor', 'flanker', 'addition', 'ring', 'information', 'journey', 'reign', 'hospice', 'broad']
    expected = {'thrust': {'sonata', 'supply'}, 'pink': {'tilt', 'rate', 'knee'}, 'confusion': set(), 'accomplishment': set(), 'secure': {'sonata', 'supply'}, 'echidna': {'erratic', 'telling', 'tugboat', 'hospice', 'journey', 'knuckle'}, 'learning': {'category', 'vicinity', 'addition'}, 'husband': {'erratic', 'telling', 'tugboat', 'hospice', 'journey', 'knuckle'}, 'iron': {'tilt', 'rate', 'knee'}, 'persimmon': set(), 'samurai': {'erratic', 'telling', 'tugboat', 'hospice', 'journey', 'knuckle'}, 'implication': set(), 'formula': {'erratic', 'telling', 'tugboat', 'hospice', 'journey', 'knuckle'}, 'price': {'creep', 'chili', 'reign'}, 'zephyr': {'sonata', 'supply'}, 'raiment': {'erratic', 'telling', 'tugboat', 'hospice', 'journey', 'knuckle'}, 'tall': {'tilt', 'rate', 'knee'}, 'feeding': {'erratic', 'telling', 'tugboat', 'hospice', 'journey', 'knuckle'}, 'lynx': {'tilt', 'rate', 'knee'}, 'steak': {'creep', 'chili', 'reign'}}
    '''
    L1 = ['convention', 'mankind', 'thrust', 'row', 'flanker', 'clammy', 'captor', 'samurai', 'dissemination', 'implication', 'briefing', 'price', 'echidna', 'lynx', 'iceberg', 'secure', 'husband', 'zephyr', 'rot', 'changeable', 'clarinet', 'steak', 'display', 'raiment', 'extract', 'pink', 'ring', 'iron', 'rely', 'tall', 'feeding', 'information', 'formula', 'confusion', 'arithmetic', 'persimmon', 'broad', 'shakedown', 'accomplishment', 'learning']
    L2 = ['clammy', 'briefing', 'rot', 'shakedown', 'mankind', 'changeable', 'flanker', 'presentation', 'sonata', 'tilt', 'dissemination', 'row', 'knee', 'display', 'vicinity', 'tugboat', 'chili', 'creep', 'iceberg', 'supply', 'rate', 'category', 'rely', 'extract', 'clarinet', 'knuckle', 'convention', 'erratic', 'telling', 'wok', 'arithmetic', 'captor', 'flanker', 'addition', 'ring', 'information', 'journey', 'reign', 'hospice', 'broad']
    expected = {'thrust': {'sonata', 'supply'}, 'pink': {'tilt', 'rate', 'knee'}, 'confusion': set(), 'accomplishment': set(), 'secure': {'sonata', 'supply'}, 'echidna': {'erratic', 'telling', 'tugboat', 'hospice', 'journey', 'knuckle'}, 'learning': {'category', 'vicinity', 'addition'}, 'husband': {'erratic', 'telling', 'tugboat', 'hospice', 'journey', 'knuckle'}, 'iron': {'tilt', 'rate', 'knee'}, 'persimmon': set(), 'samurai': {'erratic', 'telling', 'tugboat', 'hospice', 'journey', 'knuckle'}, 'implication': set(), 'formula': {'erratic', 'telling', 'tugboat', 'hospice', 'journey', 'knuckle'}, 'price': {'creep', 'chili', 'reign'}, 'zephyr': {'sonata', 'supply'}, 'raiment': {'erratic', 'telling', 'tugboat', 'hospice', 'journey', 'knuckle'}, 'tall': {'tilt', 'rate', 'knee'}, 'feeding': {'erratic', 'telling', 'tugboat', 'hospice', 'journey', 'knuckle'}, 'lynx': {'tilt', 'rate', 'knee'}, 'steak': {'creep', 'chili', 'reign'}}
    return do_func3_tests(L1, L2, expected)


# ----------------------------------- Func 4 ----------------------------------- #

def do_func4_tests(ID, expected):
    input_filename  = f'func4/in_{ID}.txt'
    output_filename = f'func4/out_{ID}.txt'
    expected_filename = f'func4/expected_{ID}.txt'
    res = program.func4(input_filename, output_filename)
    testlib.check(res, expected)
    testlib.check_text_file(output_filename, expected_filename)
    return 2

def test_func4_1(run=True):
    '''
    input_filename = 'func4/in_1.txt'
    ouput_filename = 'func4/out_1.txt'
    expected_filename = 'func4/expected_1.txt'
    expected =  (24, 279)
    '''
    ID = 1
    expected = (24, 279)
    return do_func4_tests(ID, expected)

def test_func4_2(run=True):
    '''
    input_filename = 'func4/in_2.txt'
    ouput_filename = 'func4/out_2.txt'
    expected_filename = 'func4/expected_2.txt'
    expected =  (74, 922)
    '''
    ID = 2
    expected = (74, 922)
    return do_func4_tests(ID, expected)


def test_func4_3(run=True):
    '''
    input_filename = 'func4/in_3.txt'
    ouput_filename = 'func4/out_3.txt'
    expected_filename = 'func4/expected_3.txt'
    expected = (114, 1437)
    '''
    ID = 3
    expected = (114, 1437)
    return do_func4_tests(ID, expected)

################################################################################

def do_test_func5(ID, tilesize, expected):
    img_in  = f'func5/in_{ID}.png'
    img_out = f'func5/out_{ID}_{tilesize}.png'
    img_exp = f'func5/expected_{ID}_{tilesize}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run

    res = program.func5(img_in, img_out, tilesize)
    testlib.check_val(res, expected, f'''{'*'*50}\n[ERROR] Il numero di quadretti è sbagliato! / The number of tiles is incorrect.\nReturned={res}, expected={expected}.\n{'*'*50}''')
    testlib.check_img_file(img_out, img_exp)
    return 2


def test_func5_1(run=True):
    '''
    input_png  = 'func5/in_3cime.png', 
    output_png = 'func5/out_3cime_50.png'
    tilesize   = 50
    expected   = 15
    '''
    ID         = '3cime'
    tilesize   = 50
    expected   = 15
    return do_test_func5(ID, tilesize, expected)


def test_func5_2(run=True):
    '''
    input_png  = 'func5/in_3cime.png', 
    output_png = 'func5/out_3cime_13.png'
    tilesize   = 13
    expected   = 294
    '''
    ID         = '3cime'
    tilesize   = 13
    expected   = 294
    return do_test_func5(ID, tilesize, expected)


def test_func5_3(run=True):
    '''
    input_png  = 'func5/in_3cime.png',
    output_png = 'func5/out_3cime_10.png'
    tilesize   = 10
    expected   = 294
    '''
    ID         = '3cime'
    tilesize   = 10
    expected   = 486
    return do_test_func5(ID, tilesize, expected)


def test_func5_4(run=True):
    '''
    input_png  = 'func5/in_3cime.png',
    output_png = 'func5/out_3cime_3.png'
    tilesize   = 3
    expected   = 294
    '''
    ID         = '3cime'
    tilesize   = 3
    expected   = 5460
    return do_test_func5(ID, tilesize, expected)

# ----------------------------------- EX.1 ----------------------------------- #
def do_test_ex1(string, N, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex1(string, N)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex1(string, N)
    testlib.check(res, expected)
    return 2

def test_ex1_1(run=True):
    '''
    string = 'aabca'
    N = 4
    expected {'acba', 'caba', 'acab', 'abac', 'abca', 'baca'}
    '''
    string = 'aabca'
    N = 4
    expected = {'acba', 'caba', 'acab', 'abac', 'abca', 'baca'}
    return do_test_ex1(string, N, expected)

def test_ex1_2(run=True):
    '''
    string = 'aabca'
    N = 5
    expected {'acaba', 'abaca'}
    '''
    string = 'aabca'
    N = 5
    expected = {'acaba', 'abaca'}
    return do_test_ex1(string, N, expected)


def test_ex1_3(run=True):
    '''
    string = 'aabcaCPAffPPCC'
    N = 5
    expected = 	{'adaca', 'adbac', 'adabc', 'bdaca', 'dabca', 'abacd', 'acadb', 'dcaba', 'acabd', 'bcada', 'badac',
    'bacad', 'adbca', 'cabad', 'acdba', 'abadc', 'abcda', 'badca', 'dacab', 'abcad', 'abdac', 'abada', 'adacb', 'cadba',
    'dabac', 'dbaca', 'cadab', 'abdca', 'cabda', 'dacba', 'cdaba', 'acaba', 'abaca', 'adcab', 'bacda', 'adcba', 'acbad',
    'cbada', 'acbda', 'acdab', 'acada', 'adaba'}
    '''
    string = 'aabcaadaaa'
    N = 5
    expected = {'adaca', 'adbac', 'adabc', 'bdaca', 'dabca', 'abacd', 'acadb', 'dcaba', 'acabd', 'bcada', 'badac',
                'bacad', 'adbca', 'cabad', 'acdba', 'abadc', 'abcda', 'badca', 'dacab', 'abcad', 'abdac', 'abada',
                'adacb', 'cadba', 'dabac', 'dbaca', 'cadab', 'abdca', 'cabda', 'dacba', 'cdaba', 'acaba', 'abaca',
                'adcab', 'bacda', 'adcba', 'acbad', 'cbada', 'acbda', 'acdab', 'acada', 'adaba'}
    return do_test_ex1(string, N, expected)

# ----------------------------------- EX. 2----------------------------------- #


def do_ex2_test(root_list, expected, expected_tree_list):
    root1 = tree.BinaryTree.fromList(root_list)
    root2 = tree.BinaryTree.fromList(root_list)
    root3 = tree.BinaryTree.fromList(root_list)
    root_exp = tree.BinaryTree.fromList(expected_tree_list)
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex2(root1)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex2(root2)
    #print(res)
    if res != expected:
        my_print(f'''{'*'*50}\n[ERROR]L'altezza dell'albero ritornata non è corretta! / The returned tree height is incorrect!!\nReturned={res}, expected={expected}''')
        return 0
    if root2 == root3:
        my_print(f'''{'*'*50}\n[ERROR]L'albero non è stato modificato! / The has not be changed at all!!\nReturned={root2}, \nExpected={root_exp}''')
        return 0
    if root2 != root_exp:
        my_print(f'''{'*'*50}\n[ERROR]L'albero non è stato modificato correttamente! / The has not be changed correctly!!\nReturned={root2}, \nExpected={root_exp}''')
        return 0
    return 2


def test_ex2_1(run=True):
    '''
    initial tree:
               6             |
              / \            |
             5   3           |
            /   / \          |
           4   10  6         |
              /   / \        |
             7   8  1        |
             
    modified tree:

                6            |
              /   \          |
             3     5         |
            / \   /          |
           6  10  4          |
          / \  /             |
         1  8 7              |

      expected = 4
    '''
    root_list = [6, [5, None, 
                        [4, None, None] ], 
                    [3, [10, [7, None, None], 
                             None], 
                        [6, [8, None, None], 
                            [1, None, None]]]]
    exp_list =  [6, [3, [6, [1, None, None], 
                            [8, None, None]],
                        [10, [7, None, None], 
                             None], 
                        ],
                    [5, None, 
                        [4, None, None] ], 
                    ]
    expected = 4
    return do_ex2_test(root_list, expected, exp_list)

def test_ex2_2(run=True):
    '''
              root       
          ______2______  
         |             | 
      __ 7__        ___15___  
     |      |      |       | 
    _4_     3_    _0_     _5_  
   |   |      |  |   |   |   | 
   2   -1     1  8   3   2  -9 

       expected = 4
    '''
    root_list = [2, [7, [4, [2, None, None],
                            [-1, None, None]],
                        [3, None,
                            [1, None, None]]],
                    [15, [0, [8, None, None],
                             [3, None, None]],
                         [5, [2, None, None],
                             [-9, None, None]]]]
    exp_list  = [2, [7, [3, None,
                            [1, None, None]],
                        [4, [-1, None, None],
                            [2, None, None]],
                        ],
                    [15, [0, [3, None, None],
                             [8, None, None]],
                         [5, [-9, None, None],
                             [2, None, None]]]]
    expected  =  4
    return do_ex2_test(root_list, expected, exp_list)


def test_ex2_3(run=True):
    '''
    A big tree
    expected = 44
    '''
    root_list = [-2, [5, [13, [-7, [2, [26, [27, [10, [0, None, [24, None, None]], [14, None, None]], [13, [30, [2, None, None], None], [-3, None, [-1, None, None]]]], [10, [28, None, None], [-1, [-3, [30, None, None], [-9, None, None]], [19, None, None]]]], None], [8, [11, [-2, [4, None, None], [5, None, None]], [6, [24, None, None], [19, None, None]]], [9, None, [1, [18, None, [-3, None, None]], [22, None, [-10, [5, None, None], None]]]]]], [17, [12, [26, [10, [21, None, [1, None, None]], [26, None, [30, None, None]]], [-3, [-2, [-3, None, [-2, [28, None, None], [21, None, None]]], [7, [-4, None, None], None]], [-1, [2, [18, None, None], [-2, None, None]], [24, [4, None, None], [30, [-4, None, None], None]]]]], [-2, [16, None, [9, [17, [23, None, None], None], [21, None, None]]], [-8, [2, None, [-10, None, None]], [20, [21, [7, None, None], [-5, [20, None, None], None]], [0, None, [-4, None, None]]]]]], [-1, None, [6, [30, [22, None, None], None], [28, [-4, None, None], [-10, None, None]]]]]], [-5, [13, [20, None, [17, [17, [25, [4, [5, [-4, [21, None, None], None], None], [-3, [21, None, None], None]], None], [14, [-10, [5, None, [28, [15, [7, None, [12, None, None]], [7, None, None]], [24, None, [-2, None, None]]]], [-4, [2, None, None], [14, None, None]]], [10, None, [7, [12, None, None], [19, [0, None, None], None]]]]], None]], [5, [2, [14, [3, None, None], [0, None, None]], [5, [15, None, [15, None, None]], [22, [15, None, None], [6, None, None]]]], None]], [-7, [-7, [14, [5, [24, None, [3, [4, [10, None, None], None], [27, None, None]]], [-5, [30, None, None], [24, None, None]]], [-8, [4, [-10, [10, [27, None, None], [5, None, [14, None, None]]], [10, [27, None, None], [16, None, None]]], [15, [20, None, None], [28, None, [-7, [-5, None, None], [10, None, None]]]]], [25, [17, [7, [19, None, None], [-4, [3, None, None], [12, None, None]]], [12, [23, None, None], [2, None, None]]], [20, [4, None, None], [22, [22, None, None], [21, [27, None, None], None]]]]]], [9, [12, [6, [-4, [-2, None, None], [11, None, [18, None, None]]], [25, [11, None, None], [25, None, None]]], [7, [10, [6, [18, None, None], [18, None, [0, None, None]]], [30, [5, None, None], None]], [8, None, [25, [2, None, [-4, None, None]], [-2, [27, None, None], [-4, None, None]]]]]], [1, [-9, [-10, [26, [17, None, None], None], [28, [-2, [22, None, None], None], [-6, None, [30, None, None]]]], [28, [19, [-3, None, [25, None, [10, None, None]]], [8, None, [4, None, None]]], [11, [8, None, None], [24, None, [-10, None, None]]]]], [26, [29, [-10, None, None], [-6, None, None]], None]]]], [-2, [20, [-10, [2, None, [28, [-9, [11, None, None], None], [1, None, None]]], [13, [10, None, None], [-2, None, None]]], [-4, [19, [-9, None, [-1, None, None]], [-8, [12, [21, None, None], [8, None, None]], [3, [7, None, [17, None, None]], [23, None, None]]]], [25, [3, [19, None, [-4, [25, None, None], None]], [-10, None, None]], [12, [4, [-10, None, None], None], [18, [15, [27, None, None], [-2, None, None]], [13, None, None]]]]]], [-6, [29, [17, [-4, None, [-5, None, None]], [-2, [-3, None, [-8, None, None]], [-7, None, None]]], [8, [11, [21, [-3, None, [2, None, None]], [2, None, None]], [-6, None, None]], None]], [-9, [29, [23, None, [25, [20, None, None], None]], [30, [24, [6, [25, None, None], [24, None, None]], [2, [25, None, None], [-9, [3, None, None], None]]], [16, [0, None, [-1, None, None]], [30, None, None]]]], [28, [25, [5, [3, None, None], [9, [4, None, None], None]], [-8, None, [21, None, None]]], [23, [16, [-7, [7, None, None], [12, None, None]], [16, None, [16, None, None]]], [-8, [24, None, [5, None, None]], [2, [23, None, None], [14, None, None]]]]]]]]]]], [20, [20, [19, [-2, [-1, [3, [24, [12, None, None], None], [5, None, None]], [10, None, None]], [27, [29, [24, None, None], None], [30, [-9, [4, None, None], None], None]]], [-10, [21, [26, [24, None, None], None], [5, None, [18, None, None]]], [-4, [1, None, None], [1, None, None]]]], [23, [2, [4, [21, None, [30, None, None]], None], [16, [-8, None, None], [6, None, None]]], [14, [12, None, [27, [-5, None, None], [10, None, None]]], [6, [18, None, None], [3, None, None]]]]], None]]
    expected = 14
    exp_list  = [-2, [5, [-5, [-7, [-7, [9, [1, [-9, [-10, [26, [17, None, None], None], [28, [-6, None, [30, None, None]], [-2, [22, None, None], None]]], [28, [11, [8, None, None], [24, None, [-10, None, None]]], [19, [-3, None, [25, None, [10, None, None]]], [8, None, [4, None, None]]]]], [26, [29, [-10, None, None], [-6, None, None]], None]], [12, [6, [-4, [-2, None, None], [11, None, [18, None, None]]], [25, [11, None, None], [25, None, None]]], [7, [8, None, [25, [-2, [-4, None, None], [27, None, None]], [2, None, [-4, None, None]]]], [10, [6, [18, None, None], [18, None, [0, None, None]]], [30, [5, None, None], None]]]]], [14, [-8, [4, [-10, [10, [5, None, [14, None, None]], [27, None, None]], [10, [16, None, None], [27, None, None]]], [15, [20, None, None], [28, None, [-7, [-5, None, None], [10, None, None]]]]], [25, [17, [7, [-4, [3, None, None], [12, None, None]], [19, None, None]], [12, [2, None, None], [23, None, None]]], [20, [4, None, None], [22, [21, [27, None, None], None], [22, None, None]]]]], [5, [-5, [24, None, None], [30, None, None]], [24, None, [3, [4, [10, None, None], None], [27, None, None]]]]]], [-2, [-6, [-9, [28, [23, [-8, [2, [14, None, None], [23, None, None]], [24, None, [5, None, None]]], [16, [-7, [7, None, None], [12, None, None]], [16, None, [16, None, None]]]], [25, [-8, None, [21, None, None]], [5, [3, None, None], [9, [4, None, None], None]]]], [29, [23, None, [25, [20, None, None], None]], [30, [16, [0, None, [-1, None, None]], [30, None, None]], [24, [2, [-9, [3, None, None], None], [25, None, None]], [6, [24, None, None], [25, None, None]]]]]], [29, [8, [11, [-6, None, None], [21, [-3, None, [2, None, None]], [2, None, None]]], None], [17, [-4, None, [-5, None, None]], [-2, [-7, None, None], [-3, None, [-8, None, None]]]]]], [20, [-10, [2, None, [28, [-9, [11, None, None], None], [1, None, None]]], [13, [-2, None, None], [10, None, None]]], [-4, [19, [-9, None, [-1, None, None]], [-8, [3, [7, None, [17, None, None]], [23, None, None]], [12, [8, None, None], [21, None, None]]]], [25, [3, [-10, None, None], [19, None, [-4, [25, None, None], None]]], [12, [4, [-10, None, None], None], [18, [13, None, None], [15, [-2, None, None], [27, None, None]]]]]]]]], [13, [5, [2, [5, [15, None, [15, None, None]], [22, [6, None, None], [15, None, None]]], [14, [0, None, None], [3, None, None]]], None], [20, None, [17, [17, [14, [-10, [-4, [2, None, None], [14, None, None]], [5, None, [28, [15, [7, None, [12, None, None]], [7, None, None]], [24, None, [-2, None, None]]]]], [10, None, [7, [12, None, None], [19, [0, None, None], None]]]], [25, [4, [-3, [21, None, None], None], [5, [-4, [21, None, None], None], None]], None]], None]]]], [13, [-7, [2, [26, [10, [-1, [-3, [-9, None, None], [30, None, None]], [19, None, None]], [28, None, None]], [27, [10, [0, None, [24, None, None]], [14, None, None]], [13, [-3, None, [-1, None, None]], [30, [2, None, None], None]]]], None], [8, [9, None, [1, [18, None, [-3, None, None]], [22, None, [-10, [5, None, None], None]]]], [11, [-2, [4, None, None], [5, None, None]], [6, [19, None, None], [24, None, None]]]]], [17, [-1, None, [6, [28, [-10, None, None], [-4, None, None]], [30, [22, None, None], None]]], [12, [-2, [-8, [2, None, [-10, None, None]], [20, [0, None, [-4, None, None]], [21, [-5, [20, None, None], None], [7, None, None]]]], [16, None, [9, [17, [23, None, None], None], [21, None, None]]]], [26, [-3, [-2, [-3, None, [-2, [21, None, None], [28, None, None]]], [7, [-4, None, None], None]], [-1, [2, [-2, None, None], [18, None, None]], [24, [4, None, None], [30, [-4, None, None], None]]]], [10, [21, None, [1, None, None]], [26, None, [30, None, None]]]]]]]], [20, [20, [19, [-10, [-4, [1, None, None], [1, None, None]], [21, [5, None, [18, None, None]], [26, [24, None, None], None]]], [-2, [-1, [3, [5, None, None], [24, [12, None, None], None]], [10, None, None]], [27, [29, [24, None, None], None], [30, [-9, [4, None, None], None], None]]]], [23, [2, [4, [21, None, [30, None, None]], None], [16, [-8, None, None], [6, None, None]]], [14, [6, [3, None, None], [18, None, None]], [12, None, [27, [-5, None, None], [10, None, None]]]]]], None]]
    return do_ex2_test(root_list, expected, exp_list)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3, test_func1_4,
    test_func2_1, test_func2_2, test_func2_3, test_func2_4,
    test_func3_1, test_func3_2, test_func3_3, test_func3_4,
    test_func4_1, test_func4_2, test_func4_3,
    test_func5_1, test_func5_2, test_func5_3, test_func5_4,
    test_ex1_1,   test_ex1_2,   test_ex1_3,
    test_ex2_1,   test_ex2_2,   test_ex2_3,
    test_personal_data_entry,
]


if __name__ == '__main__':
    if test_personal_data_entry() < 0:
        print(f"{COL['RED']}PERSONAL INFO MISSING. PLEASE FILL THE INITIAL VARS WITH YOUR NAME SURNAME AND STUDENT_ID{COL['RST']}")
        sys.exit()
    check_expected()
    testlib.runtests(   tests,
                        verbose=True,
                        logfile='grade.csv',
                        stack_trace=DEBUG)
    testlib.check_exam_constraints()
    if 'matricola' in program.__dict__:
        print(f"{COL['GREEN']}Nome: {program.nome}\nCognome: {program.cognome}\nMatricola: {program.matricola}{COL['RST']}")
    elif 'student_id' in program.__dict__:
        print(f"{COL['GREEN']}Name: {program.name}\nSurname: {program.surname}\nStudentID: {program.student_id}{COL['RST']}")
    else:
        print('we should not arrive here the  matricola/student ID variable is not present in program.py')
################################################################################
