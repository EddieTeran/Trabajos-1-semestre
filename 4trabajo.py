# DECLARAMOS LAS VARIABLES
opcion =0 ;suma_total = 0;cantProducto = 0;Articulo = ""
Blusa = 32;Pantalon = 45;Camisas = 29;Brasier = 28;Medias = 8.20

print("Artículos Caprichos Store \n\n")
print(
    " 1.- Blusa       ***    $32\n 2.- Pantalon    ***    $45\n 3.- Camisas     ***    $29\n 4.- Brasier     ***    $28\n 5.- Medias      ***    $8.20\n 6.- Terminar\n")

while True:
    opcion = int(input("Seleccione el producto: "))  # SOLICITAMOS QUE ESCOJA LA PRENDA
    # CREAMOS LAS ESTRUCTURAS DE CONTROL
    if opcion == 1:

        # PEDIMOS QUE INGRESE LA CANTIDAD DE ITEMS
        cantProducto = int(input("cuantas Blusas desea ? = "))

        # CREAMOS LAS FORMULAS
        subTotal = cantProducto * Blusa
        suma_total = suma_total + subTotal

        # STRING
        Articulo = Articulo + "|Blusas       | " + "| Cantidad  " + str(cantProducto) + "|" + " |PVP $" + str(Blusa) +"  |  | subtotal " + " $ " + str(subTotal)  + "\n"
    elif opcion == 2:
        cantProducto = int(input("cuantos Pantalones desea ? = "))
        subTotal = cantProducto * Pantalon
        suma_total = suma_total + subTotal
        Articulo = Articulo + "|Pantalones   | " + "| Cantidad  " + str(cantProducto) + "|" + " |PVP $" + str(
        Pantalon) + "  |  | subtotal " + " $ " + str(subTotal) + "\n"

    elif opcion == 3:
        cantProducto = int(input("cuantas Camisas desea ?  = "))
        subTotal = cantProducto * Camisas
        suma_total = suma_total + subTotal
        Articulo = Articulo + "|Camisas      | " + "| Cantidad  " + str(cantProducto) + "|" + " |PVP $" + str(
            Camisas) + "  |  | subtotal " + " $ " + str(subTotal) + "\n"

    elif opcion == 4:
        cantProducto = int(input("cuantos Brasier desea ? = "))
        subTotal = cantProducto * Brasier
        suma_total = suma_total + subTotal
        Articulo = Articulo + "|Brasier      | " + "| Cantidad  " + str(cantProducto) + "|" + " |PVP $" + str(
            Brasier) + "  |  | subtotal " + " $ " + str(subTotal)  + "\n"

    elif opcion == 5:
        cantProducto = int(input("cuantos pares de Medias desea ? = "))
        subTotal = cantProducto * Medias
        suma_total = suma_total + subTotal
        Articulo = Articulo + "|Medias       | " + "| Cantidad  " + str(cantProducto) + "|" + " |PVP $" + str(
            Medias) + " |  | subtotal " + " $ " + str(subTotal)  + "\n"
    elif opcion == 6:
        print("\n\nLista de artículos seleccionados")
        print(Articulo + "\n          TOTAL ARTICULOS SIN DESCUENTO ", suma_total)
        break  # SALIMOS DEL BUCLE
    else:
        print("No existe producto con el item solicitado")

    # CREAMOS LA FUNCION

def calcular_descuento(monto_total, porcentaje_descuento=5):
    """
    Esta función calcula el descuento aplicado a un monto total, teniendo en cuenta un porcentaje de descuento predeterminado."""

    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# CALCULO CON EL5%
monto_compra = suma_total
descuento = calcular_descuento(monto_compra)
total = suma_total - descuento
print(f'Descuento ***con tarjeta*** 5% : {descuento}')
print(f" Total a pagar tarjeta: ${total}"+"\n")

# CALCULO CON EL 10%
monto_compra = suma_total
descuento = calcular_descuento(monto_compra, 10)
total = suma_total - descuento
print(f'Descuento ***efectivo***  10%  : {descuento}')
print(f" Total a pagar en efectivo: ${total}")
print("""***GRACIAS POR SU COMPRA***
      """)