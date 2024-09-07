# Sistema Bancário com Autenticação

Este projeto é um sistema bancário simples criado em Python que permite ao usuário realizar operações bancárias básicas, como depósito, saque e visualização de extrato. O sistema utiliza a biblioteca Tkinter para fornecer uma interface gráfica de usuário (GUI) para autenticação por CPF e senha.

## Funcionalidades

- **Login com CPF e Senha**: O usuário deve se autenticar com um CPF e uma senha antes de acessar o menu bancário.
- **Depósito**: Permite ao usuário depositar um valor positivo em sua conta.
- **Saque**: Permite ao usuário sacar um valor de sua conta, desde que tenha saldo suficiente, o valor não exceda o limite permitido e o número máximo de saques diários não tenha sido atingido.
- **Extrato**: Exibe todas as operações realizadas (depósitos e saques) e o saldo atual.
- **Sair**: Encerra a sessão do usuário.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal usada para o desenvolvimento do sistema.
- **Tkinter**: Biblioteca padrão do Python para interfaces gráficas de usuário (GUI).

## Instalação e Execução

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario.git
   cd sistema-bancario
