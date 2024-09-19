
jumlah_pembeli = int(input("Masukkan jumlah pembeli: "))

total_harga = 0

for i in range(jumlah_pembeli):
    print(f"\nPembeli {i+1}:")
    usia = int(input("Masukkan usia pembeli: "))
    jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))

    Anak = 30000
    dewasa = 50000
    lansia = 35000

if usia<12:
    print(30000*jumlah_tiket)
elif 12<= usia <=60:
    print(50000*jumlah_tiket)
else:
    print(35000*jumlah_tiket)
    
    harga = (usia, jumlah_tiket)
    total_harga += harga
    
    print(f"Harga tiket untuk pembeli {i+1}: Rp {harga}")