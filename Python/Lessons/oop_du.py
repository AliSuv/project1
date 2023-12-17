import math

class Tvar:
    def __init__(self):
        pass
    def vypocet_obvodu(self):
        pass
    def vypocet_obsahu(self):
        pass

class Ctverec(Tvar):
    def __init__(self, strana):
        self.strana = strana
    def vypocet_obvodu(self):
        return 4 * self.strana
    def vypocet_obsahu(self):
        return self.strana ** 2

class Trojuhelnik(Tvar):
    def __init__(self, strana_a, strana_b, strana_c):
        self.strana_a = strana_a
        self.strana_b = strana_b
        self.strana_c = strana_c
    def vypocet_obvodu(self):
        return self.strana_a + self.strana_b + self.strana_c
    def vypocet_obsahu(self):
        vyska = float(input("Zadejte výšku trojúhelníka: "))
        return 0.5 * self.strana_a * vyska

class Kruh(Tvar):
    def __init__(self, polomer):
        self.polomer = polomer
    def vypocet_obvodu(self):
        return 2 * math.pi * self.polomer
    
rodic = Tvar()
ctverec = Ctverec(5)
troj = Trojuhelnik(4, 8, 9)
kruh = Kruh(8)

ctverec.vypocet_obvodu()
ctverec.vypocet_obsahu()
troj.vypocet_obvodu()
kruh.vypocet_obvodu()
kruh.vypocet_obsahu()

print(ctverec.vypocet_obvodu())
print(ctverec.vypocet_obsahu())
print(troj.vypocet_obvodu())
print(troj.vypocet_obsahu())
print(kruh.vypocet_obvodu())
print(kruh.vypocet_obsahu())