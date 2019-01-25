from Dane_statkow import dane_statkow
from Statek import statek
from Flota import flota
from random import randint

flota1 = flota('flota1.txt')

flota2 = flota('flota2.txt')

a = statek(dane_statkow.gs)
b = statek(dane_statkow.ns)

a.trafiony(b)

print(a.statystyki())
print('----------------');