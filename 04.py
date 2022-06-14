def buatmatrik(nilaiseed, row, col):
#"membuat matrik"
    global MA
    import random
    MA = [0] * row
    random.seed(nilaiseed)
    for baris in range(row):
        print("[", end =" ")
        MA[baris] = [0] * col
        for j in range(col):
            MA[baris][j] = random.randrange(1,100)
            mat = MA[baris][j]
            print(mat, end=" ")
        print("]")

    return MA


def penjumlahanbaris (baris,col):
    print("INI HASIL MA1 dan MA 2")
    print("MA 1 =")
    MA1=buatmatrik(21,7,9)
    print("MA 2 =")
    MA2=buatmatrik(5,7,9)
    print("")
    print("")
    print("HASIL PENJUMLAHAN BARIS =====")
    print("")
    print("")
    for i in range (col):
        hasiljumlahbaris = MA1[baris][i]+ MA2[baris][i]
        print (hasiljumlahbaris, end=" ")

def penjumlahankolom (baris,col):
    print("INI HASIL MA1 dan MA 2")
    print("MA 1 =")
    MA1=buatmatrik(21,7,9)
    print("MA 2 =")
    MA2=buatmatrik(77,7,9)
    print("")
    print("")
    print("HASIL PENJUMLAHAN KOLOM =====")
    print("")
    print("")
    for i in range (baris):
        hasiljumlahbaris = MA1[i][col]+ MA2[i][col]
        print (hasiljumlahbaris, end=" ")

def main():
    pilih = str(input("matriks ke = ? (1 / 2)"))
    if pilih == "1":
        buatmatrik(21,7,9)
    elif pilih == "2":
        buatmatrik(77,7,9)
    pilihbaris = int(input("baris  ke = ? (n)"))
    penjumlahanbaris (pilihbaris,9)
    print()
    pilihkolom = int(input("kolom  ke = ? (n)"))
    penjumlahankolom (7,pilihkolom)



    
    return
if __name__=="__main__":
    main()