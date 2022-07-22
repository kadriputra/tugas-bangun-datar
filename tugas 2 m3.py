namaSaya = input("Masukkan Nama anda : ")
nim = input("Masukkan NIM anda : ")
print()

print("-------------------------------")
print("     Selamat datang",namaSaya)
print("       Dengan NIM", nim)
print("--------------------------------")
print()

print("Soal No 1")
print("Diketahui sisi = 6, sebutkan Nama dan hitunglah Luas Bangun Datar tersebut!")
namaBD = input("Nama Bangun Datar : ")
sisi1 = int(input("sisi : "))
sisi2 = int(input("sisi : "))
hasil = sisi1*sisi2
print("Bangun Datar tersebut adalah",namaBD,"dan luas Bangun Datar tersebut",hasil)
print()

print("Soal No 2")
print("Diketahui alas = 7, tinggi = 8, hitunglah Luas Bangun Datar tersebut!")
namaBD2 = input("Nama Bangun Datar : ")
alas = int(input("Alas : "))
tinggi = int(input("Tinggi : "))
hasil2 = (alas*tinggi) / 2
print("Bangun datar tersebut adalah",namaBD2,"dan Luas Bangun Datar tersebut adalah",hasil2)
print()

print("Soal No 3")
print("Diketahui panjang = 9, lebar = 4, Sebutkan Nama dan hitunglah Luas Bangun Datar tersebut!")
namaBD3 = input("Nama Bangun Datar : ")
panjang = int(input("Panjang : "))
lebar = int(input("Lebar : "))
hasil3 = panjang*lebar
print("Bangun datar tersebut adalah",namaBD3,"dan Luas Bangun Datar tersebut adalah",hasil3)
print()

print("Soal No 4")
print("Diketahui Jari-jari = 56, Sebutkan Nama dan hitunglah Luas Bangun Datar tersebut!")
namaBD4 = input("Nama Bangun Datar : ")
phi = float(input("π : "))
r = float(input("r : "))
hasil4 = phi*r*r
print("Bangun datar tersebut adalah",namaBD4,"dan Luas Bangun Datar tersebut adalah",hasil4)
print()

print("Soal No 5")
print("Diketahui Diagonal I = 4, Diagonal II = 8, Sebutkan Nama dan hitunglah Luas Bangun Datar tersebut!")
namaBD5 = input("Nama Bangun Datar : ")
x = float(input("Diagonal I : "))
y = float(input("Diagonal II : "))
hasil5 = 0.5*x*y
print("Bangun datar tersebut adalah",namaBD5,"dan Luas Bangun Datar tersebut adalah",hasil5)
print()

print("Soal No 6")
print("Diketahui sisi AB dan CD sejajar, sisi AB = 6, sisi CD = 8, tinggi = 3, Sebutkan Nama dan hitunglah Luas Bangun Datar tersebut!")
namaBD6 = input("Nama Bangun Datar : ")
ab = float(input("sisi AB : "))
cd = float(input("sisi CD : "))
t = float(input("Tinggi : "))
hasil6 = (ab+cd)*t/2
print("Bangun datar tersebut adalah",namaBD6,"dan Luas Bangun Datar tersebut adalah",hasil6)
print()

print("Soal No 7")
print("Diketahui sebuah Jajar Genjang dengan alas = 9, tinggi = 7. Hitunglah Luas Bangun Datar tersebut!")
alas1 = int(input("Alas : "))
tinggi1 = int(input("Tinggi : "))
hasil7 = alas1*tinggi1
print("Luas Jajar Genjang tersebut adalah",hasil7)
print()

print("terima kasih")