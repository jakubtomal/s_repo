
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
        

