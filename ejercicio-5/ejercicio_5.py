# Calcular costo del agua segun los m3

print("-----------------------------------------")
print("-------VALOR SEGUN m3 GASTADOS-----------")
print("-----------------------------------------")

#INPUT

a= int(input("Ingrese el valor en metros cubicos: "))

# PROCESSING

if a<51:
    rta = f"Su costo es de: {10000}"
else:
    if 51<=a<200:
        rta = f"su costo es de: {2000+10000}"
    else:
        rta = f"su costo es de: {3000+10000}"

# OUTPUT

print("---------------------------------------")
print("-----------EL COSTO ES DE--------------")
print(rta)
print("---------------------------------------")
