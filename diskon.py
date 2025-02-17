harga_jual = input("Masukkan harga jual: ")
diskon = int(harga_jual) * 20 / 100
harga_diskon = int(harga_jual) - int(diskon)

print("harga jual sebelum diskom", harga_jual, "Rupiah")
print("harga jual setelah diskom", harga_diskon, "Rupiah")