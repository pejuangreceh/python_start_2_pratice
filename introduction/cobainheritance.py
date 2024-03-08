# ini class parent / super class
class Manusia:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

# ini class turunan / inheritance
class Pekerjaan(Manusia):
    pass

manusia1 = Manusia('Elloy',23)
manusia2 = Pekerjaan('Asep',17)

print(manusia1.nama)
print(manusia2.nama)