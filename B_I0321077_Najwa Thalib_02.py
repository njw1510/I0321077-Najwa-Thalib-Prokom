#Uang Muka
uangMukaCityCar = 250000000 * 90 / 100
uangMukaMPV = 300000000 * 90 / 100
#Sisa yang harus dibayarkan
sisaCityCar = 250000000 - uangMukaCityCar
sisaMPV = 300000000 - uangMukaMPV
#Cicilan 
cicilanCityCar1 = sisaCityCar / 11 * 0.5 + sisaCityCar / 11
cicilanMPV1 = sisaMPV / 11 * 0.5 + sisaMPV / 11
cicilanCityCar2 = sisaCityCar / 23 * 0.5 + sisaCityCar / 23
cicilanMPV2 = sisaMPV / 23 * 0.5 + sisaMPV / 23
cicilanCityCar3 = sisaCityCar / 35 * 0.5 + sisaCityCar / 35
cicilanMPV3 = sisaMPV / 35 * 0.5 + sisaMPV / 35
cicilanCityCar4 = sisaCityCar / 47 * 0.5 + sisaCityCar / 47
cicilanMPV4 = sisaMPV / 47 * 0.5 + sisaMPV / 47
cicilanCityCar5 = sisaCityCar / 59 * 0.5 + sisaCityCar / 59
cicilanMPV5 = sisaMPV / 59 * 0.5 + sisaMPV / 59

#Program
print ("Program untuk mengitung kredit cicilan mobil City Car On The Road dan MPV On The Road")
print ("=========================================================")
kendaraan = input("Masukkan kendaraan anda (city car, mpv): ")
if kendaraan == "city car" :
    print ("Uang Muka yang harus dibayarkan adalah sebesar = Rp", uangMukaCityCar)
    print ("Sisa yang harus dibayarkan adalah sebesar = Rp", sisaCityCar)
    pertanyaan = input("Masukkan cicilan yang dipilih (1/2/3/4/5 tahun): ")
    if pertanyaan == "1" :
        print ("Cicilan yang harus dibayarkan adalah sebesar = Rp", cicilanCityCar1)
    elif pertanyaan == "2" :
        print ("Cicilan yang harus dibayarkan adalah sebesar = Rp", cicilanCityCar2)
    elif pertanyaan == "3" :
        print ("Cicilan yang harus dibayarkan adalah sebesar = Rp", cicilanCityCar3)
    elif pertanyaan == "4" :
        print ("Cicilan yang harus dibayarkan adalah sebesar = Rp", cicilanCityCar4)
    elif pertanyaan == "5" :
        print ("Cicilan yang harus dibayarkan adalah sebesar = Rp", cicilanCityCar5)
    else :
        print ("Pilihan tidak tersedia")
elif kendaraan == "mpv" :
    print ("Uang Muka yang harus dibayarkan adalah sebesar = Rp", uangMukaMPV)
    print ("Sisa yang harus dibayarkan adalah sebesar = Rp", sisaMPV)
    pertanyaan = input("Masukkan cicilan yang dipilih (1/2/3/4/5 tahun): ")
    if pertanyaan == "1" :
        print ("Cicilan yang harus dibayarkan adalah sebesar = Rp", cicilanMPV1)
    elif pertanyaan == "2" :
        print ("Cicilan yang harus dibayarkan adalah sebesar = Rp", cicilanMPV2)
    elif pertanyaan == "3" :
        print ("Cicilan yang harus dibayarkan adalah sebesar = Rp", cicilanMPV3)
    elif pertanyaan == "4" :
        print ("Cicilan yang harus dibayarkan adalah sebesar = Rp", cicilanMPV4)
    elif pertanyaan == "5" :
        print ("Cicilan yang harus dibayarkan adalah sebesar = Rp", cicilanMPV5)
    else :
        print ("Pilihan tidak tersedia")
else :
    print ("Pilihan tidak tersedia")
print ("=========================================================")