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

def cadastrar_produto(produto):
    #Esta função tem o objetivo de cadastrar o (produto == dict ) e guardar dentro da (lista == lista_produtos)

    print(f"\n---Cadastrando Produto {id_produtos}---")
    nome_produto = input("Digite o nome do produto : ").strip().title()

    if nome_produto == "":
        print("Informação invalida.")
        return
    
    try: 
        valor_produto = float(input("Digite o valor do produto : "))
    except ValueError:
        print("Digite apenas números. Produto não foi cadastrado!\n")
        return

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

    #Aqui cria o valor de estoque
    produto['valor_estoque'] = valor_produto * quantidade_produto
    
    lista_produtos.append(produto)

    return produto, nome_produto
    
def listar_produtos(produto):
    #Esta função tem o objetivo de dar print das informações do produto

    if not lista_produtos:
        print("Não há produtos para listar.")
        return
    
    print("\n---Tabela de Produtos---")
    for produto in lista_produtos:
        mostrar_informacoes_produto(produto)

def buscar_produto(produto):
    #Esta função tem o objetivo de fazer a busca do produto, sendo por nome ou id.

    if not lista_produtos:
        print("Não há produtos para buscar.")
        return
    
    print("\n---Buscando Produto---")
    buscar_id_nome = input("Deseja buscar o produto na tabela por (nome) ou (id) : ").strip().title()
    encontrado = False

    if buscar_id_nome == "Nome":
        buscar_nome_produto = input("Digite o nome do produto : ").strip().title()
        encontrado = False

        #Percorrendo lista_produtos para achar produto
        encontrado = buscar_produto_por_nome(produto, encontrado, buscar_nome_produto)

        if not encontrado:
            print("Produto não encontrado.")
            return
        
        return(buscar_nome_produto)
    
    elif buscar_id_nome == "Id":
        try:
            buscar_id_produto = int(input("Digite o ID do produto : "))
        except ValueError:
            print("Digite apenas números. Produto não encontrado")
            return
            
        encontrado = False

        #Percorrendo lista_produtos para achar ID
        encontrado = buscar_produto_por_id(produto, encontrado, buscar_id_produto)

        if not encontrado:
            print("Produto não encontrado.")
            return
        return buscar_id_produto
    
    else:
        print("Informação incorreta. Produto não encontrado.")
    


def buscar_produto_por_nome(produto, encontrado, buscar_nome_produto):
    #Faz parte da Opção 3 do menu : Buscar Produto por (Nome)

    for produto in lista_produtos:
        if produto['nome'] == buscar_nome_produto:
            print("\n--Produto Encontrado--")
            mostrar_informacoes_produto(produto)
            encontrado = True
            break
    return encontrado
        
def buscar_produto_por_id(produto, encontrado, buscar_id_produto):
    #Faz parte da Opção 3 do menu : Buscar Produto por (Id)

    for produto in lista_produtos:
        if produto['id'] == buscar_id_produto:
            print("\n--Produto Encontrado--")
            mostrar_informacoes_produto(produto)
            encontrado = True
            break
    return encontrado
    
def editar_produto(produto):
    #Esta função tem objetivo de editar as informações do produto

    if not lista_produtos:
        print("Não há produtos para editar.")
        return
    
    try:
        inserir_id_produto = int(input("\nDigite o ID do produto que deseja editar : "))
    except ValueError:
        print("Digite apenas números.")
        return
    
    encontrado = False

    for produto in lista_produtos:
        if produto['id'] == inserir_id_produto:
            print("\n---INFORMAÇÃO DO PRODUTO---")
            mostrar_informacoes_produto(produto)
            encontrado = True
            break
    
    if not encontrado:
        print(("Informação incorreta. Produto não encontrado."))
        return
    continuacao_editar_produto()
    return inserir_id_produto
    
def continuacao_editar_produto():
    #Continuação do editar_produto() feita para separar em duas partes

    print("---Editando Informações do Produto---")
    print("1 - Editar Nome")
    print("2 - Editar Valor")
    print("3 - Editar Quantidade")

    try:
        editar = int(input("\nDeseja editar qual informação : "))
    except ValueError:
        print("Digite apenas números.")
        return
        
    if editar > 3 or editar < 1:
        print("Este número não está inserido no menu de opções.")
        
    if editar == 1:
        editar_produto_nome(produto)
    elif editar == 2:
        editar_produto_valor(produto)
    elif editar == 3:
        editar_produto_quantidade(produto)
    else:
        print("Informação incorreta. Produto não encontrado.")
        
    def editar_produto_nome(produto):
        #Editar o nome
            
        editar_nome = input("Digite o novo nome do produto : ").strip().title()
        if editar_nome == "":
            print("Informação invalida.")
            return
            
        encontrado = False
        for produto in lista_produtos:
            if produto['id'] == inserir_id_produto:
                produto['nome'] = editar_nome
                encontrado = True
                print("--Produto Editado com Sucesso--")
                break
                
        if not encontrado:
            print("Informação incorreta. Produto não encontrado.")
            return

def editar_produto_valor(produto):
    #Editar o valor

    try:
        editar_valor = float(input("Digite o novo valor do produto : "))
    except ValueError:
        print("Digite apenas números.")
        return

    encontrado = False

    for produto in lista_produtos:
        if produto['id'] == inserir_id_produto:
            valor_produto = editar_valor
            produto['valor'] = valor_produto
            recalcular_estoque(x= produto['valor'], y= produto['quantidade']) #Possivel erro
            encontrado = True
            print("--Produto Editado com sucesso--")
            break

    if not encontrado:
        print("Informação incorreta. Produto não encontrado.")
        return
                
def editar_produto_quantidade(produto):
    #Editar a quantidade

    try:
        editar_quantidade = int(input("Digite a nova quantidade de produtos : "))
    except ValueError:
        print("Digite apenas números.")
        return

    encontrado = False

    for produto in lista_produtos:
        if produto['id'] == inserir_id_produto:
            quantidade_produto = editar_quantidade
            produto['quantidade'] = quantidade_produto #ERRO
            recalcular_estoque(x= produto['quantidade'], y= produto['valor'])
            encontrado = True
            print("--Produto Editado com sucesso--")
            break

    if not encontrado:
        print("Informação incorreta. Produto não encontrado.")
        return

def remover_produto(produto):
    #Esta função tem objetivo de remover os produtos da lista
    if not lista_produtos:
        print("Não há produtos na lista para remover.")
        return

    try:
        remover = int(input("\nDigite o ID do produto que deseja remover : "))
    except ValueError:
        print("Digite apenas números.")
        return

    encontrado = False

    #Percorrendo lista para verificar se o produto está na lista e remove-lo
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
        return

def sair_do_menu(): 
    #Esta função finaliza o programa

    print("Obrigado.")

def mostrar_informacoes_produto(produto):
    #Esta função mostra informações do produto, reutilizo em varias partes do código.

    print(f"-Produto nº {produto['id']}-")
    print(f"Nome do produto : {produto['nome']}")
    print(f"Valor do produto : {produto['valor']}")
    print(f"Quantidade do produto : {produto['quantidade']}")
    print(f"Valor de estoque : {produto['valor_estoque']}")
    print(f"ID do produto : {produto['id']}\n")
    
def recalcular_estoque(x, y):
    #Função feita para recalcular o estoque do produto

    for produto in lista_produtos:
        if produto['id'] == inserir_id_produto:
            produto['valor_estoque'] = x * y
            return produto['valor_estoque']

while True:
    mostrar_menu_opcoes()

    while True:
        try:
            escolha_menu_opcoes = int(input("Digite uma opção : ")) 
            break
        except ValueError:
            print("Opção invalida. Digite apenas números.\n") 

    if escolha_menu_opcoes < 1 or escolha_menu_opcoes > 6: 
        print("Este número não está inserido no menu de opções.")
        continue
    
    if escolha_menu_opcoes == 1:
        #Opção 1 do menu : Cadastrar Produto

        resultado_cadastro = cadastrar_produto(produto)

        if not resultado_cadastro:
            continue

        id_produtos = contador_id + 1
        contador_id = contador_id + 1
   
    elif escolha_menu_opcoes == 2:
        #Opção 2 do menu : Listar Produto

        listar_produtos(produto)
    
    elif escolha_menu_opcoes == 3:
        #Opção 3 do menu : Buscar Produto

        buscar_produto(produto)
        
    elif escolha_menu_opcoes == 4:
        #Opção 4 do menu : Editar Produto

        inserir_id_produto = editar_produto(produto)
        
    elif escolha_menu_opcoes == 5:
        #Opção 5 do menu : Remover Produto

        remover_produto(produto)

    elif escolha_menu_opcoes == 6:
        #Opção 6 do menu : Sair

        sair_do_menu()
        break