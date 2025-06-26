import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

df = pd.read_csv("acidentes.csv", parse_dates=["Data"])
df["Mes"] = df["Data"].dt.to_period("M")

# Acidentes por estado
estado_acidentes = df.groupby("Estado")["Acidentes"].sum()
estado_acidentes.plot(kind="bar", title="Acidentes por Estado")
plt.tight_layout()
plt.savefig("acidentes_por_estado.png")
plt.clf()

# Acidentes por mês
mes_acidentes = df.groupby("Mes")["Acidentes"].sum()
mes_acidentes.plot(kind="line", marker="o", title="Acidentes por Mês")
plt.tight_layout()
plt.savefig("acidentes_por_mes.png")
plt.clf()

# Acidentes por tipo de veículo
veiculo_acidentes = df.groupby("Tipo_Veiculo")["Acidentes"].sum()
veiculo_acidentes.plot(kind="pie", autopct='%1.1f%%', title="Acidentes por Tipo de Veículo")
plt.ylabel("")
plt.tight_layout()
plt.savefig("acidentes_por_veiculo.png")
plt.clf()
