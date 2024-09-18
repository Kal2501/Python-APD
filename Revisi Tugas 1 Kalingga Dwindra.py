print("Nama : Kalingga Dwindra Putraka")
print("NIM : 2309106054")
print()
print("Tugas 1 APD : Membuat Program Input Nilai")
print()


while (True) :
    Nilai=(input("Masukkan Nilai (Bilangan Bulat 0-100):"))

    try:
        Nilai=int(Nilai)

        if Nilai <= 100 and Nilai >= 90:
            print("Nilai = A+")
            break
        elif Nilai <= 89 and Nilai >= 80:
            print("Nilai A-")
            break
        elif Nilai <= 79 and Nilai >= 75:
            print("Nilai B+")
            break
        elif Nilai <= 74 and Nilai >= 70:
            print("Nilai B-")
            break
        elif Nilai <= 69 and Nilai >= 65:
            print("Nilai C+")
            break
        elif Nilai <= 64 and Nilai >= 60:
            print("Nilai C-")
            break
        elif Nilai <= 59 and Nilai >= 50:
            print("Nilai D")
            break
        elif Nilai < 50 and Nilai >= 0:
            print("Nilai E")
            break
        else:
            print("Invalid : Masukkan Input yang Sesuai")
            break
    except ValueError:
        print("Invalid : Masukkan Input yang Sesuai")
        break