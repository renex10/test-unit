# tests/test_atm_machine.py

import unittest
from unittest.mock import Mock
from models.atm_machine import ATM  # Importación del módulo ATM desde models

class TestATM(unittest.TestCase):
    def setUp(self):
        self.display_mock = Mock()
        self.atm = ATM(self.display_mock)

    def test_deposit_valid_amount(self):
        # Depositar una cantidad válida
        self.atm.deposit(50000)
        self.display_mock.success.assert_called_with("Billetes depositados: 2 de $20,000 y 1 de $10,000.")
        self.display_mock.info.assert_called_with("Saldo actual: $50000")

    def test_deposit_invalid_amount_type(self):
        # Depositar un tipo de cantidad inválida
        self.atm.deposit("10000")
        self.display_mock.error.assert_called_with("Por favor, ingrese un monto válido en números enteros positivos.")

    def test_deposit_amount_exceeds_limit(self):
        # Depositar una cantidad que excede el límite
        self.atm.deposit(1500000)
        self.display_mock.error.assert_called_with("El monto a depositar no puede superar los $1,000,000.")

    def test_deposit_invalid_multiple(self):
        # Depositar una cantidad no múltiplo de $10,000
        self.atm.deposit(15000)
        self.display_mock.error.assert_called_with("El monto a depositar solo puede ser múltiplo de $10,000.")

    def test_withdraw_valid_amount(self):
        # Retirar una cantidad válida
        self.atm.deposit(50000)
        self.atm.withdraw(30000)
        self.display_mock.success.assert_called_with("Billetes retirados: 1 de $20,000 y 1 de $10,000.")
        self.display_mock.info.assert_called_with("Saldo actual: $20000")

    def test_withdraw_invalid_multiple(self):
        # Retirar una cantidad que no es múltiplo de $10,000 o $20,000
        self.atm.withdraw(25000)
        self.display_mock.error.assert_called_with("El monto a retirar solo puede ser múltiplo de $10,000 o $20,000.")

    def test_withdraw_insufficient_funds(self):
        # Retirar una cantidad sin fondos suficientes
        self.atm.deposit(20000)
        self.atm.withdraw(40000)
        self.display_mock.error.assert_called_with("Fondos insuficientes.")

    # Prueba que el monto a retirar sea múltiplo de $10000 o $20000
    def test_withdraw_multiple_of_10000_or_20000(self):
        self.atm.deposit(100000)
        self.atm.withdraw(5000)
        self.display_mock.error.assert_called_with("El monto a retirar solo puede ser múltiplo de $10,000 o $20,000.")

    # Prueba la extracción con una combinación válida de billetes
    def test_valid_bill_combination_withdrawal(self):
        self.atm.deposit(70000)
        self.atm.withdraw(50000)
        self.display_mock.success.assert_called_with("Billetes retirados: 2 de $20,000 y 1 de $10,000.")
        self.display_mock.info.assert_called_with("Saldo actual: $20000")

    # Prueba cuando no es posible entregar el monto con los billetes disponibles
    def test_withdraw_insufficient_bills(self):
        self.atm.deposit(40000)  # Solo hay billetes de $10,000 y $20,000
        self.atm.withdraw(30000)  # Intento de retirar con combinación no posible
        self.display_mock.error.assert_called_with("Fondos insuficientes para el monto solicitado.")

    # Verifica que no se pueda depositar más de $1,000,000
    def test_deposit_exceeds_limit(self):
        self.atm.deposit(1000001)
        self.display_mock.error.assert_called_with("El monto a depositar no puede superar los $1,000,000.")

    # Prueba que no se puedan depositar cantidad de billetes negativos
    def test_deposit_negative_amount(self):
        self.atm.deposit(-50000)
        self.display_mock.error.assert_called_with("Por favor, ingrese un monto válido en números enteros positivos.")

    # Verifica que el depósito de billetes se realice correctamente
    def test_correct_bill_deposit(self):
        self.atm.deposit(100000)  # 5 billetes de $20,000
        self.display_mock.success.assert_called_with("Billetes depositados: 5 de $20,000 y 0 de $10,000.")
        self.display_mock.info.assert_called_with("Saldo actual: $100000")

if __name__ == '__main__':
    unittest.main()
