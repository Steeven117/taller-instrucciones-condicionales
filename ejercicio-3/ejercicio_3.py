# Valor de un articulo

print("--------------------------------------")
print("------------BIENVENIDO----------------")
print("--------------------------------------")

# INPUT

A = int(input("Ingrese el valor del articulo: "))

# PROCESSING


if A< 3000:
    B = (15*A)/100
    
else:
    if 3000<=A<= 6000:
        B = 500
    else: 
      B = (25*A)/100


rta = A + B

# OUTPUT

print("----------------------------------------")
print("--------EL VALOR DEL PRODUCTO ES--------")
print(rta)
print("----------------------------------------")