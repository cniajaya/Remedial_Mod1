# Celine Kurniajaya JCDS 07 Remedial Modul 1

# Soal no 1
def Find_short(s):
    huruf = s.split(' ')
    jumlah_huruf = []
    for item in huruf:
        if item !='':
            angka = len(item)
            jumlah_huruf.append(angka)
    jumlah_huruf.sort()
    print (jumlah_huruf[0])
Find_short("Many people get up early in the morning ")
Find_short("Every office would getting newest monitor ")
Find_short("Create new file after this morning")

# Soal no 2
def persistence(n):
    strn = str(n)
    check = False
    total = 0
    while check == False:
        hasil = 1
        for item in strn:
            hasil*=int(item)
        total +=1
        if hasil < 10:
            check = True
        else:
            strn = str(hasil)
            check = False
    if n < 10:
        total =0
    print(total)
persistence(39)
persistence(999)
persistence(4)

# Soal no 3
def multiplication_table(rows,cols):
    for row in range(1,rows+1):
        for col in range(1,cols+1):
            print(row*col, end=" ")
        print()
multiplication_table(3,3)
multiplication_table(5,3)
multiplication_table(3,5)

# Soal no 4
def alphabet_position(text):
    hrfl=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    textl = text.lower()
    kamus = {}
    angka = 1
    hasil = ''
    for item in hrfl:
        kamus[item] = angka
        angka+=1
    for huruf in textl:
        if huruf.isalpha() == True:
            hasil += f'{kamus[huruf]} '
        else:
            hasil+=''
    print(hasil)
alphabet_position("The sunset sets at twelve o' clock.")
alphabet_position("it’s never too late to try")
alphabet_position("Have you done your homework?")