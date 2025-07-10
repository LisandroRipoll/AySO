#Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
# Si es invierno: solo se viaja a Bariloche.
# Si es verano: se viaja a Mar del plata y Cataratas.
# Si es otoño: se viaja a todos los lugares.
# Si es primavera: se viaja a todos los lugares menos Bariloche.

estacion = input("Ingrese estación del año (invierno, verano, otoño, primavera): ")

if estacion == "invierno":
    print("Solo se viaja a Bariloche.")
elif estacion == "verano":
    print("Se viaja a Mar del plata y Cataratas.")
elif estacion == "otoño":
    print("Se viaja a todos los lugares.")
elif estacion == "primavera":
    print("Se viaja a todos los lugares menos Bariloche.")
else:
    print("Estación invalida.")