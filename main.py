import tkinter as tk
from tkinter import messagebox

# Definindo as variáveis de controle
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Função para autenticação de CPF e senha
def autenticar():
    cpf = entry_cpf.get()
    senha = entry_senha.get()
    
    # Verifica se o CPF e a senha estão corretos (você pode substituir esta verificação por uma real)
    if cpf == "12345678900" and senha == "1234":  # Exemplo de CPF e senha válidos
        messagebox.showinfo("Autenticado", "Login realizado com sucesso!")
        janela_login.destroy()  # Fecha a janela de login
        menu_banco()  # Chama o menu bancário
    else:
        messagebox.showerror("Erro", "CPF ou senha incorretos. Tente novamente.")

# Função para o menu bancário
def menu_banco():
    global saldo, limite, extrato, numero_saques
    
    while True:
        menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        """
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do seu depósito: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("Operação realizada com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor que deseja sacar: "))

            saldo_excedeu = valor > saldo
            limite_excedeu = valor > limite
            saque_excedeu = numero_saques >= LIMITE_SAQUES

            if saldo_excedeu:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif limite_excedeu:
                print('Operação falhou! O valor do saque excede o limite!')

            elif saque_excedeu:
                print("Você já usou todos os seus saques disponíveis!")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Operação realizada com sucesso!")
            else:
                print("Operação falhou! Valor inválido.")

        elif opcao == "e":
            print('===================== EXTRATO ========================')
            print("Não foram realizadas movimentações" if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("======================================================")

        elif opcao == "q":
            print("Você saiu do seu banco!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada :)")

# Criação da interface de login com Tkinter
janela_login = tk.Tk()
janela_login.title("Sistema Bancário - Login")

tk.Label(janela_login, text="CPF:").grid(row=0, column=0, padx=10, pady=10)
entry_cpf = tk.Entry(janela_login)
entry_cpf.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela_login, text="Senha:").grid(row=1, column=0, padx=10, pady=10)
entry_senha = tk.Entry(janela_login, show="*")
entry_senha.grid(row=1, column=1, padx=10, pady=10)

botao_login = tk.Button(janela_login, text="Login", command=autenticar)
botao_login.grid(row=2, column=0, columnspan=2, pady=10)

janela_login.mainloop()
