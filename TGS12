import os
import csv 

hasil_menu = []

nama_file_laporan = "laporan_menu.txt"
nama_file_menu = "menu_kafe.csv"

def baca_menu(nama_file_menu, hasil_menu):
    hasil_menu.clear()

    with open(nama_file_menu, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for baris in reader:
            if baris: # skip baris kosong
                hasil_menu.append(baris)

        hasil_akhir = hasil_menu.pop(0)
    return hasil_menu


def tampilkan_menu(daftar, judul):
    print(f"--- {judul} ---")

    nomor = 0
    for i in daftar:
        nama = i[1]
        harga = i[3]
        nomor += 1
        print(f"{nomor}. {nama} - Rp {harga}")

def buat_laporan(daftar):
    with open(nama_file_laporan, "w", encoding="utf-8") as file:
        file.write("=== LAPORAN MENU KOPI SENJA ===\n")

        nomor_laporan = 0
        for i in daftar:
            nama_laporan = i[1]
            harga_laporan = i[3]
            nomor_laporan += 1

            file.write(f"{nama_laporan} - Rp {harga_laporan}\n")

        file.write(f"Total menu: {len(daftar)}\n")

if os.path.exists(nama_file_menu):
    print("=== Program Menu Kafe Kopi Senja ===\n")
    baca_menu(nama_file_menu, hasil_menu)
    tampilkan_menu(hasil_menu, "Menu Saat Ini")

    print()
    kode = str(input("Masukkan kode menu baru: "))
    # validasi menu baru 
    for j in hasil_menu:
        kode_lama = j[0]

        if kode_lama == kode:
            print("Kode menu sudah ada! Program dihentikan.")
            exit()
        else:
            continue

    nama_menu = str(input("Masukkan nama menu: "))
    kategori = str(input("Masukkan kategori: "))
    harga = int(input("Masukkan harga: Rp "))

    # validasi harga
    if harga <= 0:
        print("Harga tidak valid! Program dihentikan.")
        exit()

    stok = int(input("Masukkan stok: "))

    data_baru = [kode, nama_menu, kategori, harga, stok]

    with open(nama_file_menu, "a", newline="", encoding="utf-8") as file2:
        writer = csv.writer(file2)
        writer.writerow(data_baru)

    print("Menu baru berhasil ditambahkan\n")

    baca_menu_akhir = baca_menu(nama_file_menu, hasil_menu)
    buat_laporan(baca_menu_akhir)


    
    print("Laporan berhasil dibuat\n")

    print("--- laporan_menu.txt ---")
    with open(nama_file_laporan, "r", encoding="utf-8") as file:
        isi = file.read()

    print(isi)
else:
    "File menu_kafe.csv tidak ditemukan ! Program dihentikan."
    exit()
