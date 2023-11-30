class Animal:
    def __init__(self, cine, grupe_animale, hranire, dimensiune, mediu_de_viata, putere_muscare):
        self.cine = cine
        self.grupe_animale = grupe_animale
        self.hranire = hranire
        self.dimensiune = dimensiune
        self.mediu_de_viata = mediu_de_viata
        self.putere_muscare = putere_muscare
        self.dimensiune_mare = 1
        self.dimensiune_medie = 1.5
        self.dimensiune_mica = 2

    def __str__(self):
        return f'{self.cine} sunt {self.grupe_animale}, {self.hranire}, de dimensiuni {self.dimensiune} si sunt animale {self.mediu_de_viata}.'

    def __eq__(self, other):
        return self.cine == other.cine and self.dimensiune == other.dimensiune and self.hranire == other.hranire

    def evolutie(self,putere):
        for x in range (0,5):
            self.putere_muscare +=putere
            print(self.putere_muscare)

    def evolutie2_viteza(self):
        print(self.putere_muscare/20 * self.dimensiune_medie)


a1 = Animal("Crocodilienii","reptile","carnivore","medii","salbatice", 200)
print(a1)
a1.evolutie(138)
a1.evolutie2_viteza()

class Tip_Animal(Animal):
    def __init__(self,cine, grupe_animale, hranire, dimensiune, mediu_de_viata, putere_muscare, specie, culoare):
        super().__init__(cine, grupe_animale, hranire, dimensiune, mediu_de_viata, putere_muscare)
        self.specie = specie
        self.culoare = culoare

    def __str__(self):
        return f'{self.specie} sunt {self.cine} de culoarea {self.culoare}'

    #def evolutie2_viteza(self):
        #print()

a2 = Tip_Animal("Crocodilienii","reptile","carnivore","medii","salbatice", 200, "Caimanii", "verde masliniu")
print(a2)
#a2.evolutie2_viteza()

