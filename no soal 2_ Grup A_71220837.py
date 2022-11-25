print('===== Selamat datang di Toko Andi Tersenyum, selamat belanja!=====')
total=int(input('Total belanja Rp: '))
if(total<100000):
          print(f'tidak ada diskon, maka yang anda bayarkan adalah Rp',total)
elif(total>=1000000):
    diskon=(total-(total*10/100))
    print(f'biaya yang harus di bayar setelah diskon adalah Rp',diskon)
elif(total>=500000):
    diskon=(total-(total*5/100))
    print(f'biaya yang harus di bayar setelah diskon adalah Rp',diskon)
elif(total>=100000):
    diskon=(total-(total*2/100))
    print(f'biaya yang harus di bayar setelah diskon adalah Rp',diskon)
