## BERNOULLI

from scipy.stats import bernoulli
import matplotlib.pyplot as plt
p = 0.5
mean, var, skew, kurt = bernoulli.stats(p, moments = 'mvsk')
print("Media %f"%mean)
print("Varianza %f"%var)
print("Sesgo %f"%skew)
print("Curtosis %f"%kurt)

fix, ax = plt.subplots(1,1)
x = bernoulli.rvs(p, size = 100)
ax.hist(x)
plt.show()

## BINOMIAL

from scipy.stats import binom 
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1,1)
n = 200
p = 0.25

mean, var, skew, kurt = binom.stats(n, p, moments = 'mvsk')

print("Media %f"%mean)
print("Varianza %f"%var)
print("Sesgo %f"%skew)
print("Curtosis %f"%kurt)

x = np.arange(0, n+1)
ax.plot(x, binom.pmf(x, n, p), 'bo', ms = 8, 
        label = "Función de densidad de B(7,0.4)")
ax.vlines(x, 0, binom.pmf(x,n,p), colors = 'b', lw = 4, alpha = 0.5)

rv = binom(n,p)
ax.vlines(x,0, rv.pmf(x), colors = 'k', linestyles='--', lw = 1, 
          label = "Distribución teórica")
ax.legend(loc = 'upper right', frameon = False)
plt.show()

# 2do gráfico
fix, ax = plt.subplots(1,1)
r = binom.rvs(n, p, size = 10000)
ax.hist(r, bins = 10)
ax.set_title('Histograma de la random')
plt.show()

## GEOMETRICA

from scipy.stats import geom
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1,1)
p = 0.3
mean, var, skew, kurt = geom.stats(p, moments = 'mvsk')

x = np.arange(geom.ppf(0.01,p), geom.ppf(0.99, p))
ax.plot(x, geom.pmf(x, p), 'bo', ms = 8)
ax.set_title('Función de probabilidad de Geom(0.3)')
ax.vlines(x,0,geom.pmf(x,p),  colors = 'b', lw = 4, alpha = 0.5)

rv = geom(p)
ax.vlines(x,0,rv.pmf(x), colors = 'k', linestyles = '--', lw = 1, 
          label = "Frozen PMF")
ax.legend(loc = 'best')
plt.show()

print("Media %f"%mean)
print("Varianza %f"%var)
print("Sesgo %f"%skew)
print("Curtosis %f"%kurt)

fig, ax = plt.subplots(1,1)
prob = geom.cdf(x,p)
ax.plot(x, prob, 'bo', ms = 8, label = "Función de distribución acumulada")
plt.title('Función de distribución acumulada')
plt.show()

fig, ax = plt.subplots(1,1)
r = geom.rvs(p, size = 10000)
plt.hist(r)
plt.title('Histograma de la random')
plt.show()

