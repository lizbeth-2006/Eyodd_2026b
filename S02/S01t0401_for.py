"""
Escribir un programa qye calcule
la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa 
calculara la suma del 1 al 100
"""
# Importamos biblioteca time
import time

 # Tomando el tiempo inicial
timestamp_01 = time.time()

#Porgrama que calcula las suma
#de los "n" numeros naturales
n = 100
total_sum = 0

#Ciclo for 
for number in range(1,n+1):
    total_sum = total_sum + number
    # 1: sum <- 0 + 1
    # sum = 1
    # 2: sum <- 1 + 2
    # sum = 3
    # 3: sum <- 3 + 3
    # ...
    # 100: sum <- antSum + 100

print(f"La suma de 1 hasta {n} es: {total_sum}")

#  Tomando el tiempo final 
timestamp_02  = time.time()

# Impresion  del tiempo de ejecucion
print(f"Tiempo de ejucucion: {(timestamp_02-timestamp_01) * 1e6:.2f} μs")