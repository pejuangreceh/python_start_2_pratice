import aturan_olahraga
print('Program hari ini:\n1 - sepak bola\n2 - hoki\n3 - balapan 100 meter')
jawaban = input('Pilihan Anda (off - keluar):')
while jawaban != 'off':
   if jawaban == '1':
       aturan_olahraga.cetak_sepakbola()
   elif jawaban == '2':
       aturan_olahraga.cetak_hoki()
   elif jawaban == '3':
       aturan_olahraga.cetak_sprint()
   else:
       print('Olahraga tidak ditemukan!')
   jawaban = input('Pilihan Anda (off - keluar):')