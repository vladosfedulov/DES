# name Владислав
ROUNDS = 16
KEY = 'Bладислав'
TEXT = 'Куй железо не отходя от кассы'
block = []
sch = 0


while ROUNDS > len(KEY):
    KEY += KEY


if (len(TEXT) % 2) == 1:
    TEXT = TEXT + ' '

for i in range(0, len(TEXT), 2):
    block.append(TEXT[i:i + 2])


def cript(b, k):
    return [i[1] + chr(ord(i[0]) ^ ord(k[0])) for i in b]


def decript(b, k):
    return [chr(ord(i[1]) ^ ord(k[0])) + i[0] for i in b]


for i in range(0, ROUNDS):
    block = cript(block, KEY[sch])
    print("Раунд: ", i, " ", block)
    sch += 1

for i in range(0, ROUNDS):
    sch -= 1
    block = decript(block, KEY[sch])
    print("Раунд: ", i, " ", block)
