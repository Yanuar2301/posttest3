
awal = 0
tambah = 1
nim = int(input("Masukan 2 angka terakhir nim anda = "))
jumlah = nim + 10

while(awal < jumlah):
    print(tambah)
    tambah += 1
    if tambah == 10 :
        tambah -= 9
    awal += 1


