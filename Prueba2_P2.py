lista=[]
precioDolar=float(input("Ingrese los precios en dolares:"))
while precioDolar!=9.99:
    lista.append(precioDolar)
    precioDolar=float(input("Ingrese los precios en dolares:"))
print(lista)

pesoChile=950
valorchile=lista[0]*pesoChile, lista[1]*pesoChile, lista[2]*pesoChile, lista[3]*pesoChile, lista[4]*pesoChile, lista[5]*pesoChile, lista[6]*pesoChile, lista[7]*pesoChile, lista[8]*pesoChile, lista[9]*pesoChile
lista.clear()
lista.append(valorchile)
print("precio ingresados en pesos chilenos:", lista)