
import random, sys, json

with open('names.txt') as F:
    NAMES = F.read().split()

_, filename, N = sys.argv
N = int(N)

def leaves(family):
    # all leaves
    return { x  for x in family
                if not family[x]['spouse'] and not (any(x in family[y]['parents'] for y in family)) }

#print(NAMES)
ancestors  = random.sample(NAMES, k=10)
names      = random.sample(list(set(NAMES)-set(ancestors)), k=N)
family = {}
print(ancestors)
for name in ancestors:
    family[name] = {
        'alive'  : random.randint(1, 100) > 50,
        'parents': [],
        'spouse' : None
    }
for name in ancestors:
    if random.randint(1, 100) <= 20:        # 20% prob to be married (times 2 = at most 40% married)
        spouse = random.choice(ancestors)
        if not family[spouse]['spouse']:
            family[name]['spouse'] = spouse
            family[spouse]['spouse'] = name

print(json.dumps(family))

for name in names:
    family[name] = {
        'alive'  : random.randint(1,100) > 50,
        'parents': random.sample(list(family.keys()), k=2),
        'spouse' : None
    }
    if random.randint(1, 100) <= 20:
        foglie = list(leaves(family)-{name})
        print(foglie)
        spouse = random.choice(foglie)
        if not family[spouse]['spouse']:
            family[name]['spouse'] = spouse
            family[spouse]['spouse'] = name

print(json.dumps(family, indent=4))

with open(filename+'.json', mode='w', encoding='utf8') as F:
    json.dump(family, F, indent=4)

with open(filename+'.dot', mode='w', encoding='utf8') as F:
    print('digraph G {rankdir=LR', file=F)
    for p,v in family.items():
        if v['alive']:
            print(f'{p}', file=F)
        else:
            print(f'{p} [color=red]', file=F)
        for g in v['parents']:
            print(f'{p} -> {g}', file=F)
        if v['spouse']:
            print(f'{p} -> {v["spouse"]} [color=green]', file=F)
    print('}', file=F)
