##suma de vectores en R3##
def sumavectores(v1, v2):
    v = []
    for i in v1:
        v.append(v1[i]+v2[i])
    return v

#print(sumavectores([1,1,1],[1,1,1]))

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

print(multvectores([1,1,1],[2,2,2]))