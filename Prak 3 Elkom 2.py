# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:32:07 2024

@author: Rangga Aditya
"""

class Persegi:

    def __init__(self):
          #Identitas
        self.nama  = "Rangga Aditya Pradana"
        self.nim   = "064002300026"
        self.studi = "Teknik Informatika"
        self.panjang = int(input("Masukkan panjangnya : "))
        self.lebar = int(input("Masukkan lebar : "))

    def segitiga(self):
        return self.panjang * self.lebar  #rumus persegi 
    
    def Hasil(self):  #tampilan user 
        print(self.nama , self.nim , self.studi)  
        print("---->PROGRAM MENGHITUNG PERSEGI PANJANG<----")
        print("Persegi panjang dengan panjang", self.panjang, "cm lebar", self.lebar, "memiliki luas sekitar", self.segitiga(), "cm^2")

def main():  #Pemanggilan fungsi 
    obj_persegi = Persegi()
    obj_persegi.Hasil()

if __name__ == "__main__":
    main()