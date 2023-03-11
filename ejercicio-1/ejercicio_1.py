# INPUT

print("----------------------------------------------------")
print("---------EN QUE CUADRANTE Y EJE SE ENCUENTRA--------")
print("----------------------------------------------------")

x = int (input(" el valor de x: "))
y = int (input(" el valor de y: "))

#PROCESSING

if x==0 and y==0 :

    rt = "origen"
else :

    if x==0 and (y>0 or y<0) :

        rt = "Está en el eje Y"

    else :
        if y==0 and (x>0 or x<0) :

            rt = "Está en el eje X"
        
        else :

            if x>0 and y>0 :

                rt = f"Se encuentra en el primer cuadrante {x, y}"
            
            else :

                if  x<0 and y>0:

                    rt = f"Se encuentra en el segundo cuadrante {x, y}"

                else :
                    
                    if x<0 and y<0 :

                        rt = f"Se encuentra en el tercer cuadrante {x, y}"

                    else :

                        x>0 and y<0

                        rt = f"Se encuentra en el cuarto cuadrante {x, y}"


# OUTPUT
print("--------------------------------------------------------------")
print("---------------------LA RESPUESTA ES--------------------------")
print(rt)