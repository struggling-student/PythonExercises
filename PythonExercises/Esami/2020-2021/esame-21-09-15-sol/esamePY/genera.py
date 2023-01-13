import random
import program
def randomR():
     return  (random.randint(50,200)*2,      # larghezza
              random.randint(50,200)*2,      # altezza
             (   random.randint(50, 255),    # R
                 random.randint(50, 255),    # G
                 random.randint(50, 255)))   # B

rettangoli = [ randomR() for _ in range(20)]
print(rettangoli)
print(program.ex2(rettangoli,1500,1400,'20rect.png'))
