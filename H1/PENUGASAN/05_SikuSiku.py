# Minta pengguna memasukkan jumlah baris
jumlah_baris = int(input("Masukkan jumlah baris: "))

# Loop pertama untuk mengontrol baris
for baris in range(1, jumlah_baris + 1):
    # Loop kedua untuk mengontrol jumlah bintang pada setiap baris
    for bintang in range(1, baris + 1):
        print("*", end=" ")
    # Pindah ke baris berikutnya setelah setiap baris selesai
    print()