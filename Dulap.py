class Dulap:
    def __init__(self, pret,dimensiuni,culoare,material,greutate):
        self.culoare = culoare
        self.dimensiuni = dimensiuni
        self.material = material
        self.greutate = greutate
        self.pret = pret

    def __str__(self):
        return f'Dulapul la pret de {self.pret} are dimensiunile de {self.dimensiuni},culoarea {self.culoare}, ca si material a fost folosit {self.material} si are o greutate de {self.greutate}kg.'

    def __eq__(self, other):
        return self.culoare == other.culoare and self.dimensiuni == other.dimensiuni

d1=Dulap("2,769 RON", "200x200x62", "negru mat", "stejar artisan", 162)
d2=Dulap("2,769 RON", "200x150x62", "alb", "stejar artisan", 162)
print(d1)
print(d1 == d2)
