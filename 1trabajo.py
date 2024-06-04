# ingresamos la condicionales
lado = (" ");
Apotema = (" ");
base = ("");
baseMayor = ("");
baseMenor = ("");
altura = (" ")
area = (" ")
Perimetro = (" ")
altura = (" ")
while True:  # definimos bucle
    print("1: Pentagono")
    print("2: Hexagono")
    print("3: Trapecio")
    print("4: Paralelogramo")
    print("5: Salir")
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        lado = int(input("lado "))
        Apotema = int(input("Apotema "))
        Perimetro = lado * 5  # definimos formula perimetro
        print("perimetro =", Perimetro, "cm2")
        area = Perimetro * Apotema / 2  # definimos formula area
        print("area =", area, "cm2")
    elif opcion == 2:
        lado = int(input("lado "))
        Apotema = int(input("Apotema "))
        Perimetro = lado * 6  # definimos formula perimetro
        print("perimetro =", Perimetro, "cm2")
        area = (Perimetro * Apotema) / (2)  # definimos formula area
        print("area =", area, "cm2")
    elif opcion == 3:
        lado = int(input("lado "))
        baseMayor = int(input("B "))
        baseMenor = int(input("b "))
        altura = int(input("H "))
        area = (baseMayor + baseMenor) / (2) * (altura)  # definimos formula area
        print("area =", area, "cm2")
        Perimetro = baseMayor + baseMenor + lado + lado  # definimos formula perimetro
        print("perimetro =", Perimetro, "cm2")
    elif opcion == 4:
        base = int(input("Base "))
        altura = int(input("H "))
        lado = int(input("laado "))
        area = base * altura  # definimos formula area
        print("area =", area, "cm2")
        Perimetro = (2) * (base + lado)  # definimos formula perimetro
        print("perimetro =", Perimetro, "cm2")
    else:
        opcion == 5
        print("salir")
        break  # rompemos el bucle

