# f = open("EIGBUCH.dat")
# print(f.read())

# newFileByteArray = bytearray(newFileBytes)
# newFile = open("EIGBUCH-edit.txt", "wb")

def nope():
    print("NOPE")
    exit(0)

entries = list()
currentEntry = ""

flag_newentry = False

# o = open("EIGBUCH-out-v1.txt", "w")

f = open("EIGBUCH-head.dat", 'rb')
# f = open("EIGBUCH-head.dat", 'rb')
byte = f.read(62)
while byte:
    # Do stuff with byte.
    byte = f.read(1)
    # print(byte)
    if byte == b'\x84': #ä
        byte = b'\xE4'
    if byte == b'\x94': #ö
        byte = b'\xF6'
    if byte == b'\x81': #ü
        byte = b'\xFC'
    if byte == b'\x9A': #Ü
        byte = b'\xDC'
    if byte == b'\xFA': #.
        byte = b'\x2E'
    if byte == b'\x1A': #Lücke
        flag_newentry = True
        continue

    c = byte.decode("ISO-8859-1")

    if flag_newentry:
        # o.write("\n\n-----\n\n")

        entries.append(currentEntry)
        currentEntry = ""

        flag_newentry = False

    currentEntry += c
    # o.write(c)

    # print(c, end='')

for entry in entries:
    # print(entry)
    # print(entry.index('ISBN:'))
    titleF = entry[:entry.index('ISBN:')]
    print(titleF.replace('\n', ' ').replace('\r', '').strip()[2:])
    rest = entry[entry.index('ISBN:'):]
    # print(rest)

    print(rest[:26]) #ISBN
    if "ISBN" not in rest[:26]: nope()
    print(rest[26:52]) #Verlag
    if "Verlag" not in rest[26:52]: nope()
    print(rest[52:69]) #Sprache
    if "Sprache" not in rest[52:69]: nope()
    print(rest[69:75]) #Art
    if "Art" not in rest[69:75]: nope()
    print(rest[77:127]) #Originaltitel
    if "Originaltitel" not in rest[77:127]: nope()
    print(rest[129:145]) #Erstersch.
    if "Erstersch." not in rest[129:145]: nope()

    print(rest[146:180])
    print(rest[180:198])
    print(rest[211:237])
    print(rest[237:263])
    print(rest[276:301])
    print(rest[301:330])
    print(rest[330:340])
    print(rest[340:365])
    print(rest[365:397])
    print(rest[406:442])
    print(rest[444:460])
    print(rest[460:493])
    print(rest[493:506])

    print('\n---\n')
