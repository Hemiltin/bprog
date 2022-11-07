def jualan():
    a = "capucino"
    b = "teh"
    print ("Pilihan")
    print ("1.", a)
    print ("2.", b)
    print ("3. Exit")

def capucino():
    cap = "memilih capucino"
    print(cap)
    capucino = int(input("masukkan harga : "))
    ppn = 10/100
    hargapajak = capucino*ppn
    total = capucino+hargapajak
    print("Jumlah yang harus dibayarkan " + str(total))

def teh():
    te = "memilih TEH"
    print(te)
    teh = int(input("masukkan harga : "))
    ppn = 10/100
    hargapajak = teh*ppn
    total = teh+hargapajak
    print("Jumlah yang harus dibayarkan " + str(total))

def welcome():
    nim = 20210801147
    nama = "Hemiltin Adilah"
    print ("NIM : ", nim)
    print ("NAMA : ", nama)

while True:
    welcome()
    jualan()
    pil = int(input("masukkan pilihan : "))
    if pil == 1:
        capucino()
    elif pil == 2:
        teh()
    elif pil == 3:
        break
    else:
        print ("pilihan salah")