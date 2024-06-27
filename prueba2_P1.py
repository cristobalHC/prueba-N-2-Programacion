lista=[]
notas=input("Ingrese las notas:")
while notas!="0":
    lista.append(notas)
    notas=input("Ingrese las notas:")
lista.sort()
c=(len(lista))
suma=notas+notas
promedio=suma/c

print("La cantidad de notas en la lista es de", c)
print("El promedio de notas es de:")
print("La nota minima fue de:", (lista[0]))
lista.reverse()
print("La nota maxima fue de:", (lista[0]))