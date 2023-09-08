# Meminta pengguna untuk memasukkan rentang angka
awal = int(input("Masukkan angka pertama: "))
akhir = int(input("Masukkan angka kedua: "))

print(f"Bilangan ganjil antara {awal} dan {akhir}:")
for num in range(awal, akhir + 1):
    if num % 2 != 0:
        print(num)

print(f"Bilangan genap antara {awal} dan {akhir}:")
for num in range(awal, akhir + 1):
    if num % 2 == 0:
        print(num)

# mengetahui angka ganji atau genap
angka = int(input("Masukkan angka: "))

# Periksa apakah angka ganjil atau genap
if angka % 2 == 0:
    print(angka, "adalah angka genap.")
else:
    print(angka, "adalah angka ganjil.")