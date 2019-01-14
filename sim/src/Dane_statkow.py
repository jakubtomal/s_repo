
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
    def pancerz(x):
        '''Statyczna metoda zwracajaca pancerz po podaniu skrotu statku'''
        if x == 'mt':
            return dane_statkow.mt[1]
        
        elif x == 'dt':
            return dane_statkow.dt[1]
        
        elif x == 'lm':
            return dane_statkow.lm[1]
        
        elif x == 'cm':
            return dane_statkow.cm[1]
        
        elif x == 'kr':
            return dane_statkow.kr[1]
        
        elif x == 'ow':
            return dane_statkow.ow[1]
        
        elif x == 'sk':
            return dane_statkow.sk[1]
        
        elif x == 're':
            return dane_statkow.re[1]
        
        elif x == 'ss':
            return dane_statkow.ss[1]
        
        elif x == 'bb':
            return dane_statkow.bb[1]
        
        elif x == 'ns':
            return dane_statkow.ns[1]
        
        elif x == 'gs':
            return dane_statkow.gs[1]
        
        elif x == 'pa':
            return dane_statkow.pa[1]
        
    @staticmethod
    def oslona(x):
        '''Statyczna metoda zwracajaca oslone po podaniu skrotu statku'''
        if x == 'mt':
            return dane_statkow.mt[2]
        
        elif x == 'dt':
            return dane_statkow.dt[2]
        
        elif x == 'lm':
            return dane_statkow.lm[2]
        
        elif x == 'cm':
            return dane_statkow.cm[2]
        
        elif x == 'kr':
            return dane_statkow.kr[2]
        
        elif x == 'ow':
            return dane_statkow.ow[2]
        
        elif x == 'sk':
            return dane_statkow.sk[2]
        
        elif x == 're':
            return dane_statkow.re[2]
        
        elif x == 'ss':
            return dane_statkow.ss[2]
        
        elif x == 'bb':
            return dane_statkow.bb[2]
        
        elif x == 'ns':
            return dane_statkow.ns[2]
        
        elif x == 'gs':
            return dane_statkow.gs[2]
        
        elif x == 'pa':
            return dane_statkow.pa[2]
        
    @staticmethod
    def atak(x):
        '''Statyczna metoda zwracajaca atak po podaniu skrotu statku'''
        if x == 'mt':
            return dane_statkow.mt[3]
        
        elif x == 'dt':
            return dane_statkow.dt[3]
        
        elif x == 'lm':
            return dane_statkow.lm[3]
        
        elif x == 'cm':
            return dane_statkow.cm[3]
        
        elif x == 'kr':
            return dane_statkow.kr[3]
        
        elif x == 'ow':
            return dane_statkow.ow[3]
        
        elif x == 'sk':
            return dane_statkow.sk[3]
        
        elif x == 're':
            return dane_statkow.re[3]
        
        elif x == 'ss':
            return dane_statkow.ss[3]
        
        elif x == 'bb':
            return dane_statkow.bb[3]
        
        elif x == 'ns':
            return dane_statkow.ns[3]
        
        elif x == 'gs':
            return dane_statkow.gs[3]
        
        elif x == 'pa':
            return dane_statkow.pa[3]
    

