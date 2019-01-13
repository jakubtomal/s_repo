
class dane_statkow:
        
    tmplist=[]
    file1 = open('Dane_statkow.txt' , 'r')
    for i in file1:
        tmplist.append(i[:-1].split(','))
    file1.close()
        
    mt = tmplist[0]
    dt = tmplist[1]
    lm = tmplist[2]
    cm = tmplist[3]
    kr = tmplist[4]
    ow = tmplist[5]
    sk = tmplist[6]
    re = tmplist[7]
    ss = tmplist[8]
    bb = tmplist[9]
    ns = tmplist[10]
    gs = tmplist[11]
    pa = tmplist[12]
    
    @staticmethod
    def pobierz_info(x):
        '''Statyczna metoda zwracajaca tablice statystyk po podaniu skrotu statku'''
        if x == 'mt':
            return dane_statkow.mt
        
        elif x == 'dt':
            return dane_statkow.dt
        
        elif x == 'lm':
            return dane_statkow.lm
        
        elif x == 'cm':
            return dane_statkow.cm
        
        elif x == 'kr':
            return dane_statkow.kr
        
        elif x == 'ow':
            return dane_statkow.ow
        
        elif x == 'sk':
            return dane_statkow.sk
        
        elif x == 're':
            return dane_statkow.re
        
        elif x == 'ss':
            return dane_statkow.ss
        
        elif x == 'bb':
            return dane_statkow.bb
        
        elif x == 'ns':
            return dane_statkow.ns
        
        elif x == 'gs':
            return dane_statkow.gs
        
        elif x == 'pa':
            return dane_statkow.pa
        
        
        

