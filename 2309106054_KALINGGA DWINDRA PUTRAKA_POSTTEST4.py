user = {
    "Kalingga Dwindra Putraka" : "54"
}
def menu_utama():
    while True:
        print("Program perhitungan tahun kabisat")
        print("1. Login")
        print("2. Keluar")
        pilihan = input("Pilih opsi : ")
        if pilihan == '1':
            masuk=login()
            if masuk:
                kabisat()
        elif pilihan == '2':
            print("Program Berhenti.")
            break
        else:
            print("Pilihan tidak valid.")
            
def login():
    coba = 0
    while coba < 3 :
        nama = input("Masukkan nama : ")
        nim = input("Masukkan NIM : ")
        if nama in user and user[nama] == nim:
            print("Login Berhasil")
            return True
        else:
            print("Login gagal.")
            coba += 1
        if coba == 3:
            print("Anda telah mencoba login sebanyak 3 kali. Kembali ke menu awal.")
            print()
            break
        
def kabisat():
    while(True):
        tahun = int(input("Masukkan tahun : "))
        if tahun == 0 :
            print("Input tidak valid. Kembali ke menu awal.")
            break
        elif tahun%400==0 :
            print("Tahun " + str(tahun) + " adalah tahun kabisat.")
        elif tahun%100==0 :
            print("Tahun " + str(tahun) + " bukan termasuk tahun kabisat.")
        elif tahun%4==0 :
            print("Tahun " + str(tahun) + " adalah tahun kabisat.")
        else :
            print("Tahun " + str(tahun) + " bukan termasuk tahun kabisat.")
        lanjutkan = input("Ingin melanjutkan perhitungan tahun kabisat (ya/tidak)? ")
        if lanjutkan == "tidak" :
            print("Perhitungan berhenti. Kembali ke menu awal.")
            print()
            break
        else :
            continue    
menu_utama()