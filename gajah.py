class Gajah():
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age
    
    def lari(self):
        # print("gajah sedang berlari")
        return "gajah sedang berlari"

hewan = Gajah("Pablo",10)
gajahLari = hewan.lari()
print(hewan)
print(gajahLari)

