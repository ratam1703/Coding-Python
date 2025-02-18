jumlah_domba = input("Masukkan jumlah domba yang di beli: ")
harga_dasar_domba = 2500000
harga_jual_domba = 3000000
keuntungan_jual_domba = int(harga_jual_domba) - int(harga_dasar_domba)
total_modal_dikeluarkan = int(jumlah_domba) * int(harga_dasar_domba) 
total_keuntungan_jual_domba = int(jumlah_domba) * int(keuntungan_jual_domba) 
total_modal_dikeluarkan_dan_keuntungannya = int(total_modal_dikeluarkan) + int(total_keuntungan_jual_domba) 

print("total modal di keluarkan", total_modal_dikeluarkan, "Rupiah")
print("total keuntungan jual domba", total_keuntungan_jual_domba, "Rupiah")
print("total modal dan keuntungannya", total_modal_dikeluarkan_dan_keuntungannya, "Rupiah")