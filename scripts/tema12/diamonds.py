import pandas as pd
diamonds = pd.read_csv('../../data/diamonds.csv', header=0)

diamonds.head()
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

print(diamonds.shape)
print(diamonds.head(10))

# Histograma
diamonds.hist(column="carat", figsize=(8,8), color="blue", 
              bins = 50, range = (0,3.5))
plt.show()

# Outliers
print(diamonds[diamonds["carat"]>3.5])

# Boxplots
plt.clf() # borra el gráfico anterior
diamonds.boxplot(column = "price", figsize = (8,8))
plt.show()

diamonds.boxplot(column = "price", by = "clarity", figsize = (8,8))
plt.show()

diamonds.boxplot(column = "carat", by = "clarity", figsize = (8,8))
plt.show()

## Densidades

plt.clf()
diamonds["carat"].plot(kind="density", figsize=(8,8), xlim=(0,5))
plt.show()

## Tabla de frecuencias y Barplot

carat_table = pd.crosstab(index=diamonds["clarity"], columns="count")
print(carat_table)
plt.clf()

carat_table.plot(kind="bar", figsize=(8,8))
plt.show()

carat_table_2 = pd.crosstab(index=diamonds["clarity"], columns=diamonds["color"])
print(carat_table_2)
plt.clf()
carat_table_2.plot(kind="bar", figsize=(8,8), stacked=True)
plt.show()
plt.clf()
carat_table_2.plot(kind="bar", figsize=(8,8), stacked=False)
plt.show()

## Scatterplot
diamonds.plot(kind="scatter", x = "carat", y = "price", figsize=(10,10), ylim=(0,20000), xlim = (0,6), alpha = 0.1)
plt.show()