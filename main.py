# DDP LAB-3

# SOAL 1 - Gunting-Batu-Kertas
# Tuliskan program untuk Soal 1 di bawah ini
# Simpan masukan banyaknya angka kedalam variabel playerOne dan playerTwo
playerOne = input("Masukkan pilihan Player-1: ")
playerTwo = input("Masukkan pilihan Player-2: ")

# Sistem melakukan pengecekan dengan kondisi jika
# Player-1 menginputkan Gunting dan Player-2 menginputkan Kertas maka Player-1 menang
# Player-1 menginputkan Kertas dan Player-2 menginputkan Batu maka Player-1 menang
# Player-1 menginputkan Batu dan Player-2 menginputkan Gunting maka Player-1 menang
if (playerOne == "gunting" and playerTwo == "kertas") or (playerOne == "kertas" and playerTwo == "batu") or (playerOne == "batu" and playerTwo == "gunting"):
  print("Player-1 Menang.")
elif (playerTwo == "gunting" and playerOne == "kertas") or (playerTwo == "kertas" and playerOne == "batu") or (playerTwo == "batu" and playerOne == "gunting"):
  print("Player-2 Menang.")
elif playerOne == playerTwo:
  print("Pertandingan seri.")
else:
  print("Masukan Salah")




# SOAL 2 - Toko Buku Bekas
# Tuliskan program untuk Soal 2 di bawah ini
# Simpan masukan banyaknya buku kedalam variabel jumlahBuku
jumlahBuku = int(input("\nMasukkan banyaknya buku yang akan dibeli: "))

# Jika jumlahBuku lebih dari 50 maka akan dikalikan 10000
if jumlahBuku > 50:
  print("Harga yang harus dibayar = ", jumlahBuku*10000," rupiah")
# Jika jumlahBuku lebih dari 50 maka akan dikalikan 15000
elif (jumlahBuku <= 50) and (jumlahBuku >= 26):
  print("Harga yang harus dibayar = ", jumlahBuku*15000," rupiah")
# Jika jumlahBuku lebih dari 50 maka akan dikalikan 18000
elif (jumlahBuku <= 25) and (jumlahBuku >= 11):
  print("Harga yang harus dibayar = ", jumlahBuku*18000," rupiah")
# Jika jumlahBuku lebih dari 50 maka akan dikalikan 20000
else:
  print("Harga yang harus dibayar = ", jumlahBuku*20000," rupiah")




# SOAL 3 - Mencetak Persegi
# Tuliskan program untuk Soal 3 di bawah ini
# Simpan masukan sebuah bilangan bulat kedalam variabel inBilanganBulat
inBilanganBulat = int(input("\nMasukkan sebuah bilangan bulat: "))
# Lakukan perulangan sebanyak nilai yang ada di variabel inBilanganBulat
for valueBilangan in range(inBilanganBulat):
  # Jika nilai perulangan modulo 2 dan nilainya 0 maka print #
  if valueBilangan % 2 == 0:
    print("# "*inBilanganBulat)
  # Jika nilai perulangan modulo 2 dan nilainya bukan 0 maka print $
  else:
    print("$ "*inBilanganBulat)


