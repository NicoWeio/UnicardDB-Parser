# f = open("EIGBUCH.dat")
# print(f.read())

# newFileByteArray = bytearray(newFileBytes)
# newFile = open("EIGBUCH-edit.txt", "wb")

flag_newentry = False

o = open("EIGBUCH-out-v1.txt", "w")

f = open("EIGBUCH-head.dat", 'rb')
# f = open("EIGBUCH-head.dat", 'rb')
byte = f.read(1)
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
        o.write("\n\n-----\n\n")
        flag_newentry = False
    o.write(c)

    print(c, end='')
