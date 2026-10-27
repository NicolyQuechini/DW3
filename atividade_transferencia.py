from conta_bancaria import ContaBancaria, SaldoInsuficienteException

# 1. Criar as três contas e colocar o saldo inicial de cada uma
ana = ContaBancaria("123", "Ana Lima")
carlos = ContaBancaria("456", "Carlos Souza")
maria = ContaBancaria("789", "Maria Silva")

ana.depositar(500)
carlos.depositar(300)
maria.depositar(100)

# 2. Ana transfere R$ 200,00 para Carlos
ana.transferir(carlos, 200)
print("Ana transferiu R$ 200,00 para Carlos.")

# 3. Carlos transfere R$ 150,00 para Maria
carlos.transferir(maria, 150)
print("Carlos transferiu R$ 150,00 para Maria.")

# 4. Maria tenta transferir R$ 500,00 para Ana (ela não tem esse saldo!)
try:
    maria.transferir(ana, 500)
    print("Maria transferiu R$ 500,00 para Ana.")
except SaldoInsuficienteException:
    print("ERRO: Maria não tem saldo suficiente para transferir R$ 500,00.")

# 5. Transferência para a própria conta (também dá erro)
try:
    ana.transferir(ana, 50)
    print("Ana transferiu para ela mesma.")
except ValueError as erro:
    print("ERRO:", erro)

# 6. Mostrar o saldo final das três contas
print()
print("--- SALDO FINAL ---")
print("Ana Lima:", ana.get_saldo())
print("Carlos Souza:", carlos.get_saldo())
print("Maria Silva:", maria.get_saldo())