import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
df = pd.read_csv("historico_cripto.csv", header=None)

# Nomear as colunas
df.columns = ["Moeda", "Preço", "Data"]

# Filtrar apenas os registros do Bitcoin
df_bitcoin = df[df["Moeda"] == "bitcoin"]

# Converter a coluna Data para formato de data/hora
df_bitcoin["Data"] = pd.to_datetime(df_bitcoin["Data"])

# Criar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(df_bitcoin["Data"], df_bitcoin["Preço"], marker="o", linewidth=2)

# Personalização do gráfico
plt.title("Evolução do Preço do Bitcoin")
plt.xlabel("Data da Consulta")
plt.ylabel("Preço em BRL")
plt.xticks(rotation=45)
plt.grid(True)

# Ajustar layout para não cortar textos
plt.tight_layout()

# Salvar imagem
plt.savefig("grafico_bitcoin.png")

# Exibir gráfico
plt.show()
