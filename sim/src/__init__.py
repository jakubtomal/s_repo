from Dane_statkow import dane_statkow
from Statek import statek
from Flota import flota

a = dane_statkow() 

print(a.mt);

b=statek(a.mt)
g=statek(a.lm)

print(b.atak)

c = flota('flota1.txt')

print(c.lm)

b.strzel(g)

print(b.atak)
print(g.oslona)
print(10.0/50)
b.trafiony(g)
