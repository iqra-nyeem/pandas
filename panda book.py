import pandas as pd

class Foo:
    pass

ringo = pd.Series(
        ['python','jenny',1,Foo()],
        name='ringo')

print('__________________________________________')

print(ringo)

#pg22
George = pd.Series([10,1,7,22],
        index=['1998','1970','1969','1970'])

print(George)
print("___________________________________")

#pg 23
g=pd.Series({'1969':7,'1970':[1,3]},index=['1969','1970','1970'])
print(g)

print('_____________________________________')

print(George['1970'])

print('_______________________________')

#pg24

for item in George:
    print(item)
print('_____________________________________')

print(22 in George)

print(22 in set(George))
print(22 in George.values)

print("_______________________________________________")

test_t = pd.Series([11,12,3,2],
        index=['1968','1973','1964','1973'])
for item in test_t.iteritems():
    print(item)


test_t['1968']=6
print(test_t)

test_t.iloc[3]=22
print(test_t)#iloc is use to change values on the basis of position while indexing changs values on the basis of keys


print('_______________________________________________')

#pg26

#methods to add values in pandas lib
#1st method

#print(George.append(pd.Series({"1992":9})))
print(test_t.append(pd.Series({"1992":9})))

#2nd method

print(test_t.set_value('1993',55))

print(test_t)
