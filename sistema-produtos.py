produtos = [] #lista onde guardo os produtos
maior_valor = 0
identificacao = 1

def mostrar_informacao(produto): #mostra informaçoes
    print(f"\nInformações do produto - {produto['nome']} :")
    print(f"Nome: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']}")
    print(f"Quantidade: {produto['quantidade']}")
    print(f"Identificação do Produto : {produto['id']}")
    print(f"Valor total de estoque: R$ {produto['valor_estoque']}")

def pedir_numero(): #pede numero
    while True: #testando erros
        try:
            preco = float(input("Digite o preço do produto : "))
            return preco
        except ValueError:
            print("Digite apenas valores numéricos aqui!\n")

def pedir_quantidade(): #pede quantidade
    while True: #testando erros
        try:
            quantidade = int(input("Digite a quantidade do produto : "))
            return quantidade
        except ValueError:
            print("Digite apenas valores numéricos aqui!\n")

def recalcular_maior_valor():
    maior_valor = 0
    for produto in produtos:
        if produto['valor_estoque'] > maior_valor:
            maior_valor = produto['valor_estoque']
            nome_produto = produto['nome']
    return maior_valor, nome_produto

def listar_produtos(): #listar produtos
    for produto in produtos:
        print(f"\n---- Produto {produto['id']} ----")
        mostrar_informacao(produto)
    print(f"\n-- Produto : {nome_produto} --")
    print(f"-- Produto possui maior valor total em estoque : {maior_valor} --\n")
    
def buscar_produto():
    while True:
        if len(produtos) == 0: # Aqui eu vejo se a lista esta vazia.
            print(f"Não há produtos para listar.")

        buscar_produto = input("\nDeseja buscar o produto por (Nome) ou (Id)? : ").strip().title()
        if buscar_produto == "Nome":
            break
        elif buscar_produto == "Id":
            break
        else:
            print("Digite uma informação válida, tente outra vez.")

    if buscar_produto == "Nome": #por nome
        buscar_produto_nome = input("Digite o nome do produto : ").strip().title()
        encontrado = False
        for produto in produtos:
            if produto['nome'] == buscar_produto_nome:
                print("\n---- Produto Buscado com Sucesso ----")
                encontrado = True
                mostrar_informacao(produto)
                break
        if not encontrado:
            print("Verifique se digitou errado. Produto não encontrado no sistema!")

    if buscar_produto == "Id":
        while True:
            try:
                buscar_produto_id = int(input("Digite o Id do produto :"))
                break
            except ValueError:
                print("Digite apenas números.")
        encontrado = False
        for produto in produtos:
            if produto['id'] == buscar_produto_id:
                print("\n---- Produto Buscado com Sucesso ----")
                encontrado = True
                mostrar_informacao()
                break
        if not encontrado:
            print("Verifique se digitou errado. Produto não encontrado no sistema!")

while True: #programa

    print("\n1 - Cadastrar Produto")
    print("2 - Listar Produto")
    print("3 - Buscar Produto")
    print("4 - Remover Produto")
    print("5 - Editar Produto")
    print("6 - Sair\n")

    while True: #Testando erros
        try:
            opcao = int(input("Quais das opções acima você deseja? : "))
            if opcao >= 1 and opcao <= 6:
                break
            elif opcao <= 0 or opcao >= 7:
                print("Digite uma informação válida, tente outra vez.\n")
        except ValueError:
            print("Digite apenas números aqui!\n")

    #opçoes
    if opcao == 1: #cadastro

        nome = input("\nDigite o nome do produto : ").strip().title()

        preco = pedir_numero()
        quantidade = pedir_quantidade()

        produto = { #dicionario
            'nome' : nome,
            'preco' : preco,
            'quantidade' : quantidade,
            'id' : identificacao
        }

        valor_estoque_produto = produto['preco'] * produto['quantidade'] #calculo estoque
        produto['valor_estoque'] = valor_estoque_produto #criando espaço dentro do dict

        if valor_estoque_produto > maior_valor: # esquema para ver maior estoque
            maior_valor = valor_estoque_produto 
            nome_produto = produto["nome"]

        produtos.append(produto) #guarda as informaçoes do dict dentro da lista

        identificacao += 1 #contador do id
    
    elif opcao == 2: #listagem
        listar_produtos()
        
    elif opcao == 3: #buscagem
        buscar_produto() 

    elif opcao == 4: #remocao
        while True:
            remover = input("\nDeseja remover o produto por (Nome) ou (Id)? : ").strip().title()
            if remover == "Nome":
                break
            elif remover == "Id":
                break
            else:
                print("Verifique se digitou errado. Produto não encontrado no sistema!")

        if remover == "Nome": #por nome
            remover_produto_nome = input("Digite o nome do produto : ").strip().title()
            encontrado = False
            for produto in produtos:
                if produto['nome'] == remover_produto_nome:
                    encontrado = True
                    produtos.remove(produto)
                    print("Pronto.")
                    if nome_produto == remover_produto_nome:
                        nome_produto = "Produto Removido, Recalculando sistema..."
                        maior_valor, nome_produto = recalcular_maior_valor()
                    break
            if not encontrado:
                print("Verifique se digitou errado. Produto não encontrado no sistema!")
            
        elif remover == "Id": #por id
            while True:
                try:
                    remover_produto_id = int(input("Digite o Id do produto : "))
                    break
                except ValueError:
                    print("Digite apenas números aqui!")
            encontrado = False
            for produto in produtos: 
                if produto['id'] == remover_produto_id:
                    encontrado = True
                    produtos.remove(produto)
                    print("Pronto.")
                    if produto['nome'] == nome_produto:
                        nome_produto = "Produto Removido, Recalculando sistema..." 
                        maior_valor, nome_produto = recalcular_maior_valor()
                    break
            if not encontrado:
                print("Verifique se digitou errado. Produto não encontrado no sistema!")
    # < Aqui ainda nao testei
    elif opcao == 5: #O que era pra funcionar já funciona, agora tenho que procurar erros
        while True: #Aqui eu faço um loop infinito até der certo
            try:
                editar = int(input("\nDigite o ID do Produto: "))
                break
            except ValueError:
                print("Digite Apenas números aqui!")

        # if Id nao estar na lista de dicionario : mandar uma frase
        encontrado = False
        for produto in produtos: #Aqui eu digitei um NUMERO porem o codigo continua
            if produto['id'] == editar:
                encontrado = True
                mostrar_informacao(produto)
                break
        if not encontrado:
            print("Verifique se digitou errado. Produto não encontrado no sistema!\n")
        else: # Daqui pra baixo devo procurar erro e testar e refazer os erros!!!
            print("\n1 - Editar Nome")
            print("2 - Editar Preço")
            print("3 - Editar Quantidade")

            editar_informacao = int(input("Deseja editar o que? : "))

            if editar_informacao == 1: #Tenho que procurar os erros
                for produto in produtos:
                    if produto['id'] == editar:
                        novo_nome = input("Digite o novo nome do produto : ").strip().title()
                        produto['nome'] = novo_nome
                        print("---- Produto Editado ----")
                        break

            elif editar_informacao == 2: #Tenho que procurar os erros
                for produto in produtos:
                    if produto['id'] == editar:
                        while True:
                            try:
                                novo_preco = float(input("Digite o novo preço : "))
                                break
                            except ValueError:
                                print("Digite apenas números aqui!")
                        produto['preco'] = novo_preco
                        print("---- Produto Editado ----")
                        break

            elif editar_informacao == 3: #Tenho que procurar os erros
                for produto in produtos:
                    if produto['id'] == editar:
                        while True:
                            try:
                                nova_quantidade = int(input("Digite a nova quantidade : "))
                                break
                            except ValueError:
                                print("Digite apenas números aqui!")
                        produto['quantidade'] = nova_quantidade
            else:
                print("Verifique se digitou algo errado. Produto não encontrado no sistema.\n")
                    
            valor_estoque_produto = produto['preco'] * produto['quantidade'] #Recalculando
            produto['valor_estoque'] = valor_estoque_produto #Recalculando
            
    elif opcao == 6: #saida do programa
        print("Obrigado!")
        break

    elif opcao > 6:
        print("Digite uma opção válida.")