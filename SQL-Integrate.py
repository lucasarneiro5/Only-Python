import pyodbc

dados_conexao = (
    """Informações para conectar no Banco de Dados Desejado do SQL Server"""
    "Driver = {SQL Server};" # Referncia qual software de BD para conexao
    "Server = BR-E0287QR;" # Pega o seu hostname no cmd
    "Database = Hastag;" # Nome do seu BD criado
)

connect = pyodbc.connect(dados_conexao)
print('Successful Connection! \n')

cursor = connect.cursor() # Executa os comandos dentro do BD

comando = """INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
	(1, 'Lucas', 'PC', '15/02/2021', 8000, 1)""" #Pode executar qualquer comando SQL

cursor.execute(comando)