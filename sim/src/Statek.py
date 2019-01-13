
from random import randint
from Dane_statkow import dane_statkow

statek_info = dane_statkow();
plik_sd = open('szybkie_dziala.txt' , 'r' )
lista_sd = []

for i in plik_sd:
    lista_sd.append(i[:-1].split(' '))
    


class statek():
    def __init__(self ,  Tab):
        '''klasa statek : 
        name(str): skrot nazwy statku, 
        pancerz(float): aktualny pancerz statku,sd
        oslona(float): aktualna oslona statku
        atak(float): obrazenia jakie zadaje statek 
        '''
        self.name = Tab[0]
        self.pancerz = float(Tab[1])
        self.oslona = float(Tab[2])
        self.atak = float(Tab[3])
        
    def strzel(self,statek2):
        ''' Funkcja sprawdzajaca czy statek bedzie mogl ponownie strzelic  '''
        
        statek_dziala = {'mt' : 0 , 'dt' : 1 , 'lm' : 2 
                         , 'cm' : 3 , 'kr' : 4 , 'ow' : 5 
                         , 'sk' : 6 , 're' : 7 , 'ss' : 8 
                         , 'bb' : 9 , 'ns' : 10 , 'gs' : 11 
                         , 'pa' : 12 } # slownik przypisujacy nazwie statku odpowiedni indeks w tablicy szybkich dzial
        
        szansa = 100 * (1 - 1/float(lista_sd[statek_dziala[self.name]][statek_dziala[statek2.name]])) # szansa na to ze statek bedzie mogl oddac ponowny strzal
        
        if randint(0,100) <= szansa:
            return True #statek moze ponownie strzelic
        else:
            return False # statek nie moze ponownie strzelac
        
    def trafiony(self , statek2):
        ''' Funkcja obslugujaca co sie stanie jezeli w statek strzeli statek2'''
        
        if self.oslona > 0:
            if ( statek2.atak / self.oslona) < 0.1:
                return False #statek2 nie trafil
        
        obrazenia = statek2.atak
        oslona_tmp = self.oslona
        self.oslona -= obrazenia
        obrazenia -= oslona_tmp
        if self.oslona < 0:
            self.oslona = 0
        if obrazenia > 0:
            self.pancerz -= obrazenia;
            if self.pancerz <= 0:
                self.pancerz = 0
                
        if self.pancerz < float(dane_statkow.pobierz_info(self.name)[1]) * 0.7: 
            szansa_wybuch = 100 *( 1 - (self.pancerz / float(dane_statkow.pobierz_info(self.name)[1]))) #szansa na to ze statek wybuchnie
            if randint(0,100) <= szansa_wybuch :
                self.pancerz = 0
                return True #statek zostal zniszczony
            
            else:
                return False #statek nie zostal zniszczony
        else:
            return False #statek nie zostal zniszczony
        
    def zniszczony(self):
        '''funkcja zwracajaca True jezeli statek zostal zniszczony lub False jeżeli nie zostal'''
        if self.pancerz <= 0 :
            return True
        else:
            return False
        
    def statystyki(self):
        ''' funkcja wypisujaca statystyki statku '''
        print("nazwa:" + self.name + " pancerz:" + str(int(self.pancerz)) + " oslona:" + str(int(self.oslona)) + " atak:" + str(int(self.atak)))
             
        
        

        
        