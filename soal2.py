pesanan_pelanggan = {
    "meja_1": {
        "nama": "Rina",
        "menu": "Kopi Susu Gula Aren",
        "harga_satuan": 25000,
        "jumlah": 2
    }
}

pesanan_pelanggan["meja_1"]["jumlah"] + 1
total_tagihan = pesanan_pelanggan["meja_1"]["harga_satuan"] 
pesanan_pelanggan["meja_1"]["total_tagihan"] 

print("=== Data Meja 1 Setelah Penambahan Pesanan ===")
print(f"Nama Pelanggan   : {pesanan_pelanggan['meja_1']["nama"]}")
print(f"Menu\t\t : {pesanan_pelanggan['meja_1']["menu"]}")
print(f"Harga Satuan     : {pesanan_pelanggan['meja_1']["harga_satuan"]}")
print(f"Jumlah\t\t : {pesanan_pelanggan['meja_1']['jumlah']} ")
print(f"Total Tagihan    : {pesanan_pelanggan['meja_1']["total_tagihan"]}")


nama = str(input("\nMasukkan Nama Pelanggan Meja 2: "))
menu_pelanggan = str(input("Masukkan Menu: "))
harga_satuan = int(input("Masukkan Harga Satuan: "))
jumlah = int(input("Masukkan Jumlah: "))
total_tagihan2 = harga_satuan * jumlah

print("\n=== Sisa Pesanan Setelah Meja 1 Pulang ===")

pesanan_pelanggan["meja_2"] = {
    "nama" : nama,
    "menu" : menu_pelanggan,
    "harga_satuan" : harga_satuan,
    "jumlah" : jumlah,
    "total_tagihan" : total_tagihan2

}
print("\n--- Meja 2 ---")
print(f"Nama Pelanggan   : {pesanan_pelanggan['meja_2']["nama"]}")
print(f"Menu\t\t : {pesanan_pelanggan['meja_2']["menu"]}")
print(f"Harga Satuan     : {pesanan_pelanggan['meja_2']["harga_satuan"]}")
print(f"Jumlah\t\t : {pesanan_pelanggan['meja_2']['jumlah']} ")
print(f"Total Tagihan    : {pesanan_pelanggan['meja_2']["total_tagihan"]}")
