print("<==========TOM SUSHI>==========")

total = 0
nama = input("Masukkan Nama: ")
print("\nhalo selamat datang",nama)

rincian = ""

while True:
    print("\n<=====MENU MAKANAN=====>")
    print("1. Chicken Katsu          - Rp20.000")
    print("2. Salmon Sashimi         - Rp25.000")
    print("3. Tomago Sushi           - Rp15.000")
    print("4. Inari Spicy Chicken    - Rp25.000")
    print("5. Takoyaki               - Rp30.000")
    print("0. Selesai Memilih")

    pilihan = int(input("Pilih menu (0-5): "))

    if pilihan == 0:
            break
    
    elif pilihan == 1:
            harga = 20000
            nama_menu = "Chicken Katsu"
    
    elif pilihan == 2:
            harga = 25000
            nama_menu = "Salmon Sashimi"
    
    elif pilihan == 3:
            harga = 15000
            nama_menu = "Tomogo Sushi"
    
    elif pilihan == 4:
            harga = 25000
            nama_menu = "Inari Spicy Chicken"
    
    elif pilihan == 5:
            harga = 30000
            nama_menu = "Takoyaki"
    
    else:
            print("Pilihan tidak tersedia!")
            continue
    
    jumlah = int(input("Masukkan jumlah pesanan: "))
    
    if jumlah <= 0:
            print("Jumlah pesanan harus lebih dari 0!")
            continue
    
    subtotal = harga * jumlah
    total = total + subtotal
    
    print("\nPesanan berhasil!")
    print("Menu:", nama_menu)
    print("Harga:", harga)
    print("Jumlah:", jumlah)
    print("Subtotal:", subtotal)
    print("Total sementara:", total)
    
    rincian = rincian + "\nMenu     : " + nama_menu
    rincian = rincian + "\nHarga    : Rp " + str(harga)
    rincian = rincian + "\nJumlah   : " + str(jumlah)
    rincian = rincian + "\nSubtotal : Rp " + str(subtotal) + "\n"
    
    if total > 200000:
        persen_diskon = 20
        diskon = total * 0.20
    else:
        persen_diskon = 0
        diskon = 0
    total_bayar = total - diskon
    
    print("\n<================================>")
    print("       STRUK PEMBAYARAN")
    print("Nama Pelanggan:", nama)
    
    print(rincian)
    
    print("<==============================>")
    print("Total Belanja :Rp",total)
    print("Diskon        :", str(persen_diskon) + "%")
    print("Diskon        :Rp",diskon)
    print("<==================================>")
    print("Total Bayar   :Rp",total_bayar)
    
    print("<==================================>")
    print("             TERIMA KASIH")
    print("   selamat menikmati makanannya kak",nama)
    print("       Silahkan Datang Kembali 🔄")