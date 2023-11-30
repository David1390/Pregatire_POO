class Car:
    def __init__(self,culoare,brand,putere,awd,pret):
        self.culoare = culoare
        self.brand = brand
        self.putere = putere
        self.awd = awd
        self.pret = pret
        self.presiune_roti = [2.5, 2.5, 2.5, 2.5]

    def __eq__(self, other):
        return self.brand == other.brand and self.putere == other.putere

    def __str__(self):
        return f'Masina {self.brand} de culoare {self.culoare} are puterea {self.putere} si costa {self.pret}'

    def umfla_cauciucuri(self, presiune):
        for x in range (0, 4):
            self.presiune_roti[x]+=presiune

    def dezumfla_cauciucuri(self, presiune):
        for i in range(0, 4):
            self.presiune_roti[i] -= presiune

    def afisare_presiune(self):
        for x in self.presiune_roti:
            print(x)

    def scor(self):
        print(self.putere)
class Family_Car(Car):
    def __init__(self,culoare,brand,putere,awd,pret, practicability, suitsupport):
        super().__init__(culoare,brand,putere,awd,pret)
        self.practicability = practicability
        self.suitsupport = suitsupport

    def scor(self):
        print(self.practicability * self.putere)

c1=Car("rosie", "Ferrari", 600, True, 200000)
print(c1)
c1.umfla_cauciucuri(1)
c1.afisare_presiune()
c1.dezumfla_cauciucuri(2)
c1.afisare_presiune()
c2=Car("albastra", "Ferrari", 600, False, 200010)
print (c1 == c2)
fc1=Family_Car("rosie", "Ferrari", 600, True, 200000, 6, False)
print(fc1)
print(fc1.presiune_roti)
fc1.umfla_cauciucuri(1)
fc1.afisare_presiune()
c1.scor()
fc1.scor()
