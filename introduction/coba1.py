inivariabel = 1

class Coba():
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    def tampilkanhobi():
        print("Berenang, Membaca, Main game")
    def tambahkan1(self):
        return self.umur+1

iniclass = Coba('Gaby',16) #bikin objek baru
print(iniclass.nama)
iniclass.tampilkanhobi
print(iniclass.umur)
print(iniclass.tambahkan1())
print(iniclass.tambahkan1())

jawaban = "Thomas A E"

pertanyaan = []

pertanyaan[0][0] = "Siapa penemu bola lampu"
pertanyaan[0][1] = "Jokowi"
pertanyaan[0][2] = "Thomas A E"
pertanyaan[0][3] = "Alexander TG"
pertanyaan[0][4] = "Mark Z"
pertanyaan[0][5] = "Thomas A E"

if pertanyaan[0][5] == jawaban:
    print("benar")
else:
    print("salah")



