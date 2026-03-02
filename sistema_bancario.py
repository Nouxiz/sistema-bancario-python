
class ContaBancaria():
    def __init__(self, nome):
      self.saldo = 0
      self.historico = []
      self.nome = nome

    def deposito(self):
      while True:
          try:
            valor = float(input("Digite o quanto você vai depositar: "))
            if valor > 0:
              self.saldo += valor
              self.historico.append(f'Depósito R$ {valor:.2f}')
              print("Depósito realizado com sucesso!")
              return
            elif valor <= 0:
              print("Digite um valor válido")
            continue
        
          except:
            print("Digite apenas número")

    def sacar(self):
        while True:
          try:
              valor = float(input("Digite o quanto vai sacar"))
              if valor <= 0:
                print("Digite um valor correto")
              elif valor > self.saldo:
                print("Saldo insuficiente")
              else:
                self.saldo -= valor
                print("Saque feito")
                self.historico.append(f"Saque R$ {valor:.2f}")
              return
          except:
            print("Digite um valor válido")
         
        
        

    def ver_saldo(self):
      print(f"Você tem {self.saldo:.2f}")

    def transacoes(self):
      if not self.historico:
        print("Nenhuma movimentação")
      else:
        for item in self.historico:
            print(item)

nome_usuario = input("Digite seu nome:")
minha_conta = ContaBancaria(nome_usuario)

while True:
    try:
      print(f'Olá {nome_usuario} Tudo bem?')
      print("1- Saque")
      print("2- Extrato")
      print("3- Deposito")
      print("4- Ver saldo")
      print("0- Sair")

      opcao = int(input("Digite uma das opções: "))

      if opcao == 1:
        minha_conta.sacar()
      elif opcao == 2:
        minha_conta.transacoes()
      elif opcao == 3:
        minha_conta.deposito()
      elif opcao == 4:
        minha_conta.ver_saldo()
      elif opcao == 0:
        print("Sessão Encerrada..")
        break
      else:
         print("Opção Inválida")
    except:
       print("Opção Inválida")