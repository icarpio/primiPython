import random
with open('euromillones .csv','r') as lector:
    lineas = lector.read().splitlines()
    datos = []
    lineas.pop(0)
    for l in lineas:
        line = l.split(',')
        datos.append([line[0],line[1:6],line[7:9]])
    

i = int(input("Introduduce un numero del 1 al 1124: ---> "))
#i2 = random.sample(datos,1)
#print("Ha elegido la combinacion ganadora del: ", i2)

print("Ha elegido la combinacion ganadora del: ", datos[i])
