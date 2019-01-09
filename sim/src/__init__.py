from Dane_statkow import dane_statkow
from Statek import statek
from Flota import flota

a = dane_statkow() 

print(a.mt);

b=statek(a.mt)

print(b.atak)

c = flota('flota1.txt')

print(c.lm)

b.strzel(b)
