while(True):

    try:
        tahun = int(input("Masukkan tahun : "))
        if tahun%400==0 :
            print("Tahun " + str(tahun) + " adalah tahun kabisat.")
            break
        elif tahun%100==0 :
            print("Tahun " + str(tahun) + " bukan termasuk tahun kabisat.")
            break
        elif tahun%4==0 :
            print("Tahun " + str(tahun) + " adalah tahun kabisat.")
            break
        else :
            print("Tahun " + str(tahun) + " bukan termasuk tahun kabisat.")
            break
    except ValueError:
        print("Input yang anda masukkan tidak sesuai, silahkan masukkan kembali.")

print("Program berakhir.")
    