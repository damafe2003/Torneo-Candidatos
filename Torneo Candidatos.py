import numpy as np

lista=["Caruana","Radjabov","Liren","Hao","Grischuk","Nepo","Giri","Alekseenko"]
l=len(lista)
probabilidades=(
                [[0.5,0.5,0],[0.308,0.615,0.077],[0.182,0.636,0.182],[0.2,0.6,0.2],[0.364,0.454,0.182],[0.133,0.8,0.067],[0.103,0.828,0.069],[0.4,0.5,0.1]],
                [[0.077,0.615,0.308],[0.5,0.5,0],[0.111,0.667,0.222],[0.083,0.834,0.083],[0.166,0.668,0.166],[0.233,0.7,0.067],[0.081,0.895,0.024],[0.35,0.45,0.2]],
                [[0.182,0.636,0.182],[0.222,0.667,0.111],[0.5,0.5,0],[0.353,0.588,0.059],[0.27,0.676,0.054],[0.167,0.666,0.167],[0.091,0.818,0.091],[0.35,0.55,0.1]],
                [[0.2,0.6,0.2],[0.083,0.834,0.083],[0.059,0.588,0.353],[0.5,0.5,0],[0.18,0.55,0.27],[0.19,0.55,0.26],[0.15,0.6,0.25],[0.3,0.55,0.15]],
                [[0.182,0.454,0.364],[0.167,0.666,0.167],[0.054,0.676,0.27],[0.27,0.55,0.18],[0.5,0.5,0],[0.143,0.571,0.286],[0.059,0.706,0.235],[0.35,0.55,0.1]],
                [[0.067,0.8,0.133],[0.067,0.7,0.233],[0.167,0.666,0.167],[0.25,0.6,0.15],[0.235,0.706,0.059],[0.5,0.5,0],[0.15,0.5,0.35],[0.35,0.5,0.15]],
                [[0.069,0.828,0.103],[0.024,0.895,0.081],[0.091,0.818,0.091],[0.25,0.6,0.15],[0.235,0.706,0.059],[0.35,0.5,0.15],[0.5,0.5,0],[0.29,0.6,0.11]],
                [[0.1,0.5,0.4],[0.2,0.45,0.35],[0.1,0.55,0.35],[0.15,0.55,0.3],[0.1,0.55,0.35],[0.15,0.5,0.35],[0.11,0.6,0.29],[0.5,0.5,0]]                
                )
victorias=[0,0,0,0,0,0,0,0]

n=100000#numero de simulaciones

for x in range(n):
    print(x)
#Simulación del torneo
    puntos=[0,0,0,0,0,0,0,0]
    puntosD=[0,0,0,0,0,0,0,0]
    for i in range(l):
        for j in range(l):
            if lista[i]!=lista[j]:
                resultado=list(np.random.choice([lista[i],"empate",lista[j]],size=1,p=probabilidades[i][j]))
                puntos[i]=puntos[i]+ resultado.count(lista[i])+resultado.count("empate")/2
                puntos[j]=puntos[j]+resultado.count(lista[j])+resultado.count("empate")/2
#---------------------------------------------           
   
    maximo=max(puntos)
    indices = [i for i in range(len(puntos)) if puntos[i] == maximo]
    if len(indices)>1:#Checking if there is more than 1 winner 
#playing the tiebreak if there is more than 1 winner
        for y in indices:
            for z in indices:
                if lista[y]!=lista[z]:
                    resultadoDesempate=list(np.random.choice([lista[y],"empate",lista[z]],size=1000,p=probabilidades[y][z]))
                    puntosD[y]=puntosD[y]+ resultadoDesempate.count(lista[y])+resultadoDesempate.count("empate")/2
                    puntosD[z]=puntosD[z]+resultadoDesempate.count(lista[z])+resultadoDesempate.count("empate")/2
        maximoD=max(puntosD)
        indicesD = [i for i in range(len(puntosD)) if puntosD[i] == maximoD]
        for i in indicesD:
            victorias[i]=victorias[i]+1/len(indicesD)#sharing the point
    else:
        for i in indices:
            victorias[i]=victorias[i]+1
      
           
suma=sum(victorias)
print("Caruana: ", round(victorias[0]/suma*100,4))
print("Liren: ", round(victorias[2]/suma*100,4))
print("Giri: ", round(victorias[6]/suma*100,4))
print("Radjabov: ", round(victorias[1]/suma*100,4))
print("Nepo: ", round(victorias[5]/suma*100,4))
print("Hao: ", round(victorias[3]/suma*100,4))
print("Grischuk: ", round(victorias[4]/suma*100,4))
print("Alekseenko: ", round(victorias[7]/suma*100,4))
