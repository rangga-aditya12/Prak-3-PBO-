# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:14:47 2024

@author: Rangga Aditya
"""

class praktikan():
    def __init__(self, nama, nim, fakultas, hobi):
        self.nama = nama
        self.nim = nim
        self.fakultas = fakultas
        self.hobi = hobi

    def Hasil(self):
        return f"----Program menampilkan identitas---\n Nama saya adalah {self.nama}, NIM saya adalah {self.nim}, saya berasal dari fakultas {self.fakultas}, Hobi saya adalah {self.hobi}."

praktikan1 = praktikan("Rangga Aditya Pradana", "064002300026", "Teknik Informatika", "Nontonin orang debat di twitter")  

print(praktikan1.Hasil())

    
    