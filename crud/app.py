import _sqlite3

produtos = _sqlite3.connect("produtos.db")
cursor = produtos.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,nome TEXT NOT NULL, preco REAL NOT NULL, estoque INTEGER NOT NULL)")

def menu():
    print("1 - Inserir um novo produto")
    print("2 - Deletar um produto")
    print("3 - Atualizar um produto")
    print("4 - Listar todos os produtos")
    print("5 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    return opcao

def inserir():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))

    cursor.execute("INSERT INTO produtos(nome, preco, estoque) VALUES(?,?,?)" , (nome, preco, estoque))
    produtos.commit()

def deletar():
    id = int(input("Digite o id do produto que deseja deletar: "))
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
    produtos.commit()

def atualizar():
    id = int(input("Digite o id do produto que deseja atualizar: "))
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))
    cursor.execute("UPDATE produtos SET nome = ?, preco = ?, estoque = ? WHERE id = ?", (nome, preco, estoque, id))
    produtos.commit()

def listar():
    cursor.execute("SELECT * FROM produtos")
    for linha in cursor.fetchall():
        print(linha)

while True:
    opcao = menu()
    if opcao == 1:
        inserir()
    elif opcao == 2:
        deletar()
    elif opcao == 3:
        atualizar()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        break
    else:
        print("Opção inválida!")

produtos.close()
