balance = 1000
quantity_op = int(input("Cuantas operaciones desea realizar? "))

for i in range(quantity_op):
    op = int(input("1 → Consultar saldo \n2 → Retirar Dinero \n3 → Depositar Dinero \n"))

    match op:
        case 1:
            print(balance)
        case 2:
            while True:
                mount = float(input("Ingrese el monto a retirar "))
                if mount < 0:
                    print("Ingrese un monto valido ")
                    continue
                else:
                    if mount >= balance:
                        print("Fondos insuficientes")
                    else:
                        balance -= mount
                        print(f"\nEl nuevo saldo es: {balance}\n")
                break
        case 3:
            while True:
                mount = float(input("Ingrese el monto a depositar "))
                if mount < 0:
                    print("Ingrese un monto valido ")
                    continue
                else:
                    balance += mount
                    print(f"\nEl nuevo saldo es: {balance}\n")
                break
        case _:
            print("Error")
