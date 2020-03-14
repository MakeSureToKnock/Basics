#Ask for a word using input() and convert it to binary and hex

word = input('Enter a word: ').split()
del word[1:]
string = word[0]

ordList = []
hexList = []
binList = []

for i in range(len(string)):
    value = ord(string[i])
    ordList.append(str(value))

    hexValue = hex(value)
    hexList.append(hexValue)

    binValue = bin(value)
    binList.append(binValue)

print(' '.join(ordList))
print(' '.join(hexList))
print(' '.join(binList))






