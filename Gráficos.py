#GRÁFICO DE BARRAS VENDA DA SEMANA
from typing import Dict
#Importando Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

#Analisando vendas da semana
Dados = {
'Dias':['Segunda','Terça','Quarta','Quinta','Sexta','Sábado'],
'Venda':[26 ,31 ,455 ,2 ,80 ,1290],
}

#Transformando o dicionario dados em tabela para pandas(DataFrame)
df = pd.DataFrame(Dados)

#Exibe os dados no terminal
print(df)

#Cria uma figura do tamanho 10x7 polegadas(o tamanho e de sua escolha)
plt.figure(figsize=(10,7))
#Cria o grafico de barras
plt.bar(df['Dias'],df['Venda'])
#Title(Título) do grafico
plt.title('Vendas da semana')
#Eixo x Horizontal dias
plt.xlabel('Dias')
#Eixo y Vertical vendas
plt.ylabel('Vendas'),
#Dar espaço entre colunas
alpha = 1.0
#Exibir o Grafico
plt.show()






#GRÁFICO DE LINHA VENDAS DA SEMANA
from typing import Dict
#Importando Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

#Analisando vendas da semana
Dados = {
'Dias':['Segunda','Terça','Quarta','Quinta','Sexta','Sábado'],
'Venda':[26 ,31 ,455 ,2 ,80 ,1290],
}

#Transformando o dicionario dados em tabela para pandas(DataFrame)
df = pd.DataFrame(Dados)

#Exibe os dados no terminal
print(df)

plt.figure(figsize=(10,7))
#Cria um grafico de linha
plt.plot (df['Dias'],
df['Venda'],
#Cria as bolinhas no grafico (marker)
marker="o",
#Traça a linha no grafico (linestyle)
linestyle="--")
#Title(Título)
plt.title("Vendas da Semana")
#Eixo X
plt.xlabel("Dias")
#Eixo y
plt.ylabel("Venda")
#Cria uma grade no fundo para facilitar leitura (GRID)
plt.grid(True)
#Exibe o Grafico de linha
plt.show()
