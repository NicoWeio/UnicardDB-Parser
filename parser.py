# f = open("EIGBUCH.dat")
# print(f.read())

# newFileByteArray = bytearray(newFileBytes)
# newFile = open("EIGBUCH-edit.txt", "wb")

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
    # print(titleF)
    rest = entry[entry.index('ISBN:'):]
    # print(rest)
    print(rest[:26])
    print(rest[26:52])
    print(rest[52:69])
    print(rest[69:75])
    print(rest[77:127])
    # print(rest[:26])
    # print(entry[90:95])
    print('---')
