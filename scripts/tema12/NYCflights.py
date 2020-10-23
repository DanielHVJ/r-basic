import pandas as pd
nyc = pd.read_csv("../../data/flights.csv")
nyc.head(5)

pydata = nyc[nyc["dest"]=="ORD"]
pydata = pydata[['carrier', 'dep_delay', 'arr_delay', 'origin']]
pydata = pydata[pydata['arr_delay']<6*60]
pydata = pydata.dropna()

print(pydata.head())
print(pydata.shape)

pydata.describe()

pydata.boxplot(column = "arr_delay", by='origin', figsize = (8,8))
plt.title("Retraso de los vuelo hacia Orlando desde NYC")
plt.show()