print ("Program untuk menghitung tarif jalan tol untuk setiap 50km")
print ("=========================================================")

hari = int(input("Masukkaan jarak hari dari lebaran (-6 sampai -1): "))
if hari < -6 :
    kendaraan1 = input("Masukkan kendaraan anda (pribadi, bus, bus, truk): ")
    if kendaraan1 == "pribadi" :
        print ("Tarif = Rp. 1000 x 50km, total tarif untuk 50km = Rp. 50000")
    elif kendaraan1 == "bus" :
        print ("Tarif = Rp. 1500 x 50km, total tarif untuk 50km = Rp. 75000")
    elif kendaraan1 == "truk" :
        print ("Tarif = Rp. 2000 x 50km, total tarif untuk 50km = Rp. 100000")
else :
    kendaraan2 = input("Masukkan kendaraan anda (pribadi, bus, bus, truk): ")
    if kendaraan2 == "pribadi" :
        print ("Tarif akan dipangkas sebanyak 20% dari tarif normal, sehingga tarif = Rp. 1000 x 80% x 50km, total tarif untuk 50km = Rp. 40000")
    elif kendaraan2 == "bus" :
        print ("Tarif akan dipangkas sebanyak 20% dari tarif normal, sehingga tarif = Rp. 1500 x 80% x 50km, total tarif untuk 50km = Rp. 60000")
    elif kendaraan2 == "truk" :
        print ("Tarif akan dipangkas sebanyak 20% dari tarif normal, sehingga tarif = Rp. 2000 x 80% x 50km, total tarif untuk 50km = Rp. 80000")
print ("=========================================================")
