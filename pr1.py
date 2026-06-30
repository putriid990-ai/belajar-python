# Input data
nama = input("Masukkan nama: ")
matematika = int(input("Nilai Matematika: "))
bahasa_indonesia = int(input("Nilai Bahasa Indonesia: "))
pemrograman = int(input("Nilai Pemrograman: "))

# Hitung rata-rata
rata_rata = (matematika + bahasa_indonesia + pemrograman) / 3

# Menentukan grade
if rata_rata >= 85:
    grade = "A"
elif rata_rata >= 75:
    grade = "B"
elif rata_rata >= 65:
    grade = "C"
elif rata_rata >= 50:
    grade = "D"
else:
    grade = "E"

# Output
print("\n=== HASIL NILAI ===")
print("Nama:", nama)
print("Rata-rata:", round(rata_rata, 2))
print("Grade:", grade)
