# Lista de produtos onde irei guardar os (dicionarios : produtos)
lista_produtos = []

# Dicionario produto
produto = {}

# Contadores para usar nos ID´s dos produtos
id_produtos = 1 
contador_id = 1

def mostrar_menu_opcoes():
    print("\n=== Sistema Cadastro de Produtos ===")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produto")
    print("3 - Buscar Produto")
    print("4 - Editar Produto")
    print("5 - Remover Produto")
    print("6 - Sair\n")

# Opção 1 do menu : Cadastrar Produto
def cadastrar_produto(produto):

    nome_produto = input("Digite o nome do produto : ").strip().title()

    if nome_produto == "":
        print("Informação invalida.")
        return
    
    # Testando ValueError para a variavel valor do produto
    try: 
        valor_produto = float(input("Digite o valor do produto : "))
    except ValueError:
        print("Digite apenas números. Produto não foi cadastrado!\n")
        return

    # Testando ValueError para a variavel quantidade do produto
    try:
        quantidade_produto = int(input("Digite a quantidade do produto : "))
    except ValueError:
        print("Digite apenas números. Produto não foi cadastrado!\n")
        return

    produto = {
        "nome" : nome_produto,
        "valor" : valor_produto,
        "quantidade" : quantidade_produto,
        "id" : id_produtos
    }

    # Aqui cria o valor de estoque
    produto['valor_estoque'] = valor_produto * quantidade_produto
    
    lista_produtos.append(produto)

    return produto, nome_produto
    
# Opção 2 do menu : Listar Produto
def listar_produtos(produto):
    print("\n---Tabela de Produtos---")
    for produto in lista_produtos:
        mostrar_informacoes_produto(produto)

# faz parte da Opção 3 do menu : Buscar Produto por (Nome)  
def buscar_nome_produto1(produto, encontrado):
    for produto in lista_produtos:
        if produto['nome'] == buscar_nome_produto:
            print("\n--Produto Encontrado--")
            mostrar_informacoes_produto(produto)
            encontrado = True
    return encontrado

# Faz parte da Opção 3 do menu : Buscar Produto por (Id)
def buscar_id_produto2(produto, encontrado):
    for produto in lista_produtos:
        if produto['id'] == buscar_id_produto:
            print("\n--Produto Encontrado--")
            mostrar_informacoes_produto(produto)
            encontrado = True
    return encontrado

# Opção 6 do menu : sair
def sair_do_menu(): 
    print("Obrigado.")

# Função que mostra informações do produto
def mostrar_informacoes_produto(produto):
    print(f"-Produto nº {produto['id']}-")
    print(f"Nome do produto : {produto['nome']}")
    print(f"Valor do produto : {produto['valor']}")
    print(f"Quantidade do produto : {produto['quantidade']}")
    print(f"Valor de estoque : {produto['valor_estoque']}")
    print(f"ID do produto : {produto['id']}\n")
    
def recalcular_estoque(x, y):
    for produto in lista_produtos:
        if produto['id'] == inserir_id_produto:
            produto['valor_estoque'] = x * y
            return produto['valor_estoque']

while True:
    mostrar_menu_opcoes()

    # Try except ValueError escolha de opções do menu
    while True:
        try:
            escolha_menu_opcoes = int(input("Digite uma opção : ")) 
            break
        except ValueError:
            print("Opção invalida. Digite apenas números.\n") 

    # Testando se o numero está no menu
    if escolha_menu_opcoes < 1 or escolha_menu_opcoes > 6: 
        print("Este número não está inserido no menu de opções.")
        continue
    
    # Opção 1 do menu : Cadastrar Produto
    if escolha_menu_opcoes == 1:

        print(f"\n---Cadastrando Produto {id_produtos}---")
        resultado_cadastro = cadastrar_produto(produto)

        if not resultado_cadastro:
            continue

        # Contador de id do produto para sempre ter um número fixo
        id_produtos = contador_id + 1

        # Um loop de contagem para o contador sempre estar aumentando
        contador_id = contador_id + 1
   

    # Opção 2 do menu : Listar Produto
    elif escolha_menu_opcoes == 2:
        if not lista_produtos:
            print("Não há produtos para listar.")
            continue
        
        listar_produtos(produto)
    
    # Opção 3 do menu : Buscar Produto
    elif escolha_menu_opcoes == 3:

        # Verificando se a lista está vazia
        if not lista_produtos:
            print("Não há produtos para buscar.")
            continue
        
        # Vendo se o usuario pretende fazer busca por ID ou Nome
        print("\n---Buscando Produto---")
        buscar_id_nome = input("Deseja buscar o produto na tabela por (nome) ou (id) : ").strip().title()
        encontrado = False

        # Fazendo busca por Nome
        if buscar_id_nome == "Nome":
            buscar_nome_produto = input("Digite o nome do produto : ").strip().title()

            #Percorrendo lista_produtos para achar produto
            encontrado = buscar_nome_produto1(produto, encontrado)
         
            if not encontrado:
                print("Produto não encontrado.")
                continue
        
        #Fazendo busca por ID
        elif buscar_id_nome == "Id":

            #Testando ValueError para buscar_id_produto
            try:
                buscar_id_produto = int(input("Digite o ID do produto : "))
            except ValueError:
                print("Digite apenas números. Produto não encontrado")
                continue
            
            encontrado = False

            #Percorrendo lista_produtos para achar ID
            encontrado = buscar_id_produto2(produto, encontrado)

            if not encontrado:
                print("Produto não encontrado.")
                continue
        
        else:
            print("Informação incorreta. Produto não encontrado.")

    # Opção 4 do menu : Editar Informações do Produto
    elif escolha_menu_opcoes == 4:

        if not lista_produtos:
            print("Não há produtos para editar.")
            continue

        # Variavel feita para indicar qual produto será editado
        try:
            inserir_id_produto = int(input("\nDigite o ID do produto que deseja editar : "))
        except ValueError:
            print("Digite apenas números.")
            continue

        encontrado = False

        for produto in lista_produtos:
            if produto['id'] == inserir_id_produto:
                print("\n---INFORMAÇÃO DO PRODUTO---")
                mostrar_informacoes_produto(produto)
                encontrado = True
                break
        
        if not encontrado:
            print(("Informação incorreta. Produto não encontrado."))
            continue

        print("---Editando Informações do Produto---")
        print("1 - Editar Nome")
        print("2 - Editar Valor")
        print("3 - Editar Quantidade")

        # Testando ValueError na variavel editar
        try:
            editar = int(input("\nDeseja editar qual informação : "))
        except ValueError:
            print("Digite apenas números.")
            continue
        
        # Aqui faz todo o processo para editar o nome do produto
        if editar == 1:
            editar_nome = input("Digite o novo nome do produto : ").strip().title()
            if editar_nome == "":
                print("Informação invalida.")
                continue
            
            encontrado = False

            for produto in lista_produtos:
                if produto['id'] == inserir_id_produto:
                    produto['nome'] = editar_nome
                    encontrado = True
                    print("--Produto Editado com Sucesso--")
                    break

            if not encontrado:
                print("Informação incorreta. Produto não encontrado.")
                continue

        # Aqui faz todo o processo para editar o valor do produto
        elif editar == 2:

            # Testando ValueError na variavel editar_valor
            try:
                editar_valor = float(input("Digite o novo valor do produto : "))
            except ValueError:
                print("Digite apenas números.")
                continue

            encontrado = False

            # Percorrendo lista para encontrar o produto por ID e fazer a alteração do valor
            for produto in lista_produtos:
                if produto['id'] == inserir_id_produto:
                    valor_produto = editar_valor
                    produto['valor'] = valor_produto
                    calculo = recalcular_estoque(x= produto['valor'], y= produto['quantidade'])
                    encontrado = True
                    print("--Produto Editado com sucesso--")
                    break

            if not encontrado:
                print("Informação incorreta. Produto não encontrado.")
                continue

        # Aqui faz todo o processo para editar a quantidade do produto
        elif editar == 3:

            # Testando ValueError na variavel editar_quantidade
            try:
                editar_quantidade = int(input("Digite a nova quantidade de produtos : "))
            except ValueError:
                print("Digite apenas números.")
                continue

            encontrado = False

            # Percorrendo lista para encontrar o produto por ID e fazer a alteração da quantidade
            for produto in lista_produtos:
                if produto['id'] == inserir_id_produto:
                    quantidade_produto = editar_quantidade
                    produto['quantidade'] = quantidade_produto #ERRO
                    calculo = recalcular_estoque(x= produto['quantidade'], y= produto['valor'])
                    encontrado = True
                    print("--Produto Editado com sucesso--")
                    break

            if not encontrado:
                print("Informação incorreta. Produto não encontrado.")
                continue

        else:
            print("Informação incorreta. Produto não encontrado.")

    # Opção 5 do menu : Remover Produtos
    elif escolha_menu_opcoes == 5:

        if not lista_produtos:
            print("Não há produtos na lista para remover.")
            continue

        # Testando ValueError da variavel remover
        try:
            remover = int(input("\nDigite o ID do produto que deseja remover : "))
        except ValueError:
            print("Digite apenas números.")
            continue

        encontrado = False

        # Percorrendo lista para verificar se o produto está na lista e remove-lo
        for produto in lista_produtos:
            if produto['id'] == remover:
                print("\n--INFORMAÇÃO DO PRODUTO--")
                mostrar_informacoes_produto(produto)
                verificacao_remover_produto = input("Tem certeza que deseja remover o produto? (S) para sim ou (N) para não : ").strip().title()

                if verificacao_remover_produto == "S":
                    lista_produtos.remove(produto)
                    encontrado = True
                    print("--Produto Removido com sucesso--")
                    break

                elif verificacao_remover_produto == "N":
                    encontrado = True
                    print("Ok, produto não foi removido.")
                    continue

                elif verificacao_remover_produto != "S" or verificacao_remover_produto != "N":
                    encontrado = True
                    print("Informação incorreta! Escolha (S) para sim ou (N) para não.")
                    continue
        
        if not encontrado:
            print("Informação incorreta. Produto não encontrado.")
            continue

    # Opção 6 do menu : Sair
    elif escolha_menu_opcoes == 6: #Opção 6 do menu : sair
        sair_do_menu()
        break