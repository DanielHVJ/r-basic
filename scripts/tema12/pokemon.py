pokemon = pd.read_csv("../../data/Pokemon.csv")
print(pokemon.head())
print(pokemon.shape)

pokemon2 = pokemon[pokemon["Generation"]==1]
pokemon2 = pokemon2[["Type 1", "Type 2", "Speed"]]
print(pokemon2.shape)
pokemon2 = pokemon2.dropna()
print(pokemon2.shape)

pokemon.hist(column="Speed", figsize=(6,6), color="blue", bins = 50)
plt.show()

pokemon.hist(column="Total", figsize=(6,6), color="blue", bins = 20)
plt.show()

