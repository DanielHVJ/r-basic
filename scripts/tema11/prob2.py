## HYPERGEOM

from scipy.stats import hypergeom
import matplotlib.pyplot as plt
import numpy as np

[M, n, N] = [20, 12, 7]
rv = hypergeom(M, n, N)
x = np.arange(0, n+1)
y = rv.pmf(x)

mean, var, skew, kurt = rv.stats(moments = 'mvsk')
print("Media %f"%mean)
print("Varianza %f"%var)
print("Sesgo %f"%skew)
print("Curtosis %f"%kurt)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, 'bo' )
ax.vlines(x,0,y, lw = 2, alpha = 0.5)
ax.set_xlabel("Número de perros entre los 12 elegidos al azar")
ax.set_ylabel("Distribución de probabilidad de H(13,7,12)")
plt.show()

## POISSON

import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt


mu = 5
mean, var, skew, kurt = poisson.stats(mu, moments = 'mvsk')
print("Media %f"%mean)
print("Varianza %f"%var)
print("Sesgo %f"%skew)
print("Curtosis %f"%kurt)


fig, ax = plt.subplots(1,1)
x = np.arange(0, 12)
ax.plot(x, poisson.pmf(x, mu), 'bo', ms = 8, label = 'Poisson(0.8)')
ax.vlines(x,0, poisson.pmf(x,mu), colors = 'b', lw = 4, alpha = 0.5)
ax.legend(loc = "best", frameon = False)
plt.show()


## BINOMIAL NEGATIVA

from scipy.stats import nbinom 
import matplotlib.pyplot as plt
import numpy as np

n = 7
p = 0.4
mean, var, skew, kurt = nbinom.stats(n, p, moments = 'mvsk')
print("Media %f"%mean)
print("Varianza %f"%var)
print("Sesgo %f"%skew)
print("Curtosis %f"%kurt)

fig, ax = plt.subplots(1,1)
x = np.arange(0, n+1)
ax.plot(x, nbinom.pmf(x, n, p), 'bo', ms = 8, 
        label = "Función de densidad de B(7,0.4)")
ax.vlines(x, 0, nbinom.pmf(x,n,p), colors = 'b', lw = 4, alpha = 0.5)

rv = nbinom(n,p)
ax.vlines(x,0, rv.pmf(x), colors = 'k', linestyles='--', lw = 1, 
          label = "Distribución teórica")
ax.legend(loc = 'best', frameon = False)
plt.show()

fix, ax = plt.subplots(1,1)
r = binom.rvs(n, p, size = 10000)
ax.hist(r, bins = n)
plt.show()


##  DISTRIBUCION UNIFORME

from scipy.stats import uniform
import matplotlib.pyplot as plt 
import numpy as np

a = 0
b = 1

loc = a
scale = b-a

rv = uniform(loc = loc, scale = scale)

mean, var, skew, kurt = rv.stats(moments = 'mvsk')
print("Media %f"%mean)
print("Varianza %f"%var)
print("Sesgo %f"%skew)
print("Curtosis %f"%kurt)

fig, ax = plt.subplots(1,1)
x = np.linspace(-0.1, 1.1, 120)
ax.plot(x, rv.pdf(x), 'k-', lw = 2, label = "U(0,1)")

r = rv.rvs(size = 100000)  # crea aleatorios
ax.hist(r, density = True, histtype = "stepfilled", alpha = 0.25)

ax.legend(loc = 'best', frameon = False)
plt.show()

## DISTRIBUCION EXPONENCIAL

from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt

lam = 1.5
rv = expon(scale = 1/lam)

mean, var, skew, kurt = rv.stats(moments = 'mvsk')
print("Media %f"%mean)
print("Varianza %f"%var)
print("Sesgo %f"%skew)
print("Curtosis %f"%kurt)

fig, ax = plt.subplots(1,1)
x = np.linspace(0, 3, 1000)
ax.plot(x, rv.pdf(x), 'r-', lw = 5, alpha = 0.6, label = "Exp(10)")

r = rv.rvs(size = 100000)
ax.hist(r, bins = 20, density = True, histtype = 'stepfilled',
         alpha = 0.5)

ax.legend(loc = "best", frameon= False)
plt.show()