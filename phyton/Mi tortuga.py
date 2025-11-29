print("Simulación de los pasos de una tortuga")

posicion = 0


def adelante(n):
    global posicion
    posicion = n
    print("🏁" + "-" * n )


def abajo(n):
    for i in range(n - 1):
        print(" " * (posicion + 2) + "|")
    print(" " * (posicion + 2) + "🐢")

 # escalon 1
adelante(10)
abajo(8)        
# escalon 2
adelante(10)    
abajo(8) 
# escalon 3
adelante(10)  
abajo(8)





    

