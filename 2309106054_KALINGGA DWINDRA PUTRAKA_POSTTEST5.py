import os

User = ["Admin"]
Pass = ["AdminGanteng"]
pricemesin=[2500000,2200000]
priceksterior=[7000000,1500000]
priceinterior=[2500000,16000000]

def menu():
    print("Selamat Datang di RR Garage")
    print()
    while True:
        print("Menu Utama")
        print("1. Registrasi Akun")
        print("2. Login Akun")
        print("3. Keluar")
        pilihan = input("Pilih opsi(1/2/3): ")
        os.system('cls')
        if pilihan == '1':
            regis()
            break
        elif pilihan == '2':
            login()
            break
        elif pilihan == '3':
            print("Program berhenti, selamat tinggal.")
            break
        else:
            print("Pilihan tidak valid, kembali ke menu awal.")
            menu()

def regis():
    print("Silahkan buat akun")
    fusername=input("Buat username : ")
    User.append(fusername)
    fpassword=input("Buat password : ")
    Pass.append(fpassword)
    os.system('cls')
    print("Pembuatan akun berhasil!")
    login()

def login():
    while True:
        print()
        username = input("Masukkan username : ")
        password = input("Masukkan password : ")
        os.system('cls')
        if username == User[0] and password == Pass[0]:
            admin()
            break
        elif username in User[1] and password in Pass[1]:
            cust()
            break
        else:
            print("Login gagal")
            menu()

def admin():
    print("Anda memasuki mode admin")
    presensi=str(input("Silahkan lakukan presensi harian anda(Hadir/Tidak Hadir) : "))
    os.system('cls')
    if presensi == "Hadir" :
        print("Kehadiran anda hari ini telah terekam, Terima Kasih.")
        print()
    elif presensi == "Tidak hadir":
        print("Berikan keterangan yang jelas dikemudian hari")
        print("Akses program tidak diperkenankan.")
        menu()
    else :
        print("Pilihan tidak valid, kembali ke menu.")
        menu()
    cekakun=str(input("Cek akun pelanggan(Setuju/Batal)? "))
    if cekakun=="Setuju" :
        print("Username: ", User[1])
        print("Password: ", Pass[1])
        hapus=str(input("Ingin menghapus akun pelanggan(Setuju/Batal)? "))
        os.system('cls')
        if hapus=="Setuju":
            del User[1]
            del Pass[1]
            print("Penghapusan akun berhasil.")
            menu()
        elif hapus=="Batal":
            admin()
    elif hapus=="Batal":
        menu()
    else:
        print("Pilihan tidak valid, kembali ke menu awal.")
        menu()

def cust():
    print("Apapun keinginan anda, kami siap melayani anda")
    total=[]
    mobil=str(input("Masukkan merk dan nama mobil anda : "))
    mobil
    while True:
        print("Bagian mobil apa yang ingin anda modifikasi?")
        print("1. Mesin")
        print("2. Eksterior")
        print("3. Interior")
        print("4. Cukup modifikasinya.")
        bagian=int(input("Pilih ya(1/2/3/4): "))
        os.system('cls')
        if bagian == 1:
            modzmesin=0
            print("Kami memiliki beberapa opsi untuk sektor mesin")
            print("1. Tune up")
            print("2. Maintenance")
            mesin=int(input("Pilih ya(1/2): "))
            if mesin==1:
                total.append(pricemesin[0])
                modzmesin+=1
            elif mesin==2:
                total.append(pricemesin[1])
                modzmesin+=1
        elif bagian == 2:
            modzeks=0
            print("Kami memiliki beberapa opsi untuk modifikasi eksterior")
            print("1. Bodykit")
            print("2. Body Painting")
            eksterior=int(input("Pilih ya(1/2): "))
            if eksterior==1:
                total.append(priceksterior[0])
                modzeks+=1
            elif eksterior==2:
                total.append(priceksterior[1])
                modzeks+=1
        elif bagian == 3:
            modzint=0
            print("Kami memiliki beberapa opsi untuk sektor interior")
            print("1. Detailing")
            print("2. Audio by ALPINE")
            interior=int(input("Pilih ya(1/2): "))
            if interior==1:
                total.append(priceinterior[0])
                modzint+=1
            elif interior==2:
                total.append(priceinterior[1])
                modzint+=1
            else:
                print("Pilih sesuai opsi yang tersedia.")
                continue
        elif bagian == 4:
            break
    print("Berikut isi keranjang anda")
    for i in total :
        print("Rp.", i)
    totalbayar=sum(total)
    print()
    print("Total harga dari keranjang anda : ")
    print("Rp.", totalbayar)
    setuju=str(input("Konfirmasi belanja anda?(Setuju/Batal): "))
    if setuju == "Setuju":
        print("Terima Kasih telah menggunakan jasa kami, silahkan print struk dan bawa ke RR Garage terdekat.")
        print()
    elif setuju == "Batal" :
        os.system('cls')
        total.clear()
        menu()

menu()