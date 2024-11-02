from models.atm_machine import ATM

def main():
    atm = ATM(balance_file="data/initial_balance.json")

    while True:
        print("\nOpciones:")
        print("1. Retirar dinero")
        print("2. Depositar dinero")
        print("3. Salir")
        
        option = input("Seleccione una opción (1/2/3): ")

        if option == "1":
            try:
                amount = int(input("Ingrese la cantidad que desea retirar: "))
                if amount % 10000 != 0:
                    atm.display.error("El monto a retirar debe ser un múltiplo de $10,000 o $20,000.")
                else:
                    atm.withdraw(amount)
            except ValueError:
                atm.display.error("Por favor, ingrese un monto válido en números enteros.")
        
        elif option == "2":
            try:
                amount = int(input("Ingrese la cantidad que desea depositar: "))
                if amount % 10000 != 0:
                    atm.display.error("El monto a depositar debe ser un múltiplo de $10,000 o $20,000.")
                else:
                    atm.deposit(amount)
            except ValueError:
                atm.display.error("Por favor, ingrese un monto válido en números enteros.")

        elif option == "3":
            print("Gracias por usar el cajero automático.")
            break
        else:
            atm.display.error("Opción inválida. Por favor, seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()
