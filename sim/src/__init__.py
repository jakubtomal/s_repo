from Dane_statkow import dane_statkow
from Statek import statek
from Flota import flota
from random import randint




def symuluj(n , flotaA , flotaB):
    
    runda = 1   
    tmp1 = flota('flota_sum1.txt')
    tmp2 = flota('flota_sum1.txt')
    

    
    for i in range(n):
        flota2 = flota(flotaB)
        flota1= flota(flotaA)
        flota2.stworz()
        flota1.stworz()
        
        while runda <= 6:
            flota1.atakuj(flota2)
            flota2.atakuj(flota1)
            flota1.wyczysc()
            flota2.wyczysc()
            if flota1.istnieje() == False and flota2.istnieje() == False :
                #print('!!!! REMIS !!!!')
                break ;
            
            elif flota1.istnieje() == False :
                #print('WYGRYWA FLOTA2')
                break;
            
            elif flota2.istnieje() == False :
                #print('WYGRYWA FLOTA1')
                break;
                
            runda += 1
            
            
        for i in flota1.flota:
            tmp1.dadaj(i.name, 1)
            
        for i in flota2.flota:
            tmp2.dadaj(i.name, 1)
            
    tmp1.mt = tmp1.mt / n
    tmp1.dt = tmp1.dt / n
    tmp1.lm = tmp1.lm / n
    tmp1.cm = tmp1.cm / n
    tmp1.kr = tmp1.kr / n
    tmp1.ow = tmp1.ow / n
    tmp1.sk = tmp1.sk / n
    tmp1.re = tmp1.re / n
    tmp1.ss = tmp1.ss / n
    tmp1.bb = tmp1.bb / n
    tmp1.ns = tmp1.ns / n
    tmp1.gs = tmp1.gs / n
    tmp1.pa = tmp1.pa / n
    
    tmp2.mt = tmp2.mt / n
    tmp2.dt = tmp2.dt / n
    tmp2.lm = tmp2.lm / n
    tmp2.cm = tmp2.cm / n
    tmp2.kr = tmp2.kr / n
    tmp2.ow = tmp2.ow / n
    tmp2.sk = tmp2.sk / n
    tmp2.re = tmp2.re / n
    tmp2.ss = tmp2.ss / n
    tmp2.bb = tmp2.bb / n
    tmp2.ns = tmp2.ns / n
    tmp2.gs = tmp2.gs / n
    tmp2.pa = tmp2.pa / n
    
    
    
                
    tmp1.stworz();
    tmp2.stworz()
    
    if tmp1.istnieje() == False and tmp2.istnieje() == False :
        print('!!!! REMIS !!!!')

    elif tmp1.istnieje() == False :
        print('WYGRYWA FLOTA2')
    
    elif tmp2.istnieje() == False :
        print('WYGRYWA FLOTA1')
    
    else:
        print('!!!! REMIS !!!!')
    
    tmp1.wypisz_ilosc()
    print('----------------------------')
    tmp2.wypisz_ilosc()          
        
    return 0


symuluj( 100 , 'flota1.txt' , 'flota2.txt' )
    
