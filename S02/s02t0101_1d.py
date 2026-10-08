# Importando el modulo Arrays 
from array import array as arr 

# Crando un arreglo 
array_01 = arr('i',[3,8,5,1,6])

# Iterando automaticamente 
for data in array_01:
    print(data,end=",")
print()