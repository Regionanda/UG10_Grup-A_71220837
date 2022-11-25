nama=input('Masukan nama mahasiswa: ')
nim=input('Masukan NIM-nya: ')

if nim[2:4]== '22':
    print(nim,'merupakan mahasiswa informatika angkatan 20 hingga 22')
    
elif nim[2:4]== '21':
    print(nim,'merupakan mahasiswa informatika angkatan 20 hingga 22')
elif nim[2:4]== '20':
    print(nim,'merupakan mahasiswa informatika angkatan 20 hingga 22')
else:
    print('bukan mahasiswa informatika angkatan 20 hingga 22')
