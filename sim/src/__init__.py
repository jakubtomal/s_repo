from Dane_statkow import dane_statkow
from Statek import statek
from Flota import flota
from random import randint

flota1 = flota('flota1.txt')

flota2 = flota('flota2.txt')


runda = 1

while runda <= 6:
    flota1.atakuj(flota2)
    flota2.atakuj(flota1)
    flota1.wyczysc()
    flota2.wyczysc()
    
    if flota1.istnieje() == False and flota2.istnieje() == False :
        print('!!!! REMIS !!!!')
        break ;
    
    elif flota1.istnieje() == False :
        print('WYGRYWA FLOTA2')
        break;
    
    elif flota2.istnieje() == False :
        print('WYGRYWA FLOTA1')
        break;
        
    runda += 1
    
if flota2.istnieje() and flota1.istnieje():
    print('!!!! REMIS !!!!')
        
        
flota1.wypisz_ilosc()
print('-----------------')
flota2.wypisz_ilosc()
    

