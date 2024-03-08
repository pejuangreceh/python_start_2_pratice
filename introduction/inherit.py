class Hero:
    def __init__(self,nama,health):
        self.nama = nama
        self.health = health
    def recall():
        print("doing recall")

class Tank(Hero):
    def __init__(self,strength,armor):
        self.speciality = strength
        self.speciality2 = armor

class Mage(Hero):
    def __init__(self,magic,manaregen,intelegence):
        self.speciality = magic
        self.speciality2 = manaregen
        self.speciality3 = intelegence
        
class Assasin(Hero):
    def __init__(self,nama,health,attack,mov_speed):
        super().__init__(nama,health)
        self.speciality = attack
        self.speciality2 = mov_speed

karina = Assasin("Karina",100,50,70)

print(karina.nama)

