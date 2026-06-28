def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error! Tidak bisa bagi dengan 0"
    return a / b

# Program utama
print("=== KALKULATOR SEDERHANA ===")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("Pilih operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

pilihan = input("Pilihan kamu (1/2/3/4): ")

if pilihan == "1":
    print("Hasil:", tambah(angka1, angka2))
elif pilihan == "2":
    print("Hasil:", kurang(angka1, angka2))
elif pilihan == "3":
    print("Hasil:", kali(angka1, angka2))
elif pilihan == "4":
    print("Hasil:", bagi(angka1, angka2))
else:
    print("Pilihan tidak valid!")
