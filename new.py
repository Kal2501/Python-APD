a = input("Masukkan jenis kelamin : ")

if a == "laki-laki" :
    b = int(input("Masukkan tinggi : "))
    if b >= 175 :
        print("Anda lolos seleksi")
    else :
        print("Anda tidak lolos seleksi")
elif a == "perempuan" :
    c = int(input("Masukkan tinggi : "))
    if c >= 160 :
        print("Anda lolos seleksi")
    else :
        print("Anda tidak lolos seleksi")