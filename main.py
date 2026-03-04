balance = 1000

while True:
    try:
        quantity_op = int(input("Cuantas operaciones desea realizar? "))
        if quantity_op < 0:
            print("\nPor favor ingrese un valor valido \n")
            continue
        break
    except ValueError:
        print("\nPor favor solo digite valores numericos \n")

for i in range(quantity_op):

    while True:
        try:
            op = int(input("\n1 → Consultar saldo \n2 → Retirar Dinero \n3 → Depositar Dinero \n"))

            if op not in (1, 2, 3):
                print("\nOpción inválida \n")
                continue
            break
        except ValueError:
            print("\nPor favor solo digite valores numericos \n")
    
    match op:
        case 1:
            print(balance)
        case 2:
            while True:
                try:
                    mount = float(input("Ingrese el monto a retirar "))
                    if mount < 0:
                        print("Ingrese un monto valido \n")
                        continue
                    else:
                        if mount > balance:
                            print("Fondos insuficientes")
                        else:
                            balance -= mount
                            print(f"\nEl nuevo saldo es: {balance}\n")
                    break
                except ValueError:
                    print("Por favor solo digite valores numericos \n")
        case 3:
            while True:
                try:
                    mount = float(input("Ingrese el monto a depositar "))
                    if mount < 0:
                        print("Ingrese un monto valido \n")
                        continue
                    else:
                        balance += mount
                        print(f"\nEl nuevo saldo es: {balance}\n")
                    break
                except ValueError:
                    print("Por favor solo digite valores numericos \n")
        case _:
            print("Error")
print("\nGracias por usar el cajero automático")
