print("""
Nama  : Kalingga Dwindra Putraka
NIM   : 2309106054
      """)
#Memasukkan data berupa 20 data Numerik bilangan bulat kedalam sebuah LISTS.
Data = []
for i in range(20) :
    try :
        DataNumerik = int(input("Masukkan bilangan bulat ke dalam list : "))
        Data.append(DataNumerik)
    except ValueError:
        print("Input yang anda masukkan tidak sesuai!")
print()
#Menampilkan data yang telah diinput.
print(Data)
print()
#Menghitung berapa banyak data yang dimasukkan berupa bilangan genap, dab berapa yang bilangan ganjil.
ganjil = 0
genap = 0
for DataNumerik in Data :
    if DataNumerik%2 == 0 :
        genap += 1
    else :
        ganjil += 1 

print("Jumlah bilangan ganjil pada list adalah : ", ganjil)
print("Jumlah bilangan genap pada list adalah : ", genap)
print()
#Mengurutkan data yang ada dalam Lists.
DataUrut = sorted(Data)
print(DataUrut)


