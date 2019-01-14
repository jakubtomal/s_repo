'''
Created on 19 lis 2018

@author: dredi
'''

from Statek import statek
from Dane_statkow import dane_statkow
from random import randint 


class flota():
    def __init__(self , nazwa_pliku, ochronna = 1 , opancerzenie = 1 , bojowa = 1):
        plik = open(nazwa_pliku , 'r')
        tmplist = []
        
        for i in plik:
            tmplist.append(i[:-1])
            
        plik.close()
            
        self.mt = int(tmplist[0][3:])
        self.dt = int(tmplist[1][3:])
        self.lm = int(tmplist[2][3:])
        self.cm = int(tmplist[3][3:])
        self.kr = int(tmplist[4][3:])
        self.ow = int(tmplist[5][3:])
        self.sk = int(tmplist[6][3:])
        self.re = int(tmplist[7][3:])
        self.ss = int(tmplist[8][3:])
        self.bb = int(tmplist[9][3:])
        self.ns = int(tmplist[10][3:])
        self.gs = int(tmplist[11][3:])
        self.pa = int(tmplist[12][3:])
        
        self.ochronna = ochronna
        self.opancerzenie = opancerzenie
        self.bojowa = bojowa
        
        self.flota = []
        
        for i in range(0,self.mt):
            self.flota.append(statek( dane_statkow.mt , ochronna , opancerzenie , bojowa ))
            
        for i in range(0,self.dt):
            self.flota.append(statek( dane_statkow.dt , ochronna , opancerzenie , bojowa ))
            
        for i in range(0,self.lm):
            self.flota.append(statek( dane_statkow.lm , ochronna , opancerzenie , bojowa ))
        
        for i in range(0,self.cm):
            self.flota.append(statek( dane_statkow.cm , ochronna , opancerzenie , bojowa ))
            
        for i in range(0,self.kr):
            self.flota.append(statek( dane_statkow.kr  , ochronna , opancerzenie , bojowa ))
            
        for i in range(0,self.ow):
            self.flota.append(statek( dane_statkow.ow  , ochronna , opancerzenie , bojowa ))
            
        for i in range(0,self.sk):
            self.flota.append(statek( dane_statkow.sk  , ochronna , opancerzenie , bojowa ))
            
        for i in range(0,self.re):
            self.flota.append(statek( dane_statkow.re  , ochronna , opancerzenie , bojowa ))
            
        for i in range(0,self.ss):
            self.flota.append(statek( dane_statkow.ss  , ochronna , opancerzenie , bojowa ))
            
        for i in range(0,self.bb):
            self.flota.append(statek( dane_statkow.bb  , ochronna , opancerzenie , bojowa ))
            
        for i in range(0,self.ns):
            self.flota.append(statek( dane_statkow.ns  , ochronna , opancerzenie , bojowa ))
            
        for i in range(0,self.gs):
            self.flota.append(statek( dane_statkow.gs , ochronna , opancerzenie , bojowa ))
            
        for i in range(0,self.pa):
            self.flota.append(statek( dane_statkow.pa , ochronna , opancerzenie , bojowa ))
        
        
    def usun(self , nazwa , n ):
        
        if nazwa == 'mt':
            self.mt -= n
            
        elif nazwa == 'dt':
            self.dt -= n
            
        elif nazwa == 'lm':
            self.lm -= n
            
        elif nazwa == 'cm':
            self.cm -= n
            
        elif nazwa == 'kr':
            self.kr -= n
            
        elif nazwa == 'ow':
            self.ow -= n
            
        elif nazwa == 'sk':
            self.sk -= n
            
        elif nazwa == 're':
            self.re -= n
            
        elif nazwa == 'ss':
            self.ss -= n
            
        elif nazwa == 'bb':
            self.bb -= n
            
        elif nazwa == 'ns':
            self.ns -= n
            
        elif nazwa == 'gs':
            self.gs -= n
            
        elif nazwa == 'pa':
            self.pa -= n
            
    def wyczysc(self):
        tmp = []
        
        for i in self.flota:
            if i.zniszczony() == False:
                i[2] = dane_statkow.oslona(i[0]) * self.ochronna
                tmp.append(i)
            else:
                self.usun(i.name , 1)
                
        self.flota = tmp
        
    def atakuj(self , flota_2):
        for i in self.flota:
            
            r = randint(0,len( flota_2.flota ))
            
            flota_2.flota[r].trafiony(i)
            
            while i.strzel( flota_2.flota[ r ] ):
                r = randint(0,len( flota_2.flota ))
                flota_2.flota[r].trafiony(i)
            
    def wypisz_ilosc(self):
        print('male transportery: ' + str(self.mt) + 
              '\nduze transportery: ' + str(self.dt) +
              '\nlekkie mysliwce: ' + str(self.lm) +
              '\nciezkie mysliwce: ' + str(self.cm) +
              '\nkrazowniki: ' + str(self.kr) + 
              '\nokrety wojenne: ' + str(self.ow) + 
              '\nstatki kolonizacyjne: ' + str(self.sk) + 
              '\nrecyklery: ' + str(self.re) + 
              '\nsady szpiegowskie' + str(self.ss) +
              '\nbabowce: ' + str(self.bb) + 
              '\nniszczyciele: ' + str(self.ns) + 
              '\ngwiazdy smierci: ' + str(self.gs) + 
              '\npancerniki: ' + str(self.pa) )
            
                
        
        

            
        