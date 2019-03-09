# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 04:55:15 2019

@author: Dell
"""

import pandas as pd

songs3 = pd.Series([145, 142, 38, 13],
       name='counts',
       index=['Paul', 'John', 'George', 'Ringo'])
print(songs3)

import numpy as np
num_ser=np.array([145,142,38,14])
print(num_ser[1])
print(songs3[1])


print(songs3.mean())
print(num_ser.mean())

true_false = songs3>songs3.median()
print(true_false)
print(songs3[true_false])
#true_False = num_ser>num_ser.median()
#print(true_False)
print(num_ser[num_ser>np.median(num_ser)])
