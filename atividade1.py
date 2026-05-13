import pandas as pd

# 1. Criação do dicionário com os dados das frutas
dados_frutas = {
    "Fruta": ["Maçã", "Banana", "Morango", "Uva", "Abacaxi"],
    "Quantidade": [12, 24, 10, 15, 8],
    "Preco": [4.50, 2.99, 7.50, 6.00, 5.20],
}

# 2. Conversão do dicionário em um DataFrame do Pandas
df_frutas = pd.DataFrame(dados_frutas)

# 3. Exibição do DataFrame na tela
print("--- DataFrame Manual de Frutas ---")
print(df_frutas)
