# Crie um programa que receba uma lista com o nome de 5 produtos e outra lista com as quantidades em estoque de cada um desses produtos. O programa deve exibir os produtos que estão com o estoque zerado.

# Exemplo de entrada:
# Produtos: ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
# Estoque: [10, 0, 5, 0, 20]

# Exemplo de saída:
# Produtos com estoque zerado: Feijão, Açúcar
def verificar_estoque():
    # Lista de produtos
    produtos = ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
    # Lista de quantidades em estoque
    estoque = [10, 0, 5, 0, 20]
    
    # Lista para armazenar produtos com estoque zerado
    produtos_zerados = []

    # Verificando quais produtos estão com estoque zerado
    for i in range(len(produtos)):
        if estoque[i] == 0:
            produtos_zerados.append(produtos[i])

    # Exibindo os produtos com estoque zerado
    if produtos_zerados:
        print("Produtos com estoque zerado:", ', '.join(produtos_zerados))
    else:
        print("Todos os produtos têm estoque disponível.")

verificar_estoque()
