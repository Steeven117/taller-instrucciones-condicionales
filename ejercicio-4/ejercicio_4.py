# CALCULAR PESO

print("-------------------------------------------------")
print("----------------BIENVENIDO-----------------------")
print("-------------------------------------------------")

#INPUT

a = int(input("Digite el valor del peso en kg: "))
b = float(input("Digite el valor de la altura en m: "))


c = a/(b*2)

# PROCESSING

if c<16:
    rta= "Ve al hospital"
else:
    if 16<=c<17:
        rta = "infrapeso"
    else:
        if 17<=c<18:
            rta= "Bajo peso"
        else:
            if 18<=c<25:
                rta="peso normal"
            else:
                if 25<=c<30:
                    rta= "Sobrepeso"
                else:
                    if 30<=c<35:
                        rta= "Sobrepeso cronico"
                    else:
                        if 35<=c<40:
                            rta="Obesidad premorbida"
                        else:
                            rta= "Obesidad morbida "

# OUTPUT

print(rta)

print("---------------------------------------------------")
print("------------- -COME SALUDABLEMENTE-----------------")
print("---------------------------------------------------")
