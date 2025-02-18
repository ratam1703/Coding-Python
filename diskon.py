harga_awal = input("Masukkan harga jual: ")
diskon = int(harga_awal) * 20 / 100
harga_diskon = int(harga_awal) - int(diskon)

print("harga jual sebelum diskom", harga_awal, "Rupiah")
print("harga jual setelah diskom", harga_diskon, "Rupiah")