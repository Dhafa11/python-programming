a = int(input("masukan jumlah siswa: "))

for 1 in range (a) :
    nama = (input("masukan nama siswa : "))
    tugas1 = float(input("masukan nilai tugas ke 1: "))
    tugas2 = float(input("masukan nilai tugas ke 2: "))
    tugas3 = float(input("masukan nilai tugas ke 3: "))

    b = 3

    all = tugas1 + tugas2 + tugas3

    avv = all // b

    if avv >= 70 :
        print("kamu lulus")

    elif avv >= 50 and avv < 70 :
        print("kamu harus di perbaiki")

    else :
        print("kamu tidak lulus")

    print("selamat", nama, "nilai rata rata kamu = ", avv, "semangat balajar")