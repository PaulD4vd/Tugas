user = str(input("Masukkan username\t: "))
password = int(input("Masukkan password\t: "))

if user == "david" and password == 3827 and user != " " and password != 0:
    print(f"\nLogin berhasil. Welcome {user}!\n")

    print("="*5 + " " + "TOKO MAS BRAM" + " " + "="*5 )
    print("1. Philips")
    print("2. Miyako")
    print("3. EXIT")

    pilihan = int(input("\nPilih brand: "))

    if pilihan == 1:
        print(" ")
        brand = "Philips"
        print(f"{brand} HR2115")
        print(f"{brand} HR2221")
        print(f"{brand} HR2223")

        print(" ")
        brand_1 = int(input("Masukkan tipe blender: "))
        print(" ")

        if brand_1 == 1:
            brand_1_nama = "HR2115"
            brand_1_harga = 500000
            brand_1_bonus = "1 buah spatula mini"
        elif brand_1 == 2:
            brand_1_nama = "HR2221"
            brand_1_harga = 800000
            brand_1_bonus = "1 buah spatula mini dan 1 gelas ukur"
        elif brand_1 == 3:
            brand_1_nama = "HR2223"
            brand_1_harga = 1100000
            brand_1_bonus = "2 buah spatula mini, 1 gelas ukur, dan garansi 6 bulan"
        else:
            print("\n[!] Tipe tersebut tidak ada dalam daftar")

        print(" ")
        brand_1_sum = int(input("Masukkan jumlah blender: "))
        print(" ")

        if brand_1_sum > 8:
            if brand_1 == 1:
                potongan1 = 50000
            elif brand_1 == 2:
                potongan1 = 100000
            elif brand_1 == 3:
                potongan1 = 150000
        else:
            potongan1 = 0
    
        print(" ")
        brand_1_member = str(input("Masukkan jenis member (Gold/Silver/None): "))
        print(" ")

        if brand_1_member.lower() == "gold":
            potongan1_member = 10/100
        elif brand_1_member.lower() == "silver":
            potongan1_member = 5/100
        else:
            potongan1_member = 0

        print("="*4 + " Data Pembelian " + "="*4)
        print(f"Nama\t\t:{user}")
        print(f"Tipe\t\t:{brand_1_nama}")
        print(f"Jumlah\t\t:{brand_1_sum}")
        total_harga1 = brand_1_harga * brand_1_sum
        potongan1_biasa = total_harga1 - potongan1
        potongan1_member_fix = potongan1_biasa * potongan1_member
        total_harga_potongan = potongan1_biasa - potongan1_member_fix

        print(f"Total Harga\t:Rp {total_harga_potongan}")
        print(f"Mendapatkan bonus {brand_1_bonus}")

    elif pilihan == 2:
        print(" ")
        brand = "Miyako"
        print(f"{brand} BL-101 PL")
        print(f"{brand} BL-152 PF")
        print(f"{brand} CH-501")

        print(" ")
        brand_2 = int(input("Masukkan tipe blender: "))
        print(" ")

        if brand_2 == 1:
           brand_2_nama = "BL-101 PL"
           brand_2_harga = 300000
           brand_2_bonus = "1 buah sendok takar"
        elif brand_2 == 2:
             brand_2_nama = "BL-152 PF"
             brand_2_harga = 450000
             brand_2_bonus = "1 buah sendok takar dan 1 gelas ukur"
        elif brand_2 == 3:
             brand_2_nama = "CH-501"
             brand_2_harga = 600000
             brand_2_bonus = "2 buah sendok takar, 1 gelas ukur, dan garansi 1 tahun"
        else:
            print("\n[!] Tipe tersebut tidak ada dalam daftar")

        print(" ")
        brand_2_sum = int(input("Masukkan jumlah blender: "))
        print(" ")

        if brand_2_sum > 8:
           Bonus = True
           if brand_2 == 1:
              potongan2 = 50000
           elif brand_2 == 2:
              potongan2 = 100000
           elif brand_2 == 3:
              potongan2 = 150000
        else: 
            Bonus = False 

        print(" ")
        brand_2_member = str(input("Masukkan jenis member (Gold/Silver/None): "))
        print(" ")
        
        if brand_2_member.lower() == "gold":
            potongan2_member = 10/100
        elif brand_2_member.lower() == "silver":
            potongan2_member = 5/100
        else:
            potongan2_member = 0

        print("="*4 + " Data Pembelian " + "="*4)
        print(f"Nama\t\t:{user}")
        print(f"Tipe\t\t:{brand_2_nama}")
        print(f"Jumlah\t\t:{brand_2_sum}")
        
        total_harga2 = brand_2_harga * brand_2_sum
        potongan2_biasa = total_harga2 - potongan2
        potongan2_member_fix = potongan2_biasa * potongan2_member
        total_harga_potongan = potongan2_biasa - potongan2_member_fix
        
        print(f"Total Harga\t:Rp {total_harga_potongan}")
        print(f"Mendapatkan bonus {brand_2_bonus}")
        
                
    else:
        print("Brand tidak tersedia")

else: 
    print("!! username dan password gagal !!")
    print("!! Login dan Gagal !!")

