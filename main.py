# DDP LAB-3

# SOAL 1 - Gunting-Batu-Kertas
# Tuliskan program untuk Soal 1 di bawah ini
playerOne = input("Masukkan pilihan Player-1: ")
playerTwo = input("Masukkan pilihan Player-2: ")

# Gunting mengalahkan Kertas
# Kertas mengalahkan Batu
# Batu mengalahkan Gunting
if (playerOne == "gunting" and playerTwo == "kertas") or (playerOne == "kertas" and playerTwo == "batu") or (playerOne == "batu" and playerTwo == "gunting"):
  print("\nPlayer-1 Menang.")
elif (playerTwo == "gunting" and playerOne == "kertas") or (playerTwo == "kertas" and playerOne == "batu") or (playerTwo == "batu" and playerOne == "gunting"):
  print("\nPlayer-2 Menang.")
elif playerOne == playerTwo:
  print("\nPertandingan seri.")
else:
  print("\nMasukan Salah")




# SOAL 2 - Toko Buku Bekas
# Tuliskan program untuk Soal 2 di bawah ini
jumlahBuku = int(input("\nMasukkan banyaknya buku yang akan dibeli: "))

if jumlahBuku > 50:
  print("\nHarga yang harus dibayar = ", jumlahBuku*10000," rupiah")
elif (jumlahBuku <= 50) and (jumlahBuku >= 26):
  print("\nHarga yang harus dibayar = ", jumlahBuku*15000," rupiah")
elif (jumlahBuku <= 25) and (jumlahBuku >= 11):
  print("\nHarga yang harus dibayar = ", jumlahBuku*18000," rupiah")
else:
  print("\nHarga yang harus dibayar = ", jumlahBuku*20000," rupiah")




# SOAL 3 - Mencetak Persegi
# Tuliskan program untuk Soal 3 di bawah ini
inBilanganBulat = int(input("\nMasukkan sebuah bilangan bulat: "))
for valueBilangan in range(inBilanganBulat):
  if valueBilangan % 2 == 0:
    print("# "*inBilanganBulat)
  else:
    print("$ "*inBilanganBulat)


