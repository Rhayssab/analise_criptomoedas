import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("historico_cripto.csv", header=None)

# Nomear as colunas
df.columns = ["Moeda", "Preço", "Data"]

# Filtrar apenas o Bitcoin
df_bitcoin = df[df["Moeda"] == "bitcoin"]

# Configurar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(df_bitcoin["Data"], df_bitcoin["Preço"], marker='o')

# Adicionar títulos e exibir
plt.title("Evolução do Preço do Bitcoin")
plt.xlabel("Data da Consulta")
plt.ylabel("Preço em BRL")
plt.xticks(rotation=45)  # Dois espaços antes do comentário corrigem o E261
plt.show()

# Esta linha em branco abaixo é necessária para corrigir o W292

plt.title("Evolução do Preço do Bitcoin")
plt.xlabel("Data da Consulta")
plt.ylabel("Preço")
plt.grid(True)


plt.savefig("grafico_bitcoin.png")
plt.show()
