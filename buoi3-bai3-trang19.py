# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:41:46 2024

@author: Admin
"""

a=int(input("nhap vao so nguyn duong N co 2 chu so :"))
if a>=10 and a<=99:
    x=a//10
    y=a%10
    print(" tong cua 2 chu so la :",x+y)
else:
    print(" nhap sai ! moi nhap lai ")
    