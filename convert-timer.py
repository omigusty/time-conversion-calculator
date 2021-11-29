inputUser = int(input("Masukan jumlah detik: "))

print("Konversi dari", inputUser, "adalah: ")

jumlah_jam = inputUser // 3600
print(jumlah_jam, "jam")

jumlah_menit = (inputUser - (jumlah_jam * 3600)) // 60
print(jumlah_menit, "menit")

jumlah_detik = (inputUser - (jumlah_jam * 3600)) % 60
print(jumlah_detik, "detik")
