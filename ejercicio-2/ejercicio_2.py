# Generador de Credito

print("-------------------------------------")
print("------------BIENVENIDO---------------")
PRINT("-------------------------------------")

#INPUT

A = int(input("Ingrese el valor de su sueldo actual: "))

# PROCESSING

if A<945200 :

    rta = "tu crédito fue denegado"

else :

    y = int(input("si tiene deudas ingrese 1, de lo contrario ingrese otro valor:  "))

    if y==1 :
        
        rta= "tu crédito fue denegado"

    else : 

        rta = "tu crédito fue aprovado"

# OUTPUT

print (rta)

print("----------------------------------------------")
print("-------------QUE TENGA BUEN DIA---------------")
print("----------------------------------------------")

