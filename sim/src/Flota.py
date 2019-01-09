'''
Created on 19 lis 2018

@author: dredi
'''
class Flota():
    def __init__(self):
        self.mt = 0
        self.dt = 0
        self.lm = 0
        self.cm = 0
        self.kr = 0
        self.ow = 0
        self.sk = 0
        self.re = 0
        self.ss = 0
        self.bb = 0
        self.ns = 0
        self.gs = 0
        self.pa = 0
        
    def czytaj_flote(self,nazwa_pliku):
        plik = open(nazwa_pliku , 'r')
        tmplist = []
        
        for i in plik:
            tmplist.append(i[3:-1])
            
        