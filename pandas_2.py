#pg 27
#del on basis of indexing
import pandas as pd
import numpy as np
g2 = pd.Series({'1969': 7, '1970': [1, 22]},
  index=['1969', '1970', '1970'])
print(g2)
del g2['1970']
print(g2)


print("_____________________________")
#pg 31
#indexing
#for indexing through .iloc and .loc

print(g2.iloc[1])
#pg32
