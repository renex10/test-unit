# models/atm_machine.py

class ATM:
    def __init__(self, display):
        self.display = display
        self.bills_20000 = 0
        self.bills_10000 = 0
        self.balance = 0

    def deposit(self, amount):
        if not isinstance(amount, int) or amount <= 0:
            self.display.error("Por favor, ingrese un monto válido en números enteros positivos.")
            return
        if amount > 1000000:
            self.display.error("El monto a depositar no puede superar los $1,000,000.")
            return
        if amount % 10000 != 0:
            self.display.error("El monto a depositar solo puede ser múltiplo de $10,000.")
            return

        # Calcular cuántos billetes de $20,000 y $10,000 se pueden depositar
        bills_20000_to_add = amount // 20000
        amount_remaining = amount % 20000
        bills_10000_to_add = amount_remaining // 10000

        # Actualizar los billetes en el cajero
        self.bills_20000 += bills_20000_to_add
        self.bills_10000 += bills_10000_to_add

        # Mensaje de éxito
        self.display.success(f"Billetes depositados: {bills_20000_to_add} de $20,000 y {bills_10000_to_add} de $10,000.")
        self.display_balance()

    def withdraw(self, amount):
        if not isinstance(amount, int) or amount <= 0:
            self.display.error("Por favor, ingrese un monto válido en números enteros positivos.")
            return
        if amount % 10000 != 0:
            self.display.error("El monto a retirar solo puede ser múltiplo de $10,000 o $20,000.")
            return
        if amount > self.get_balance():
            self.display.error("Fondos insuficientes.")
            return

        # Lógica para el retiro de billetes
        bills_20000_to_withdraw = min(amount // 20000, self.bills_20000)
        amount -= bills_20000_to_withdraw * 20000
        bills_10000_to_withdraw = min(amount // 10000, self.bills_10000)
        amount -= bills_10000_to_withdraw * 10000

        # Si hay un monto restante que no se puede cubrir
        if amount > 0:
            self.display.error("Fondos insuficientes para el monto solicitado.")
            return

        # Actualizar el saldo y la cantidad de billetes
        self.bills_20000 -= bills_20000_to_withdraw
        self.bills_10000 -= bills_10000_to_withdraw
        self.display.success(f"Billetes retirados: {bills_20000_to_withdraw} de $20,000 y {bills_10000_to_withdraw} de $10,000.")
        self.display_balance()

    def get_balance(self):
        return self.bills_20000 * 20000 + self.bills_10000 * 10000

    def display_balance(self):
        balance = self.get_balance()
        self.display.info(f"Saldo actual: ${balance}")
