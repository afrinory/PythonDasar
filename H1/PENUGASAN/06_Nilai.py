while True:
    nilai = int(input("Masukkan nilai siswa: "))
    
    if nilai >= 75:
        print("Siswa tuntas.")
        break
    else:
        mengulang = input("Nilai kurang dari 75. Apakah Anda ingin mengulang (ya/tidak)? ").lower()
        if mengulang != "ya":
            print("Siswa tidak tuntas.")
            break