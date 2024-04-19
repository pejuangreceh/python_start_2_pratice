import gaji_olahraga
 
nama = input('Nama pelatih:')
kerja = input('Jabatan (1-penuh waktu, 2-paruh waktu):')
if kerja == '1':
   pengalaman = int(input('Pengalaman dalam tahun:'))
   gaji = gaji_olahraga.dapat_penuh_waktu(pengalaman)
elif kerja == '2':
   jam = int(input('Jam bekerja:'))
   gaji = gaji_olahraga.dapat_paruh_waktu(jam)
print(nama, '-', gaji)
