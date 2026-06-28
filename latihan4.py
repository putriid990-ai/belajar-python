nilai = int(input("Masukkan nilai ujian kamu (0-100): "))

if nilai >= 90:
    print("Grade A - Luar biasa!")
elif nilai >= 75:
    print("Grade B - Bagus!")
elif nilai >= 60:
    print("Grade C - Cukup")
else:
    print("Grade D - Perlu belajar lebih giat!")
