# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar 
# la posición del jugador en la cancha, considerando los siguientes parámetros:
# * Menos de 160 cm: Base
# * Entre 160 cm y 179 cm: Escolta
# * Entre 180 cm y 199 cm: Alero
# * 200 cm o más: Ala-Pívot o Pívot 

altura = int(input("Ingrese estatura del jugador: "))
 
if altura <= 160 :
  print("Posición del jugador: Base")
elif altura < 180:
    print("Posición del jugador: Escolta")
elif altura < 200:
   print("Posición del jugador: Alero")
else:
    print("Posición del jugador: Ala-Pívot o Pívot")