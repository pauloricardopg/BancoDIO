def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        return("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        return("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        return("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return(saldo, extrato, numero_saques)

    else:
        return("Operação falhou! O valor informado é inválido.")

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return(saldo, extrato)

    else:
        return("Operação falhou! O valor informado é inválido.")
    
def mostrar_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
def criar_usuario():
    nome = input("Informe seu nome: ")
    dianascimento = int(input("Infome o dia do seu nascimento: "))
    
    while dianascimento < 1 or dianascimento > 31:
        dianascimento = int(input("Infome o dia do seu nascimento: "))
    mesnascimento = int(input("Infome o mês do seu nascimento: "))
    
    while mesnascimento < 1 or mesnascimento > 12:
        mesnascimento = int(input("Infome o mês do seu nascimento: "))
    anonascimento = int(input("Informe o ano do seu nascimento: "))
    
    while anonascimento <1900  or anonascimento > 2025:
        anonascimento = int(input("Infome o ano do seu nascimento: "))
    dtnascimento = str(dianascimento) +"/"+  str(mesnascimento) +"/"+ str(anonascimento)
    cpf = ""
    
    while len(cpf) != 11 or not cpf.isdigit():
        cpf = input("Informe seu CPF (apenas números): ").strip()
        if len(cpf) != 11 or not cpf.isdigit():
            print("CPF inválido! Digite exatamente 11 números.")
    logradouro = input("Informe o seu logradouro: ")
    numero = input("Informe o numero da sua casa: ")
    bairro = input("Informe o seu bairro: ")
    cidade = input("Informe a sua cidade: ")
    estado = input("Informe a sigla do seu estado: ")
    endereco = logradouro + ", " + numero + " - " + bairro + " - " + cidade +"/"+ estado  
    
    usuario = {
        "nome": nome,
        "dtnascimento": dtnascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    return usuario

def criar_conta_corrente(nconta, usuario):
    agencia = ""
    if nconta >= 0:
        nconta += 1
    agencia = ("0001")
    
    conta = {
        "numeroConta": nconta,
        "agencia": agencia,
        "usuario": usuario
    }

    return conta


def buscar_usuario_por_cpf(cpf, lista_usuarios):
    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def adicionar_usuario(lista_usuarios):
    usuario = criar_usuario()
    
    if buscar_usuario_por_cpf(usuario["cpf"], lista_usuarios):
        print("Erro: Usuário com este CPF já cadastrado.")
    else:
        lista_usuarios.append(usuario)
        print("Usuário criado com sucesso!")

def adicionar_conta(nconta_atual, lista_usuarios, lista_contas):
    cpf_usuario=""
    while len(cpf_usuario) != 11 or not cpf_usuario.isdigit():
        cpf_usuario = input("Informe seu CPF (apenas números): ").strip()
        if len(cpf_usuario) != 11 or not cpf_usuario.isdigit():
            print("CPF inválido! Digite exatamente 11 números.")
            
    usuario_encontrado = buscar_usuario_por_cpf(cpf_usuario, lista_usuarios)
    
    if usuario_encontrado:
        conta = criar_conta_corrente(nconta_atual, usuario_encontrado)
        lista_contas.append(conta)
        
        print("\nConta criada com sucesso!")
        print(f"  Agência: \t{conta['agencia']}")
        print(f"  Conta: \t{conta['numeroConta']}")
        print(f"  Usuário: \t{conta['usuario']['nome']}")

        return nconta_atual + 1
    else:
        print("CPF do usuario não encontrado")
        return nconta_atual


def listar_usuarios(lista_usuarios):
    print("\n================ USUÁRIOS ================")
    if not lista_usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for i, usuario in enumerate(lista_usuarios):
            print(f"  --- Usuário {i+1} ---")
            print(f"    Nome: \t{usuario['nome']}")
            print(f"    CPF: \t{usuario['cpf']}")
            print(f"    Endereço: \t{usuario['endereco']}")
    print("==========================================")
    
def listar_contas(lista_contas):
    print("\n================= CONTAS =================")
    if not lista_contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in lista_contas:
            print(f"  --- Conta Nº {conta['numeroConta']} ---")
            print(f"    Agência: \t{conta['agencia']}")
            print(f"    Titular: \t{conta['usuario']['nome']}")
            print(f"    CPF: \t{conta['usuario']['cpf']}")
    print("==========================================")


menu = """

[u] Criar Usuario
[c] Criar Conta
[lu] Listar Usuários
[lc] Listar Contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor = 0
nconta = 0
listaContas = []
listaUsuarios = []

while True:

    opcao = input(menu)

    if opcao == "d":
        while True:
            valor_digitado = input("Informe o valor do depósito: ")
            try:
                valor = float(valor_digitado)
                break
            except ValueError:
                print(f"\nErro: '{valor_digitado}' não é um número válido. Por favor, tente novamente.\n")
        
        retorno_deposito = deposito(saldo, valor, extrato)
        if isinstance(retorno_deposito, tuple):
            saldo, extrato = retorno_deposito
            print("Depósito realizado com sucesso!")
        else:
            print(retorno_deposito)

    elif opcao == "s":
        while True:
            valor_digitado = input("Informe o valor do saque: ")
            try:
                valor = float(valor_digitado)
                break
            except ValueError:
                print(f"\nErro: '{valor_digitado}' não é um número válido. Por favor, tente novamente.\n")
        

        retorno_saque = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        if not isinstance(retorno_saque, tuple):
            print(retorno_saque)
        else:
            saldo, extrato, numero_saques = retorno_saque
            print("Saque realizado com sucesso!")

    elif opcao == "e":
        mostrar_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        adicionar_usuario(listaUsuarios)
    
    elif opcao == "c":
        nconta = adicionar_conta(nconta, listaUsuarios, listaContas)

    elif opcao == "lu":
        listar_usuarios(listaUsuarios)
        
    elif opcao == "lc":
        listar_contas(listaContas)

    elif opcao == "q":
        break

    else:

        print("Operação inválida, por favor selecione novamente a operação desejada.")
