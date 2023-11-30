# Belajar Tipe Data pada python


from ctypes import c_double
integer = 11
print(integer, type(integer))  # mencetak variabel dan cek type/tipe data

float = 1.1
print(float, type(float))  # mencetak variabel dan cek type/tipe data

string = "10"
print(string, type(string))  # mencetak variabel dan cek type/tipe data

boolean = True
print(boolean, type(boolean))  # mencetak variabel dan cek type/tipe data


# tipe data khusus
# tipe data complex
complex = complex(5, 6)
print(complex, type(complex))

# tipe data bahasa C
# untuk menggunakan tipe bahasa C jika dibutuhkan
# from ctypes import c_double
c_double = c_double(10.5)
print(c_double, type(c_double))
