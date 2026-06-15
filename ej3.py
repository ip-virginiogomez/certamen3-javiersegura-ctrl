#**Enunciado:**
#Un supermercado aplica descuentos especiales a sus clientes. Para acceder al descuento, el cliente debe ser mayor de 60 años o tener una tarjeta de socio, y además el total de su compra debe superar los $10.000.

#**Indicaciones paso a paso:**
#1. Solicita al usuario su edad, si tiene tarjeta de socio (sí/no) y el monto total de su compra.
#2. Verifica si cumple las condiciones: el monto debe superar $10.000 y debe ser mayor de 60 años o tener tarjeta de socio.
#3. Muestra un mensaje indicando si obtiene el descuento del 15% o si no califica, mostrando el monto final en cada caso.

edad=int(input("ingrese su edad: "))
socio=input("tiene tarjeta socio si/no: ")
compra=int(input("ingrese el monto total de su compra: "))

if edad>=60 or socio=="si" and compra >10000:
    print("felicidades tienes un descuento del 15%")
    total=compra*0.85
    print(f"el total con el descuento aplicado es de {total}")

else:
    print(f"no clasifica con el descuento el monto es {compra}")