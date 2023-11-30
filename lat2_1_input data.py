# latihan input user

data = input("Masukan data: ")  # kode untuk input data

# semua data dari input bertipe string
print("data = ", data, " ", type(data))

# jika ingin mengubah tipe data maka gunakan cara casting
data_integer = int(input("Masukan Angka : "))  # casting tipe data
print("data = ", data_integer, " ", type(data_integer))


# jika boolean ubah dulu ke integer baru ke boolean
biner = bool(int(input("Masukan nilai boolean: ")))

print("data = ", biner, type(biner))
