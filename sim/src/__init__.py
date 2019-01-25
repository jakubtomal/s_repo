from Dane_statkow import dane_statkow
from Statek import statek
from Flota import flota
from random import randint
from appJar import gui
from matplotlib.cbook import Null




app = gui("Symulator Ogame","fullscreen")
#app.setSize(600,800)
app.setBg("white")
app.setFont(10)

def press(button):
    if button == "wyjdz":
        app.stop()
    else:
        plik1 = open('flota1.txt' , 'w')
        plik2 = open('flota2.txt' , 'w')
        plik3 = open('technologie1' , 'w')
        plik4 = open('technologie2' , 'w')
        
        if app.getEntry("maly transporter") == '':
            mt = '0';
        else:
            mt = app.getEntry("maly transporter")
        
        if app.getEntry("duzy transporter") == '':
            dt = '0';
        else:
            dt = app.getEntry("duzy transporter")
            
        if app.getEntry("lekki mysliwiec") == '':
            lm = '0';
        else:
            lm = app.getEntry("lekki mysliwiec")
            
        if app.getEntry("ciezki mysliwiec") == '':
            cm = '0';
        else:
            cm = app.getEntry("ciezki mysliwiec")
            
        if app.getEntry("krazownik") == '':
            kr = '0';
        else:
            kr = app.getEntry("krazownik")
            
        if app.getEntry("okret wojenny") == '':
            ow = '0';
        else:
            ow = app.getEntry("okret wojenny")
            
        if app.getEntry("statek kolonizacyjny") == '':
            sk = '0';
        else:
            sk = app.getEntry("statek kolonizacyjny")
            
        if app.getEntry("recykler") == '':
            re = '0';
        else:
            re = app.getEntry("recykler")
            
        if app.getEntry("sada szpiegowska") == '':
            ss = '0';
        else:
            ss = app.getEntry("sada szpiegowska")
            
        if app.getEntry("babowiec") == '':
            bb = '0';
        else:
            bb = app.getEntry("babowiec")
            
        if app.getEntry("niszczyciel") == '':
            ns = '0';
        else:
            ns = app.getEntry("niszczyciel")
            
        if app.getEntry("gwiazda smierci") == '':
            gs = '0';
        else:
            gs = app.getEntry("gwiazda smierci")
            
        if app.getEntry("pancernik") == '':
            pa = '0';
        else:
            pa = app.getEntry("pancernik")
            
        if app.getEntry("technologia bojowa") == '':
            tb1 = '1';
        else:
            tb1 = app.getEntry("technologia bojowa")
        if app.getEntry("opancerzenie") == '':
            op1 = '1';
        else:
            op1 = app.getEntry("opancerzenie")
        if app.getEntry("technologia ochronna") == '':
            to1 = '1';
        else:
            to1 = app.getEntry("technologia ochronna")
            

        
        
    
        plik1.write('mt:'+mt+"\n"+
                    'dt:'+dt+"\n"+
                    'lm:'+lm+"\n"+
                    'cm:'+cm+"\n"+
                    'kr:'+kr+"\n"+
                    'ow:'+ow+"\n"+
                    'sk:'+sk+"\n"+
                    're:'+re+"\n"+
                    'ss:'+ss+"\n"+
                    'bb:'+bb+"\n"+
                    'ns:'+ns+"\n"+
                    'gs:'+gs+"\n"+
                    'pa:'+pa+".")
        plik1.close()
        plik3.write(to1+'\n'+op1+'\n'+tb1+'\n')
        plik3.close()
        
        if app.getEntry("maly transporter.") == '':
            mt = '0';
        else:
            mt = app.getEntry("maly transporter.")
        
        if app.getEntry("duzy transporter.") == '':
            dt = '0';
        else:
            dt = app.getEntry("duzy transporter.")
            
        if app.getEntry("lekki mysliwiec.") == '':
            lm = '0';
        else:
            lm = app.getEntry("lekki mysliwiec.")
            
        if app.getEntry("ciezki mysliwiec.") == '':
            cm = '0';
        else:
            cm = app.getEntry("ciezki mysliwiec.")
            
        if app.getEntry("krazownik.") == '':
            kr = '0';
        else:
            kr = app.getEntry("krazownik.")
            
        if app.getEntry("okret wojenny.") == '':
            ow = '0';
        else:
            ow = app.getEntry("okret wojenny.")
            
        if app.getEntry("statek kolonizacyjny.") == '':
            sk = '0';
        else:
            sk = app.getEntry("statek kolonizacyjny.")
            
        if app.getEntry("recykler.") == '':
            re = '0';
        else:
            re = app.getEntry("recykler.")
            
        if app.getEntry("sada szpiegowska.") == '':
            ss = '0';
        else:
            ss = app.getEntry("sada szpiegowska.")
            
        if app.getEntry("babowiec.") == '':
            bb = '0';
        else:
            bb = app.getEntry("babowiec.")
            
        if app.getEntry("niszczyciel.") == '':
            ns = '0';
        else:
            ns = app.getEntry("niszczyciel.")
            
        if app.getEntry("gwiazda smierci.") == '':
            gs = '0';
        else:
            gs = app.getEntry("gwiazda smierci.")
            
        if app.getEntry("pancernik.") == '':
            pa = '0';
        else:
            pa = app.getEntry("pancernik.")
        if app.getEntry("technologia bojowa.") == '':
            tb2 = '1';
        else:
            tb2 = app.getEntry("technologia bojowa.")
        if app.getEntry("opancerzenie.") == '':
            op2 = '1';
        else:
            op2 = app.getEntry("opancerzenie.")
        if app.getEntry("technologia ochronna.") == '':
            to2 = '1';
        else:
            to2 = app.getEntry("technologia ochronna.")
        
        plik2.write('mt:'+mt+"\n"+
                    'dt:'+dt+"\n"+
                    'lm:'+lm+"\n"+
                    'cm:'+cm+"\n"+
                    'kr:'+kr+"\n"+
                    'ow:'+ow+"\n"+
                    'sk:'+sk+"\n"+
                    're:'+re+"\n"+
                    'ss:'+ss+"\n"+
                    'bb:'+bb+"\n"+
                    'ns:'+ns+"\n"+
                    'gs:'+gs+"\n"+
                    'pa:'+pa+".")
        
        plik2.close()
        plik4.write(to2+'\n'+op2+'\n'+tb2+'\n')
        plik4.close()
        
        app.stop()

#app.addLabel("title", "Welcome to appJar")
#app.setLabelBg("title", "red")
app.addLabel("flota1" , "wpisz dane floty pierwszej:")
app.setLabelBg("flota1", "grey")
app.addLabelEntry("technologia bojowa" )
app.setEntryDefault("technologia bojowa", "0")
app.addLabelEntry("opancerzenie")
app.setEntryDefault("opancerzenie", "0")
app.addLabelEntry("technologia ochronna")
app.setEntryDefault("technologia ochronna", "0")
app.addLabelEntry("maly transporter")
app.setEntryDefault("maly transporter", "0")
app.addLabelEntry("duzy transporter")
app.setEntryDefault("duzy transporter", "0")
app.addLabelEntry("lekki mysliwiec")
app.setEntryDefault("lekki mysliwiec", "0")
app.addLabelEntry("ciezki mysliwiec")
app.setEntryDefault("ciezki mysliwiec", "0")
app.addLabelEntry("krazownik")
app.setEntryDefault("krazownik", "0")
app.addLabelEntry("okret wojenny")
app.setEntryDefault("okret wojenny", "0")
app.addLabelEntry("statek kolonizacyjny")
app.setEntryDefault("statek kolonizacyjny", "0")
app.addLabelEntry("recykler")
app.setEntryDefault("recykler", "0")
app.addLabelEntry("sada szpiegowska")
app.setEntryDefault("sada szpiegowska", "0")
app.addLabelEntry("babowiec")
app.setEntryDefault("babowiec", "0")
app.addLabelEntry("niszczyciel")
app.setEntryDefault("niszczyciel", "0")
app.addLabelEntry("gwiazda smierci")
app.setEntryDefault("gwiazda smierci", "0")
app.addLabelEntry("pancernik")
app.setEntryDefault("pancernik", "0")


app.addLabel("flota2" , "wpisz dane floty drugiej:")
app.setLabelBg("flota2", "grey")
app.addLabelEntry("technologia bojowa.")
app.setEntryDefault("technologia bojowa.", "0")
app.addLabelEntry("opancerzenie.")
app.setEntryDefault("opancerzenie.", "0")
app.addLabelEntry("technologia ochronna.")
app.setEntryDefault("technologia ochronna.", "0")
app.addLabelEntry("maly transporter.")
app.setEntryDefault("maly transporter.", "0")
app.addLabelEntry("duzy transporter.")
app.setEntryDefault("duzy transporter.", "0")
app.addLabelEntry("lekki mysliwiec.")
app.setEntryDefault("lekki mysliwiec.", "0")
app.addLabelEntry("ciezki mysliwiec.")
app.setEntryDefault("ciezki mysliwiec.", "0")
app.addLabelEntry("krazownik.")
app.setEntryDefault("krazownik.", "0")
app.addLabelEntry("okret wojenny.")
app.setEntryDefault("okret wojenny.", "0")
app.addLabelEntry("statek kolonizacyjny.")
app.setEntryDefault("statek kolonizacyjny.", "0")
app.addLabelEntry("recykler.")
app.setEntryDefault("recykler.", "0")
app.addLabelEntry("sada szpiegowska.")
app.setEntryDefault("sada szpiegowska.", "0")
app.addLabelEntry("babowiec.")
app.setEntryDefault("babowiec.", "0")
app.addLabelEntry("niszczyciel.")
app.setEntryDefault("niszczyciel.", "0")
app.addLabelEntry("gwiazda smierci.")
app.setEntryDefault("gwiazda smierci.", "0")
app.addLabelEntry("pancernik.")
app.setEntryDefault("pancernik.", "0")


app.addButtons(["symuluj", "wyjdz"], press)


app.go()





def symuluj(n , flotaA , flotaB ):
    
    tech1 = open('technologie1' , 'r')
    tech2 = open('technologie2' , 'r')
    t1 = []
    t2 = []
    
    for i in tech1:
        t1.append(int(i[-2]))
    tech1.close()
    
    for i in tech2:
        t2.append(int(i[-2]))
    tech2.close()
    
    runda = 1   
    tmp1 = flota('flota_sum1.txt')
    tmp2 = flota('flota_sum1.txt')
    

    
    for i in range(n):
        flota2 = flota(flotaB , t1[0] , t1[1] , t1[2] )
        flota1= flota(flotaA , t2[0] , t2[1] , t2[2] )
        flota2.stworz()
        flota1.stworz()
        
        while runda <= 6:
            flota1.atakuj(flota2 )
            flota2.atakuj(flota1 )
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
            
        runda = 0    
        for k in flota1.flota:
            tmp1.dadaj(k.name, 1)
            
        for k in flota2.flota:
            tmp2.dadaj(k.name, 1)
            
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
        wynik ='!!!! REMIS !!!!'

    elif tmp1.istnieje() == False :
        wynik = 'WYGRYWA FLOTA2'
    
    elif tmp2.istnieje() == False :
        wynik = 'WYGRYWA FLOTA1'
    
    else:
        wynik = '!!!! REMIS !!!!'
        
    app = gui("Symulator Ogame","fullscreen")
    app.setBg("white")
    app.setFont(10)
    app.addLabel('WYNIKI : ')
    app.setLabelBg("WYNIKI : ", "red")
    app.addLabel('flota1 : ')
    app.setLabelBg("flota1 : ", "grey")
    app.addLabel(tmp1.wypisz_ilosc())
    app.addLabel('flota2 : ')
    app.setLabelBg("flota2 : ", "grey")
    app.addLabel(tmp2.wypisz_ilosc() )
    app.addLabel(wynik)
    app.setLabelBg( wynik , "red")
    
    app.go()

    
    print(tmp1.wypisz_ilosc())
    print('----------------------------')
    print(tmp2.wypisz_ilosc())          
        
    return 0


symuluj( 5 , 'flota1.txt' , 'flota2.txt'  )
    
