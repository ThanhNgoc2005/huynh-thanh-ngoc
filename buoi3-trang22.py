# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:12:23 2024

@author: Admin
"""

import math
a=float(input("Nhap so thuc a:"))
b=float(input("Nhap so thuc b:"))
x=((math.sqrt(a)-math.sqrt(b))/(pow(a,1/4)-pow(b,1/4)))-((math.sqrt(a)+pow(a*b,1/4))/(pow(a,1/4)+pow(b,1/4)))
print("Ket qua la:",round(x,3))