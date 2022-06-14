def buatmatrik(nilaiseed=77, row=7, col=9):
    import random
    MA = [0]* row
    random.seed(nilaiseed)
    for baris in range (row):
        MA[baris] = [0] * col
        for j in range(col):
            MA[baris][j] = random.randrange(1, 100) 
    for i in range(len(MA)):
        for j in range(len(MA[i])):
            print(MA[i][j], end=' ')
        print()

def buatmatrik2(nilaiseed=2021, row=7, col=9):
    import random
    MA = [0]* row
    random.seed(nilaiseed)
    for baris in range (row):
        MA[baris] = [0] * col
        for j in range(col):
            MA[baris][j] = random.randrange(1, 100) 
    for i in range(len(MA)):
        for j in range(len(MA[i])):
            print(MA[i][j], end=' ')
        print()

def main():
    return buatmatrik()

def main2():
    return buatmatrik2()

if __name__ == "__main__":
    main()
    print()
    main2()
