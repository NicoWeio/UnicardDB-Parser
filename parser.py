# f = open("EIGBUCH.dat")
# print(f.read())

# newFileByteArray = bytearray(newFileBytes)
# newFile = open("EIGBUCH-edit.txt", "wb")

f = open("EIGBUCH-head.dat", 'rb')
# f = open("EIGBUCH-head.dat", 'rb')
byte = f.read(1)
while byte:
    # Do stuff with byte.
    byte = f.read(1)
    # print(byte)
    # if byte == 0x84:
    if byte == b'\x81':
        byte = b'\xFC'
    if byte == b'\x1A':
        continue
        # print("HIT!")
        # print(byte.decode("ISO-8859-1"), end = '')
    # else:
    print(byte.decode("ISO-8859-1"), end='')
