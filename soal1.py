stok_kafe = [
    ["Biji Kopi Arabica", "Bahan Utama", 120000, 15],
    ["Susu UHT", "Bahan Tambahan", 18000, 24]
]

print("="*3 + " " + "DATA STOK AWAL" + " " + "="*3)
print(stok_kafe)

bahan_baru = str(input("\nMasukkan Nama Bahan Baru: "))
kategori = str(input("Masukkan Kategori: "))
harga_satuan = int(input("Masukkan Harga Satuan :"))
jumlah_stok = int(input("Masukkan Jumlah Stok: "))

stok_kafe.append([bahan_baru, kategori, harga_satuan, jumlah_stok])
print()
print("="*3 + " " + "Data Setelah Penambahan" + " " + "="*3)
print(stok_kafe)

stok_kurang_arabica = int(input("\nMasukkan Jumlah Biji Arabica yang terpakai: ")) 
operasi_penguranan = stok_kafe[0][3] - stok_kurang_arabica # kurangi value
stok_kafe[0][3] = operasi_penguranan # tambahan value

print()
print("="*3 + " " + "Data Setelah Penambahan" + " " + "="*3)
print(stok_kafe)
print()

indeks_hapus = int(input("Masukkan indeks bahan yang ingin dihapus: "))
stok_kafe.pop(indeks_hapus)
print("=== Data Final ===")
print(stok_kafe)
