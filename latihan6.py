def cek_nilai(nilai):
    if nilai >= 90:
        return "Grade A - Luar biasa!"
    elif nilai >= 75:
        return "Grade B - Bagus!"
    elif nilai >= 60:
        return "Grade C - Cukup"
    else:
        return "Grade D - Perlu belajar lebih giat!"

# Program utama
nama = input("Nama kamu: ")
nilai = int(input("Nilai ujian kamu: "))

hasil = cek_nilai(nilai)
print(nama, "mendapat", hasil)
