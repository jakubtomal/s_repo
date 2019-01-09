
#szybkie_dziala =[ [1,1,1,1,1,1,1,1,5,1,1,1,1] , [1,1,1,1,1,1,1,1,5,1,1,1,1] , [1,1,1,1,1,1,1,1,5,1,1,1,1] , [3,1,1,1,1,1,1,1,5,1,1,1,1] , [1,1,6,1,1,1,1,1,5,1,1,1,1] , [1,1,1,1,1,1,1,1,5,1,1,1,1] , [1,1,1,1,1,1,1,1,5,1,1,1,1] , [1,1,1,1,1,1,1,1,5,1,1,1,1] , [1,1,1,1,1,1,1,1,5,1,1,1,1] , [1,1,1,1,1,1,1,1,5,1,1,1,1] , [1,1,1,1,1,1,1,1,5,1,1,1,2] , [250,250,200,100,33,30,250,250,1250,25,5,1,15] ,[3,3,1,4,4,7,1,1,5,1,1,1,1] ]
from random import randint

plik_sd = open('szybkie_dziala.txt' , 'r' )
lista_sd = []

for i in plik_sd:
    lista_sd.append(i[:-1].split(' '))
    


class statek():
    def __init__(self ,  Tab):
        self.name = Tab[0]
        self.pancerz = float(Tab[1])
        self.oslona = float(Tab[2])
        self.atak = float(Tab[3])
        
    def strzel(self,statek2):
        
        statek_dziala = {'mt' : 0 , 'dt' : 1 , 'lm' : 2 
                         , 'cm' : 3 , 'kr' : 4 , 'ow' : 5 
                         , 'sk' : 6 , 're' : 7 , 'ss' : 8 
                         , 'bb' : 9 , 'ns' : 10 , 'gs' : 11 
                         , 'pa' : 12 }
        
        szansa = 100 * (1 - 1/float(lista_sd[statek_dziala[self.name]][statek_dziala[statek2.name]]))
        
        if randint(0,100) <= szansa:
            return True
        else:
            return False
        
    def trafiony(self , statek2):
        print(statek2.atak / self.oslona)
        if ( statek2.atak / self.oslona) < 0.1:
            print('nie strzela')
        else:
            print ('strzela')
        
        
        
        

        
        