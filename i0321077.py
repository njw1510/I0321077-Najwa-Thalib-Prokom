def buatmatrik(nilaiseed, row, col):
#"membuat matrik"
    import random
    MA = [0] * row
    random.seed(nilaiseed)
    for baris in range(row):
        MA[baris] = [0] * col
        for j in range(col):
            MA[baris][j] = random.randrange(1,100)
    for x in range(row):
        print("[", end =" ")
        for y in range(col):
            mat = MA[x][y]
            print(mat, end=" ")
        print("]")
    return MA




def main():
    pilih = str(input("matriks ke = ? (1 / 2)"))
    if pilih == "1":
        buatmatrik(21,7,9)
    elif pilih == "2":
        buatmatrik(77,7,9)

    
    return
if __name__=="__main__":
    main()