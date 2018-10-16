# name Владислав
ROUNDS = 16
KEY = 'Bладислав'
text = 'Куй железо не отходя от кассы'
block = []
key_position = 0


while ROUNDS > len(KEY):
    KEY += KEY


if (len(text) % 2) == 1:
    text = text + ' '

for i in range(0, len(text), 2):
    block.append(text[i:i + 2])


def cript(b, k):
    return [i[1] + chr(ord(i[0]) ^ ord(k[0])) for i in b]


def decript(b, k):
    return [chr(ord(i[1]) ^ ord(k[0])) + i[0] for i in b]


print('\nШифрование текста:\n')\

for i in range(0, ROUNDS):
    block = cript(block, KEY[key_position])
    print("Раунд: ", i, " ", block)
    key_position += 1

print('\nДешифрование текста:\n')

for i in range(0, ROUNDS):
    key_position -= 1
    block = decript(block, KEY[key_position])
    print("Раунд: ", i, " ", block)
