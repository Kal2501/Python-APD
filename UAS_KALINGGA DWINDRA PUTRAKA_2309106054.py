import os

print("""
Nama : Kalingga Dwindra Putraka
NIM  : 2309106054

Kantin Teknik Baru Universitas Mulawarman
      """)

menu = {
    "001" : {
        "Nama Menu" : "Ayam Geprek",
        "Harga" : 12000
    },
    "002" : {
        "Nama Menu" : "Chicken Katsu",
        "Harga" : 13000
    },
    "003" : {
        "Nama Menu" : "Roti Bakar",
        "Harga" : 6000
    },
    "004" : {
        "Nama Menu" : "Cappucino",
        "Harga" : 5000
    },
    "005" : {
        "Nama Menu" : "Indomie",
        "Harga" : 10000
    }
}

custom_menu = {
    "Telur" : 2000,
    "Sawi"  : 3000,
    "Pedas" : 2000,
    "Ice"   : 1000
}

rasa_rotibakar={
    "1. ":"Coklat",
    "2. ":"Keju",
    "3. " :"Strawberry"
}

indomie={
    "1. ":"Kuah",
    "2. ":"Goreng"
}

def QuickSort(dictionary, key):
    if len(dictionary) <= 1:
        return dictionary

    pivot_key, pivot_value = dictionary.popitem()
    less, equal, greater = {}, {pivot_key: pivot_value}, {}

    for dict_key, dict_value in dictionary.items():
        if dict_value[key] < pivot_value[key]:
            less[dict_key] = dict_value
        elif dict_value[key] == pivot_value[key]:
            equal[dict_key] = dict_value
        else:
            greater[dict_key] = dict_value

    sorted_less = QuickSort(less, key)
    sorted_greater = QuickSort(greater, key)

    return {**sorted_less, **equal, **sorted_greater}

menu_setelah = QuickSort(menu, key='Harga')

def menu_utama():
    total=[]
    while True:
        for i,j in menu_setelah.items():
            print(f"ID : {i}")
            for ket, desc in j.items():
                print(f"{ket} : {desc}")
        print()
        pilih=input("Masukkan ID hidangan untuk memesan (press(0) for exit): ")
        if pilih=="001":
            total.append(menu["001"]["Harga"])
        elif pilih=="002":
            total.append(menu["002"]["Harga"])
            while True:
                maks=0
                for i,tambahan in enumerate(custom_menu):
                    print(f"{i+1}. {tambahan}")
                custom_order=input("Ingin menambahkan apa (press(0) for exit)?: ")
                print()
                if custom_order=="3":
                    total.append(custom_menu["Pedas"])
                    maks+=1
                elif custom_order=="0":
                    break
                if maks==1:
                    break
                else:
                    print("Tambahan tidak tersedia untuk menu ini.")
        elif pilih=="003":
            total.append(menu["003"]["Harga"])
            for i,j in rasa_rotibakar.items():
                    print(f"{i}{j}")
            custom_roti=input("Pilih rasa roti bakar: ")
            print()
            if custom_roti=="1":
                continue
            if custom_roti=="2":
                continue
            if custom_roti=="3":
                continue
            else:
                print("Rasa tidak tersedia.")
        elif pilih=="004":
            total.append(menu["004"]["Harga"])
            while True:
                maks=0
                for i,tambahan in enumerate(custom_menu):
                    print(f"{i+1}. {tambahan}")
                custom_order=input("Ingin menambahkan apa (press(0) for exit)?")
                print()
                if custom_order=="4":
                    total.append(custom_menu["Ice"])
                    maks+=1
                elif custom_order=="0":
                    break
                if maks==1:
                    break
                else:
                    print("Tambahan tidak tersedia untuk menu ini.")
        elif pilih=="005":
            total.append(menu["005"]["Harga"])
            while True:
                for i,j in rasa_rotibakar.items():
                    print(f"{i}{j}")
                custom_roti=input("Pilih varian: ")
                print()
                if custom_roti=="1":
                    continue
                if custom_roti=="2":
                    continue
                else:
                    print("Rasa tidak tersedia.")
                while True:
                    maks=0
                    for i,tambahan in enumerate(custom_menu):
                        print(f"{i+1}. {tambahan}")
                    custom_order=input("Ingin menambahkan apa (press(0) for exit)?")
                    print()
                    if custom_order=="3":
                        total.append(custom_menu["Pedas"])
                        maks+=1
                    elif custom_order=="2":
                        total.append(custom_menu["Sawi"])
                        maks+=1
                    elif custom_order=="1":
                        total.append(custom_menu["Telur"])
                        maks+=1
                    elif custom_order=="0":
                        break
                    if maks==1:
                        break
                    else:
                        print("Tambahan tidak tersedia untuk menu ini.")
        elif pilih == "0":
            break
        else:
            print("ID hidangan tidak tersedia.")

    print()
    print("Berikut isi keranjang anda")
    for i in total :
        print("Rp.", i)
    print()
    while True :
        validasi=input("Ingin melanjutkan ke tahap pembayaran(y/n)?")
        if validasi.lower() == "y":
            os.system('cls')
            print("Kantin Teknik Baru Universitas Mulawarman")
            print()
            print("Berikut total pesanan anda: ")
            print(f"Rp. {sum(total)}")
            print()
            print("Bawa struk ke kasir untuk pembayaran")
            print("Selamat menikmati!")
            print()
            break
        elif validasi.lower() == "n":
            menu_utama()
        else:
            print("Pilihan tidak tersedia")

menu_utama()