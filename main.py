#name Владислав
ROUNDS = 16
KEY = "Bладислав"
TEXT = 'Куй железо не отходя от кассы'
Block = []
sch = len(KEY) - 1


while ROUNDS >= len(KEY)*2:
    KEY += KEY
    sch = len(KEY) - 1

En1 = []
En0 = []
LenTXT = len(TEXT)

if (LenTXT % 2) == 1:
    TEXT = TEXT + ' '

for i in range(0, len(TEXT), 2):
    Block.append(TEXT[i:i+2])


def incript(b, k):
    block2 = []
    for i in b:
        block2.append(i[1] + chr(ord(i[0]) ^ ord(k[0])))
    return block2


def decript(b, k):
    block2 = []
    for i in b:
        block2.append(chr(ord(i[1]) ^ ord(k[0])) + i[0])
    return block2


for i in range(0,ROUNDS):
    En1 = incript(Block, KEY[sch])
    Block = En1
    print("Раунд: ", i, " ", En1)
    sch -= 1

for i in range(0, ROUNDS):
    sch +=1
    Dec = decript(Block, KEY[sch])
    Block = Dec
    print("Раунд: ", i, " ", Dec)
