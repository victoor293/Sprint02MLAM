import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("amostra_chargegrid.xlsx")


setores = df["faixa_renovavel"].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(
    setores,
    labels=setores.index,
    autopct="%1.1f%%",
    colors=["lightblue", "lightgreen", "orange"]
)
plt.title("Distribuição das Faixas de Energia Renovável")
plt.legend(title="Faixas")
plt.show()


barras = df["faixa_renovavel"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(
    barras.index,
    barras.values,
    color="skyblue",
    label="Quantidade"
)
plt.title("Quantidade de Países por Faixa de Energia Renovável")
plt.xlabel("Faixa de Energia Renovável")
plt.ylabel("Quantidade de Países")
plt.legend()
plt.show()


plt.figure(figsize=(8, 5))
plt.hist(
    df["renewables_share_energy"].dropna(),
    bins=10,
    color="lightgreen",
    edgecolor="black"
)
plt.title("Distribuição da Participação de Energias Renováveis")
plt.xlabel("Percentual de Energia Renovável")
plt.ylabel("Frequência")
plt.show()


plt.figure(figsize=(8, 5))
plt.boxplot(
    df["gdp"].dropna(),
    patch_artist=True
)
plt.title("Boxplot do PIB (GDP)")
plt.xlabel("GDP")
plt.ylabel("Valor")
plt.show()

print("=" * 50)
print("ANÁLISE UNIVARIADA - GDP")
print("=" * 50)

gdp = df["gdp"].dropna()

# tendência central
print("\nMEDIDAS DE TENDÊNCIA CENTRAL")
print("Média:", gdp.mean())
print("Mediana:", gdp.median())
print("Moda:", gdp.mode().iloc[0])

# dispersão
print("\nMEDIDAS DE DISPERSÃO")
print("Amplitude:", gdp.max() - gdp.min())
print("Variância:", gdp.var())
print("Desvio-padrão:", gdp.std())

# separatrizes
print("\nMEDIDAS SEPARATRIZES")
print("Q1 (25%):", gdp.quantile(0.25))
print("Q2 (50%):", gdp.quantile(0.50))
print("Q3 (75%):", gdp.quantile(0.75))



print("\n" + "=" * 50)
print("ANÁLISE UNIVARIADA - RENEWABLES_SHARE_ENERGY")
print("=" * 50)

renovavel = df["renewables_share_energy"].dropna()

# tendência central
print("\nMEDIDAS DE TENDÊNCIA CENTRAL")
print("Média:", renovavel.mean())
print("Mediana:", renovavel.median())
print("Moda:", renovavel.mode().iloc[0])

# dispersão
print("\nMEDIDAS DE DISPERSÃO")
print("Amplitude:", renovavel.max() - renovavel.min())
print("Variância:", renovavel.var())
print("Desvio-padrão:", renovavel.std())

# separatrizes
print("\nMEDIDAS SEPARATRIZES")
print("Q1 (25%):", renovavel.quantile(0.25))
print("Q2 (50%):", renovavel.quantile(0.50))
print("Q3 (75%):", renovavel.quantile(0.75))