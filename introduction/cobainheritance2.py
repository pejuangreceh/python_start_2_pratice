# ini class parent / super class
class Manusia:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def showInfo(self):#method dari parent
        print("{} berumur : {}".format(self.nama,self.umur))

# ini class turunan / inheritance
class Guru(Manusia):
    def __init__(self,nama,umur):#constructor punya guru
        # Manusia.__init__(self,nama,23)
        super().__init__(nama,umur)
        super().showInfo()
        # Manusia.showInfo(self)

class Murid(Manusia):
    def __init__(self,nama,murid):
        self.nama = nama
        self.umur = 17
        self.namamurid = murid
manusia1 = Manusia('Yabes',27)
# ini class turunan / inheritance
manusia2 = Guru('Guru',23)
manusia3 = Murid('Murid',"Romy")
manusia4 = Murid('Murid',"Tata")


print(manusia2.nama ," ",manusia2.umur)
print(manusia3.nama ," ",manusia3.umur, " ",manusia3.namamurid)
print(manusia4.nama ,"-----",manusia4.umur, "----",manusia4.namamurid)

print("nama = ", manusia1.nama)
print("umur = ", manusia1.umur)