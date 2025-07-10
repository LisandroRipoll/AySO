""" Facturación del Servicio de Agua Potable
El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. Para garantizar un uso eficiente del recurso y establecer una estructura justa de costos,
se han definido diferentes tarifas y ajustes según el consumo y el tipo de cliente.
Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y un costo variable por metro cúbico consumido. Además, se aplican bonificaciones y recargos
dependiendo del consumo y la categoría del usuario. En algunos casos especiales, también pueden otorgarse descuentos adicionales.

A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios para determinar el monto final a pagar.
Tarifa base:
* Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
* El costo por metro cúbico (m³) de agua es de $200/m³.
Bonificaciones y Recargos según tipo de cliente:
-Cliente Residencial:
* Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
* Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.
-Cliente Comercial:
* Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
* Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
* Si el consumo es menor a 50 m³, se aplica un recargo del 5%.
-Cliente Industrial:
* Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
consumo.
* Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
* Si el consumo es menor a 200 m³, se aplica un recargo del 10%.
-Casos especiales:
* Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.
* En todos los casos, se aplica el IVA del 21% sobre el total.
-Requerimientos del programa:
-Solicitar al usuario:
* Cantidad de metros consumidos
* Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.
-Calcular:
* Subtotal de consumo.
* Bonificaciones, si corresponde
* Recargos, si corresponde
* Subtotal, con recargos y bonificaciones.
* IVA aplicado (21%), si corresponde.
* Total final a pagar.
* Mostrar en pantalla el desglose de los cálculos. """

resultado_bonificación = 0
resultado_recargo = 0
resultado_total = 0
subtotal_consumo = 0
subtotal_recarga_bonificacion = 0
total = 0

metros_consumidos = int(input("Ingrese metros consumidos: "))
tipo_de_cliente = input("Ingrese tipo de cliente(Residencial, Comercial o Industrial): ")

subtotal = (metros_consumidos * 200) + 7000

#-Cliente Residencial:
#* Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
#* Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo."""
# * Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones es menor a $35000, se aplica un descuento adicional del 5%.

if tipo_de_cliente == "Residencial":
    if subtotal < 35000:
        resultado_bonificación_plus = subtotal * 0.05
    if metros_consumidos < 30:
        resultado_bonificación = (subtotal * 0.10) + resultado_bonificación_plus
    elif metros_consumidos > 80:
        resultado_recargo = subtotal * 1.15

# -Cliente Comercial:
# * Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
# * Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
# * Si el consumo es menor a 50 m³, se aplica un recargo del 5%.

if tipo_de_cliente == "Comercial":
    if metros_consumidos < 50:
        resultado_recargo = subtotal * 1.05
    elif metros_consumidos > 150:
        resultado_bonificación = subtotal * 0.08
    elif metros_consumidos > 300:
        resultado_bonificación = subtotal * 0.12

#-Cliente Industrial:
# * Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
# consumo.
# * Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
# * Si el consumo es menor a 200 m³, se aplica un recargo del 10%.

if tipo_de_cliente == "Industrial": 
    if metros_consumidos > 500:   
        resultado_bonificación = subtotal * 0.20
    elif metros_consumidos > 1000:
        resultado_bonificación = subtotal * 0.30
    elif metros_consumidos < 200:
        resultado_recargo = subtotal * 1.10

# -Casos especiales:
# * En todos los casos, se aplica el IVA del 21% sobre el total.
# * Subtotal de consumo.
# * Bonificaciones, si corresponde
# * Recargos, si corresponde
# * Subtotal, con recargos y bonificaciones.
# * IVA aplicado (21%), si corresponde.
# * Total final a pagar.
# * Mostrar en pantalla el desglose de los cálculos. 

subtotal_recarga_bonificacion = subtotal - resultado_bonificación + resultado_recargo
total = subtotal_recarga_bonificacion * 1.21

print("Subtotal de consumos:", subtotal)
print("Bonificación:",resultado_bonificación)
print("Recargo:", resultado_recargo)
print("Subtotal con recargo y bonificación:", subtotal_recarga_bonificacion)
print("IVA aplicado: 21%")
print("Total final a pagar: $",total)