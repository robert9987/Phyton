import operaciones

numeros = []

for i in range(5):
    numero = int(input("Escribe un numero: "))
    numeros.append(numero)

suma = operaciones.sumar_lista(numeros)

promedio = operaciones.sacar_promedio(numeros)

mayor = operaciones.encontrar_mayor(numeros)

print("Tu lista de numeros es:", numeros)
print("La suma total es", suma)
print("El promedio es", promedio)
print("El numero mayor es", mayor)

input("Presiona Enter para salir...")

# Ejercicio de hoja de números