# Aplikasi To-Do List
tugas = []

def tampilkan_tugas():
    if len(tugas) == 0:
        print("Belum ada tugas!")
    else:
        print("\n=== DAFTAR TUGAS ===")
        for i in range(len(tugas)):
            print(i + 1, ".", tugas[i])
        print("====================")

def tambah_tugas():
    t = input("Masukkan tugas baru: ")
    tugas.append(t)
    print("✓ Tugas berhasil ditambahkan!")

def hapus_tugas():
    tampilkan_tugas()
    if len(tugas) > 0:
        nomor = int(input("Hapus tugas nomor berapa? "))
        if nomor >= 1 and nomor <= len(tugas):
            dihapus = tugas[nomor - 1]
            tugas.remove(dihapus)
            print("✓ Tugas", dihapus, "berhasil dihapus!")
        else:
            print("Nomor tidak valid!")

# Program utama
print("=== APLIKASI TO-DO LIST ===")

while True:
    print("\nMenu:")
    print("1. Lihat tugas")
    print("2. Tambah tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

    pilihan = input("\nPilihan kamu (1/2/3/4): ")

    if pilihan == "1":
        tampilkan_tugas()
    elif pilihan == "2":
        tambah_tugas()
    elif pilihan == "3":
        hapus_tugas()
    elif pilihan == "4":
        print("Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid!")
