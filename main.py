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
    result = []
    for i in b:
        result.append(i[1] + chr(ord(i[0]) ^ ord(k[0])))
    return result


def decript(b, k):
    result = []
    for i in b:
        result.append(chr(ord(i[1]) ^ ord(k[0])) + i[0])
    return result


for i in range(0, ROUNDS):
    block = cript(block, KEY[sch])
    print("Раунд: ", i, " ", block)
    sch += 1

for i in range(0, ROUNDS):
    sch -= 1
    block = decript(block, KEY[sch])
    print("Раунд: ", i, " ", block)
