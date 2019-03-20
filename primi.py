import random
with open('primitiva.csv','r') as lector:
    lineas = lector.read().splitlines()
    datos = []
    lineas.pop(0)
    for l in lineas:
        line = l.split(',')
        datos.append([line[0],line[1:7]])

i = int(input("Introduduce un numero del 1 al 573: ---> "))
#i2 = random.sample(datos,1)
#print("Ha elegido la combinacion ganadora del: ", i2)

print("Ha elegido la combinacion ganadora del: ", datos[i])

