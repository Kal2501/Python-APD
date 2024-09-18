Data = {
    "Username" : "032",
    "Password" : "Riva"
}

uname=input("Masukkan Username: ")
pword=input("Masukkan password: ")

if uname in Data.values(["Username"]) and pword in Data.values(["Password"]):
    print("Login berhasil")
else :
    print("Login Gagal")