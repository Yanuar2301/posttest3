kue_keju = 25
kue_coklat = 35

def tanya():
    tanya = str(input("Apakah Anda ingin memesan kembali? [Ya/Tidak] = "))
    if tanya == "Ya":
        awal()
    elif tanya == "Tidak":
        akhir()
    else:
        print("Masukan jawaban sesuia perintah !")
        ulang()
def ulang():
    tanya = str(input("Apakah Anda ingin memesan kembali? [Ya/Tidak] = "))
    if tanya == "Ya":
        awal()
    elif tanya == "Tidak":
        akhir()
    else:
        print("Masukan jawaban sesuia perintah !")
        ulang()

def awal():
    print("\t\t\t===============")
    print("\t\t\t Toko kue Sule")
    print("\t\t\t===============")
    print("Yuk Cek Promo Terbaru Kami")
    print("\t\t\t Kue Coklat")
    print("1. Beli 5 kue Coklat sampai 20 kue Coklat dapatkan diskon 7 %\n2. Beli 21 kue Coklat sampai 35 kue Coklat dapatkan diskon 12 %\n3. Beli kurang dari 5")
    print("\t\t\t  Kue Keju ")
    print("4. Beli 4 kue Keju sampai  15 kue Keju dapatkan diskon 10 %\n5. Beli 16 kue keju sampai 25 kue Keju dapatan diskon 15 %\n6. Beli kurang dari 4")
    print("7. Keluar")
    pilihan = int(input("Masukan Pilihan Anda! = "))
    if pilihan == 1:
        pesanan_kue_Coklat = int(input("Masukan jumlah kue cokat yang ingin Anda pesan! = "))
        if pesanan_kue_Coklat >= 5 and pesanan_kue_Coklat <= 20 :
            diskon = (pesanan_kue_Coklat * 3500 * 7/100) 
            jumlah = (pesanan_kue_Coklat * 3500 - diskon)
            print("Anda memesan {} kue coklat dan mendapat diskon sebesar Rp.{} Harga yang harus Anda bayar adalah Rp.{}".format(pesanan_kue_Coklat,diskon,jumlah))
            tanya()
        else :
            print("Anda hanya bisa memesan 5 sampai 20 kue coklat")
            ulang_kue_coklat()

    elif pilihan == 2:
        pesanan_kue_Coklat2 = int(input("Masukan jumlah kue coklat yang ingin Anda pesan! = "))
        if pesanan_kue_Coklat2 >= 21 and pesanan_kue_Coklat2 <= 35 :
            diskon2 = (pesanan_kue_Coklat2 * 3500 * 12/100) 
            jumlah2 = (pesanan_kue_Coklat2 * 3500 - diskon2)
            print("Anda memesan {} kue coklat dan mendapat diskon sebesar Rp.{} Harga yang harus Anda bayar adalah Rp.{}".format(pesanan_kue_Coklat2,diskon2,jumlah2))
            tanya()
        else :
            print("Anda hanya bisa memesan 21 sampai 35 kue coklat")
            ulang_kue_coklat2()

    elif pilihan == 3 :
        pesanan_normal = int(input("Masukan jumlah kue coklat yang ingin Anda pesan! = "))
        if pesanan_normal < 5 :
            normal = pesanan_normal * 3500
            print("Anda memesan {} kue coklat Harga yang harus Anda bayar adalah Rp.{}".format(pesanan_normal,normal))
            tanya()
        else:
            print("Anda Hanya bisa memesan 1 sampai 4 kue coklat")
            ulang_kue_coklat_normal()
    elif pilihan == 4 :
        pesanan_kue_keju = int(input("Masukan jumlah kue keju yang ingin Anda pesan! = "))
        if pesanan_kue_keju >= 4 and pesanan_kue_keju <=15 :
            diskon3 = (pesanan_kue_keju * 6000 * 10/100)
            jumlah3 = (pesanan_kue_keju * 6000 - diskon3)
            print("Anda memesan {} kue keju dan mendapat diskon sebesar Rp.{} Harga yang harus Anda bayar adalah Rp.{}".format(pesanan_kue_keju,diskon3,jumlah3))
            tanya()
        else:
            print("Anda hanya bisa memesan 4 sampai 15 kue keju")
            ulang_kue_keju()

    elif pilihan == 5 : 
        pesanan_kue_keju2 = int(input("Masukan jumlah kue keju yang ingin Anda pesan! = "))
        if pesanan_kue_keju2 >=16 and pesanan_kue_keju2 <= 25 :
            diskon4 = (pesanan_kue_keju2 * 6000 * 15/100)
            jumlah4 = (pesanan_kue_keju2 * 6000 - diskon4)
            print("Anda memesan {} kue keju dan mendapat diskon sebesar Rp.{} Harga yang harus Anda bayar adalah Rp.{}".format(pesanan_kue_keju2,diskon4,jumlah4))
            tanya()
        else:
            print("Anda hanya bisa memesan 16 sampai 25 kue keju")
            ulang_kue_keju2()

    elif pilihan == 6:
        pesanan_normal = int(input("Masukan jumlah kue keju yang ingin Anda pesan! = "))
        if pesanan_normal < 4 :
            normal = pesanan_normal * 6000
            print("Anda memesan {} kue keju Harga yang harus Anda bayar adalah Rp.{}".format(pesanan_normal,normal))
            tanya()
        else:
            print("Anda Hanya bisa memesan 1 sampai 3 kue keju")
            ulang_kue_keju_normal2()
    elif pilihan == 7 :
        print("Terima Kasih sudah membeli kue di toko kami")
    else:
        print("Masukan Pilihan yang sesuai")
        awal()

def ulang_kue_coklat():
    pesanan_kue_Coklat = int(input("Masukan jumlah kue cokat yang ingin Anda pesan! = "))
    if pesanan_kue_Coklat >= 5 and pesanan_kue_Coklat <= 20 :
        diskon = (pesanan_kue_Coklat * 3500 * 7/100) 
        jumlah = (pesanan_kue_Coklat * 3500 - diskon)
        print("Anda memesan {} kue coklat dan mendapat diskon sebesar Rp.{} Harga yang harus Anda bayar adalah Rp.{}".format(pesanan_kue_Coklat,diskon,jumlah))
        tanya()
    else :
        print("Anda hanya bisa memesan 5 sampai 20 kue coklat")
        ulang_kue_coklat()

def ulang_kue_coklat2():
    pesanan_kue_Coklat2 = int(input("Masukan jumlah kue coklat yang ingin Anda pesan! = "))
    if pesanan_kue_Coklat2 >= 21 and pesanan_kue_Coklat2 <= 35 :
        diskon2 = (pesanan_kue_Coklat2 * 3500 * 12/100) 
        jumlah2 = (pesanan_kue_Coklat2 * 3500 - diskon2)
        print("Anda memesan {} kue coklat dan mendapat diskon sebesar Rp.{} Harga yang harus Anda bayar adalah Rp.{}".format(pesanan_kue_Coklat2,diskon2,jumlah2))
        tanya()
    else :
        print("Anda hanya bisa memesan 21 sampai 35 kue coklat")
        ulang_kue_coklat2()
def ulang_kue_keju():
    pesanan_kue_keju = int(input("Masukan jumlah kue keju yang ingin Anda pesan! = "))
    if pesanan_kue_keju >= 4 and pesanan_kue_keju <=15 :
        diskon3 = (pesanan_kue_keju * 6000 * 10/100)
        jumlah3 = (pesanan_kue_keju * 6000 - diskon3)
        print("Anda memesan {} kue keju dan mendapat diskon sebesar Rp.{} Harga yang harus Anda bayar adalah Rp.{}".format(pesanan_kue_keju,diskon3,jumlah3))
        tanya()
    else:
        print("Anda hanya bisa memesan 4 sampai 15 kue keju")
        ulang_kue_keju()

def ulang_kue_keju2():
    pesanan_kue_keju2 = int(input("Masukan jumlah kue keju yang ingin Anda pesan! = "))
    if pesanan_kue_keju2 >=16 and pesanan_kue_keju2 <= 25 :
        diskon4 = (pesanan_kue_keju2 * 6000 * 15/100)
        jumlah4 = (pesanan_kue_keju2 * 6000 - diskon4)
        print("Anda memesan {} kue keju dan mendapat diskon sebesar Rp.{} Harga yang harus Anda bayar adalah Rp.{}".format(pesanan_kue_keju2,diskon4,jumlah4))
        tanya()
    else:
        print("Anda hanya bisa memesan 16 sampai 25 kue keju")
        ulang_kue_keju2()
def ulang_kue_coklat_normal():
    pesanan_normal = int(input("Masukan jumlah kue coklat yang ingin Anda pesan! = "))
    if pesanan_normal < 5 :
        normal = pesanan_normal * 3500
        print("Anda memesan {} kue coklat Harga yang harus Anda bayar adalah Rp.{}".format(pesanan_normal,normal))
        tanya()
    else:
        print("Anda Hanya bisa memesan 1 sampai 4 kue coklat")
        ulang_kue_coklat_normal()
def ulang_kue_keju_normal2():
    pesanan_normal = int(input("Masukan jumlah kue keju yang ingin Anda pesan! = "))
    if pesanan_normal < 4 :
        normal = pesanan_normal * 6000
        print("Anda memesan {} kue keju Harga yang harus Anda bayar adalah Rp.{}".format(pesanan_normal,normal))
        tanya()
    else:
        print("Anda Hanya bisa memesan 1 sampai 3 kue keju")
        ulang_kue_keju_normal2()

def akhir():
    print()
    print("Terima Kasih sudah membeli kue di toko kami")

awal()