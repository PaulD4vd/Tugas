print("=== ANALISIS SAHAM PAK HARTONO ===")
nama_perusahaan = str(input("Masukkan Nama Perusahaan:\t\t:"))
kode_perusahaan = str(input("Massukan Kode Saham\t\t\t:"))
harga_saham = int(input("Masukkan Harga Saham per Lembar (Rp)\t:"))
nilai_buku = int(input("Masukkan Nilai Buku per Saham (Rp)\t:"))

pbv = harga_saham / nilai_buku

if pbv < 1 and pbv != 0 and pbv > 0:
    status = "Undervalued"
elif pbv == 1:
    status = "Fair Value"
elif pbv > 1 and pbv < 5:
    status = "Overvalued"
elif pbv > 5: 
    status = "Bubble"
else:
    status = "invalid number"

print(f"\nNilai PBV Saham {kode_perusahaan} adalah {pbv:,.2f}")
print(f"Kategori\t:{status}")

