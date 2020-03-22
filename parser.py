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
    if byte == b'\x84':  # ä
        byte = b'\xE4'
    if byte == b'\x94':  # ö
        byte = b'\xF6'
    if byte == b'\x81':  # ü
        byte = b'\xFC'
    if byte == b'\x9A':  # Ü
        byte = b'\xDC'
    if byte == b'\xFA':  # .
        byte = b'\x2E'
    if byte == b'\x1A':  # Lücke
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

    print(rest[0:26])  # ISBN
    print(rest[26:52])  # Verlag
    print(rest[52:69])  # Sprache
    print(rest[69:75])  # Art
    print(rest[77:127])  # Originaltitel
    print(rest[129:145])  # Erstersch.
    print(rest[146:180])  # geliehen.von
    print(rest[180:198])  # am
    print(rest[211:237])  # Ausleihe.offen?
    print(rest[237:263])  # Rückgdatum
    print(rest[276:301])  # Herkunft
    print(rest[301:330])  # Herk.datum
    print(rest[330:340])  # Preis
    print(rest[340:365])  # verliehen
    print(rest[365:397])  # an
    print(rest[406:442])  # Bemerkungen.und.Stichworte
    print(rest[444:460])  # zu.lesen
    print(rest[460:493])  # wo.gesehen
    print(rest[493:506])  # Signatur

    print('\n---\n')
