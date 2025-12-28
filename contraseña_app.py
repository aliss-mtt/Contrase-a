import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pregunta = int(input("introduzca la longitud de la contrasena"))
contrasena = ""

for i in range(pregunta):
    contrasena =contrasena+ random.choice(caracteres)

print ("tu contrasena es:", contrasena)
