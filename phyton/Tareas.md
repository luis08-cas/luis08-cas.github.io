#  Implementando la tortuga

# Reto 1

## Asi hacemos que una tortuga se mueva hacia adelante usando `input`  y  `print`

```python
print("Simulacion de los paosos de una tortuga")
pasos = int(input("¿Cuántos pasos quieres que avance la tortuga? "))

print("La tortuga avanza", pasos, "pasos.")

print("🏁" + "-" * pasos + "🐢")
```

<img width="369" height="55" alt="Captura de pantalla 2025-11-26 140520" src="https://github.com/user-attachments/assets/1c78a54b-bbf9-4448-8a1d-7833319d794a" />



### Cometarios
Como hacer que la toruga e pasos hacia adelante usando print, input y pidiendo los datos al usuario. 

# Reto 2

## Tortuga bajando

```python
print("Simulacion de los pasos de una tortuga") 

Pasos_abajo = int(input("¿Cuántos pasos quieres que baje la tortuga? "))

print("La tortuga baja", Pasos_abajo, "pasos.")

print("🏁") 

for i in range(Pasos_abajo):
 print("|")

print("🐢")
```
<img width="406" height="208" alt="Captura de pantalla 2025-11-26 145600" src="https://github.com/user-attachments/assets/87d60896-4225-4063-91f3-b21e217aaa85" />

### Comentarios
Igualente que en el reto 1, utilizamos print y input y pedimos datos al usuario para que la tortuga baje

# Reto 3

## Tortuga girando

```python
print("Simulacion de los pasos de una tortuga") 

Pasos_adelante =int(input("¿Cuántos pasos quieres que avance la tortuga? "))
Pasos_abajo = int(input("¿Cuántos pasos quieres que baje la tortuga? "))

print("La tortuga avanza", Pasos_adelante, "pasos.")
print("La tortuga baja", Pasos_abajo, "pasos.")


print("🏁" + "-" * Pasos_adelante )

for i in range(Pasos_abajo):
    print(" " * (Pasos_adelante + 2 ) + "|" )

print(" " * (Pasos_adelante + 1) + "🐢")
```
<img width="371" height="181" alt="Captura de pantalla 2025-11-28 193358" src="https://github.com/user-attachments/assets/41e63a5a-e1a6-41b7-a54d-76d9155d36f7" />

### Cometarios
Podemos ver como la tortuga avanza y hace un giro hacia abajo, todo esto utilizacon print y input, igualmente preguntando al usuario 

# Reto 4

## Tortuga avanza y baja usando funciones

```python
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


adelante(16)
abajo(7)
```
<img width="301" height="155" alt="Captura de pantalla 2025-11-28 195056" src="https://github.com/user-attachments/assets/3dd435f8-78a3-45ba-9d64-912102a17fc0" />

### Comentarios
En este ejercicio podemos ver como ya no se preguntan los datos al usuario, si no que se programan ess datos para que sea de forma automatica, osea utilizando funciones

# Reto 5

## La tortuga bajando escalas

```python
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
```
<img width="182" height="458" alt="Captura de pantalla 2025-11-28 201314" src="https://github.com/user-attachments/assets/072c6480-5dc1-4418-a4f9-7c9cef435da4" />

### Cometarios
De igual forma, utilizamos funciones para que los movimientos de la tortuga sean automaticos, sin necesidad de preguntar al usuario


