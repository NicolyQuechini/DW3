from conta_bancaria import ContaBancaria

import unittest
from conta_bancaria import ContaBancaria, SaldoInsuficienteException


class TestContaBancaria(unittest.TestCase):

    # CT01 - conta criada com dados válidos
    def test_ct01_criar_conta(self):
        conta = ContaBancaria("123", "Ana Lima")
        self.assertEqual(conta.numero, "123")
        self.assertEqual(conta.titular, "Ana Lima")
        self.assertEqual(conta.get_saldo(), 0.0)

    # CT02 - titular com menos de 3 letras
    def test_ct02_titular_curto(self):
        with self.assertRaises(ValueError):
            ContaBancaria("123", "Al")

    # Extras do RF01
    def test_numero_vazio(self):
        with self.assertRaises(ValueError):
            ContaBancaria("", "Ana Lima")

    def test_numero_nulo(self):
        with self.assertRaises(ValueError):
            ContaBancaria(None, "Ana Lima")

    def test_titular_nulo(self):
        with self.assertRaises(ValueError):
            ContaBancaria("123", None)

    # CT03 - depositar 100
    def test_ct03_depositar(self):
        conta = ContaBancaria("123", "Ana Lima")
        conta.depositar(100)
        self.assertEqual(conta.get_saldo(), 100.0)

    # CT04 - depositar 0
    def test_ct04_depositar_zero(self):
        conta = ContaBancaria("123", "Ana Lima")
        with self.assertRaises(ValueError):
            conta.depositar(0)
        self.assertEqual(conta.get_saldo(), 0.0)

    # CT05 - depositar valor negativo
    def test_ct05_depositar_negativo(self):
        conta = ContaBancaria("123", "Ana Lima")
        with self.assertRaises(ValueError):
            conta.depositar(-50)
        self.assertEqual(conta.get_saldo(), 0.0)

    # CT06 - sacar 40 de 100
    def test_ct06_sacar(self):
        conta = ContaBancaria("123", "Ana Lima")
        conta.depositar(100)
        conta.sacar(40)
        self.assertEqual(conta.get_saldo(), 60.0)

    # CT07 - sacar exatamente o saldo
    def test_ct07_sacar_tudo(self):
        conta = ContaBancaria("123", "Ana Lima")
        conta.depositar(100)
        conta.sacar(100)
        self.assertEqual(conta.get_saldo(), 0.0)

    # CT08 - sacar mais do que tem
    def test_ct08_sacar_demais(self):
        conta = ContaBancaria("123", "Ana Lima")
        conta.depositar(100)
        with self.assertRaises(SaldoInsuficienteException):
            conta.sacar(100.01)
        self.assertEqual(conta.get_saldo(), 100.0)

    # Extra do RF03 - sacar valor inválido
    def test_sacar_valor_invalido(self):
        conta = ContaBancaria("123", "Ana Lima")
        conta.depositar(100)
        with self.assertRaises(ValueError):
            conta.sacar(0)
        self.assertEqual(conta.get_saldo(), 100.0)

    # CT09 - transferir 30 de 100
    def test_ct09_transferir(self):
        origem = ContaBancaria("123", "Ana Lima")
        destino = ContaBancaria("456", "Bruno Souza")
        origem.depositar(100)
        origem.transferir(destino, 30)
        self.assertEqual(origem.get_saldo(), 70.0)
        self.assertEqual(destino.get_saldo(), 30.0)

    # CT10 - transferir para a própria conta
    def test_ct10_transferir_para_si_mesma(self):
        conta = ContaBancaria("123", "Ana Lima")
        conta.depositar(100)
        with self.assertRaises(ValueError):
            conta.transferir(conta, 30)
        self.assertEqual(conta.get_saldo(), 100.0)

    # Extra do RF04 - destino nulo
    def test_transferir_destino_nulo(self):
        conta = ContaBancaria("123", "Ana Lima")
        conta.depositar(100)
        with self.assertRaises(ValueError):
            conta.transferir(None, 30)
        self.assertEqual(conta.get_saldo(), 100.0)

    # Extra do RF04 - falhou, então nenhuma conta muda
    def test_transferir_sem_saldo(self):
        origem = ContaBancaria("123", "Ana Lima")
        destino = ContaBancaria("456", "Bruno Souza")
        origem.depositar(50)
        with self.assertRaises(SaldoInsuficienteException):
            origem.transferir(destino, 80)
        self.assertEqual(origem.get_saldo(), 50.0)
        self.assertEqual(destino.get_saldo(), 0.0)


if __name__ == "__main__":
    unittest.main()


#retirar 80 reais...

 

conta1.transferir(conta2, 80)
 

print("--- DEPOIS DA TRANSFERÊNCIA ---")
print("Saldo da conta1:", conta1.get_saldo())
print("Saldo da conta2:", conta2.get_saldo())
 


