# f = open("EIGBUCH.dat")
# print(f.read())

# newFileByteArray = bytearray(newFileBytes)
# newFile = open("EIGBUCH-edit.txt", "wb")


def nope():
    print("NOPE")
    exit(0)


def read_single(content, startsWith):
    global total_error_count
    global flag_error_in_entry
    trimContent = content.replace('\n', '').replace('\r', '').strip()
    if not trimContent.startswith(startsWith):
        print(f'!!! "{trimContent}" does not start with "{startsWith}"')
        total_error_count = total_error_count + 1
        flag_error_in_entry = True
        # exit(1)
    return trimContent.replace(startsWith, '').strip()

def read_line(line, keywords):
    global total_error_count
    global flag_error_in_entry
    result = list()
    for i, keyword in enumerate(keywords):
        try:
            indexstart = line.index(keyword)+len(keyword)
            if ((i+1) < len(keywords)):
                next = keywords[i+1]
                sub = line[indexstart:line.index(next)]
                # result.append(line[indexstart:line.index(next)].strip())
            else:
                # result.append(line[indexstart:].strip())
                sub = line[indexstart:]
            if sub.strip() == '.':
                result.append('')
            else:
                result.append(sub.strip())
        except:
            print("Substring not found…")
            total_error_count += 1
            flag_error_in_entry = True
            result.append(False)
    return result


def read_v1(rest):
    entry = {
        'isbn': read_single(rest[0:26],    'ISBN:'),
        'verlag': read_single(rest[26:52],   'Verlag:'),
        'sprache': read_single(rest[52:69],   'Sprache:'),
        'art': read_single(rest[69:75],   'Art:'),
        'originaltitel': read_single(rest[77:127],  'Originaltitel:'),
        'erstersch': read_single(rest[129:145], 'Erstersch.:'),
        'geliehen': read_single(rest[146:180], 'geliehen.von:'),
        'geliehen_am': read_single(rest[180:198], 'am:'),
        'ausleihe': read_single(rest[211:237], 'Ausleihe.offen?:'),
        'rueckg_datum': read_single(rest[237:263], 'Rückgdatum:'),
        'herkunft': read_single(rest[276:301], 'Herkunft:'),
        'herkunft_datum': read_single(rest[301:330], 'Herk.datum:'),
        'preis': read_single(rest[330:340], 'Preis:'),
        'verliehen': read_single(rest[340:365], 'verliehen..ja(')[:-1],
        'verliehen_an': read_single(rest[365:397], 'an:'),
    }
    # read_single(rest[407:442], 'todo', 'Bemerkungen.und.Stichworte')
    # read_single(rest[444:460], 'todo', 'zu.lesen')
    # read_single(rest[460:493], 'todo', 'wo.gesehen')
    # read_single(rest[493:506], 'todo', 'Signatur')
    return entry


def write_csv(entries):
    import csv

    with open('out_v1.csv', 'w', newline='') as csvfile:
        fieldnames = ['isbn', 'verlag', 'sprache', 'art', 'originaltitel', 'erstersch', 'geliehen', 'geliehen_am',
                      'ausleihe', 'rueckg_datum', 'herkunft', 'herkunft_datum', 'preis', 'verliehen', 'verliehen_an']
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames, extrasaction='ignore')

        writer.writeheader()
        for row in entries:
            writer.writerow(row)


entries = list()
currentEntry = ""

flag_newentry = False
flag_error_in_entry = False
error_count = 0
total_error_count = 0
type1_count = 0
type2_count = 0
unrecognized_count = 0

# o = open("EIGBUCH-out-v1.txt", "w")

unrecognized_out = open("unrecognized.txt", "w")

f = open("EIGBUCH.dat", 'rb')
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
    if byte == b'\xE1':  # ß
        byte = b'\xDF'
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

parsed_entries = list()

for entry in entries:
    # print(entry)
    # print("-----")

    if 'verliehen? (n) an:' in entry:
        # print('Guessed Type 2: TODO')
        type2_count += 1
        continue
    if not 'ISBN:' in entry:
        print('!!! quite fatal: ISBN not found')
        continue
    if 'verliehen..ja(' in entry:
        # print('Guessed Type 1… All good… Yet…')
        type1_count += 1
    else:
        print('!!!!!!!!!!!!!!!!!!')
        print("Not recognized: ")
        print(entry)
        print('!!!!!!!!!!!!!!!!!!')
        unrecognized_count += 1
        continue

    rest = entry[entry.index('ISBN:'):]
    # parsed_entry = read_v1(rest)
    # parsed_entries.append(parsed_entry)

    lines = rest.splitlines()
    flag_error_in_entry = False

    # print(lines[8])

    results = [read_line(lines[0], ['ISBN:', 'Verlag:', 'Sprache:', 'Art:']),
                read_line(lines[1], ['Originaltitel:', 'Erstersch.:']),
                read_line(lines[3], ['geliehen.von:', 'am:', 'Signatur:']),
                read_line(lines[4], ['Ausleihe.offen?:', 'Rückgdatum:', 'z.am:']),
                read_line(lines[7], ['Herkunft:', 'Herk.datum:', 'Preis:']),
                read_line(lines[8], ['verliehen..ja', 'an:', 'am:']),
    ]
    print(results)

    parsed_entry = {
        'isbn': results[0][0],
        'verlag': results[0][1],
        'sprache': results[0][2],
        'art': results[0][3],
        'originaltitel': results[1][0],
        'erstersch': results[1][1],
        'geliehen': results[2][0],
        'geliehen_am': results[2][1],
        'ausleihe': results[3][0],
        'rueckg_datum': results[3][1],
        'herkunft': results[4][0],
        'herkunft_datum': results[4][1],
        'preis': results[4][2],
        'verliehen': results[5][0],
        'verliehen_an': results[5][1],
    }

    if flag_error_in_entry:
        print("→ Error in current…")
        unrecognized_out.write(entry)
        unrecognized_out.write('\n-----\n')
        flag_error_in_entry = False
        error_count += 1
    else:
        parsed_entries.append(parsed_entry)


print("ERROR ENTRIES COUNT: " + str(error_count))
print("TOTAL ERROR COUNT: " + str(total_error_count))
print("TYPE 1 COUNT: " + str(type1_count))
print("TYPE 2 COUNT: " + str(type2_count))
print("UNRECOGNIZED COUNT: " + str(unrecognized_count))

write_csv(parsed_entries)
