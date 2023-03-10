#EJERCICIO 1
##suma de vectores en R3##
def sumavectores(v1, v2):
    v = []
    for i in v1:
        v.append(v1[i]+v2[i])
    return v

#print(sumavectores([1,1,1,1],[1,1,1,1]))

##resta de vectores en R3##
def restavectores(v1, v2):
    v = []
    for i in v1:
        v.append(v1[i]-v2[i])
    return v

#print(restavectores([1,1,1],[1,1,1]))

##multiplicacion de vectores en R3##
def multvectores(v1, v2):
    vr = 0
    for i in v1:
        vr = vr + v1[i]*v2[i]
    return vr

#print(multvectores([1,1,1],[2,2,2]))

def sumaarrays(a1, a2):
    A = []
    i = 0
    while (i < (len(a1))):
        j = 0
        aux = []
        while (j < (len(a1[i]))):
            aux.append(a1[i][j]+a2[i][j])
            j = j + 1
        
        A.append(aux)
        i = i + 1
    return A

#print(sumaarrays([[1,1,1],[1,1,1],[1,1,1]], [[2,2,2],[2,2,2],[2,2,2]]))

def arrxesc(a, n):
    A = []
    i = 0
    while (i < (len(a))):
        j = 0
        aux = []
        while (j < (len(a[i]))):
            aux.append(a[i][j] * n)
            j = j + 1
        
        A.append(aux)
        i = i + 1
    return A

#print(arrxesc([[1,1,1],[1,1,1],[1,1,1]], 2))

def arrxvec(a, v):
    A = []
    i = 0
    while (i<len(a)):
        j = 0
        aux = 0
        while (j < (len(a[i]))):
            aux = aux + (a[i][j] * v[i])
            j = j + 1
        A.append(aux)
        i = i + 1
    return A

#print(arrxvec([[1,1,1],[1,1,1],[1,1,1]], [1,1,1]))

def arrxarr(a1, a2):
    A = []
    i = 0
    while (i<len(a1)):
        j = 0
        suma = 0
        z = 0
        aux2 = []

        while (z<len(a1)):
            while (j < (len(a1[i]))):
                suma = suma + (a1[z][j] * a2[j][i])
                j = j + 1
            
            aux2.append(suma)
            z = z + 1
        
        A.append(aux2)
        i = i + 1
    return A

#print(arrxarr([[1,1,1],[1,1,1],[1,1,1]], [[1,1,1],[1,1,1],[1,1,1]]))


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,20)

fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")
ax.plot(x, x)
ax.plot(x, 3-(1/2)*x)
ax.plot(x, np.ones_like(x)*2)

plt.xlabel('x')
plt.ylabel('y')
plt.title('ejercicio 6')
plt.show()

