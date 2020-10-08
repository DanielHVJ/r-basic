# Ejercicio 1

#%%
from math import sqrt

def eq(a,b,n):
    if ((b**2) - 4*a*n) < 0:
        print('solución con número complejos')
    else:
        x1 = (-b + sqrt(b**2 - (4*a*n))) / (2 * a)
        x2 = (-b - sqrt(b**2 - (4*a*n))) / (2 * a)
        print("""Las soluciones de la ecuación son:
            x1 = {}
            x2 = {} """.format(x1, x2))


eq(1,4,2)

# %%

def palindromo():
    texto = input("Ingrese una palabra: ")
    copia = texto.lower()
    s_e = texto.replace(" ", "") 
    inv = s_e[::-1]
    print("Palabra invertida: ",texto[::-1])
    print("Longitud: ", len(texto)," letras")
    print("Eliminando espacios: ",s_e)
    print("Reducción: ", len(s_e)," letras")
    if (s_e == inv):
        print("CONCLUSION: la palabra ingresada SI es Palíndromo!!")
    else:
        print("CONCLUSION: La palabra ingresada NO es Palíndromo!!")  
        
palindromo()
# %%
#Creando un diccionario con clave y valor
diccionario = {
    1 : sqrt(1), 2 : sqrt(2),
    3 : sqrt(3), 4 : sqrt(4),
    5 : sqrt(5), 6 : sqrt(6),
    7 : sqrt(7), 8 : sqrt(8),
    9 : sqrt(9), 10 : sqrt(10),
}
diccionario


for key,val in diccionario.items():
   print (key,val)
    
# Otra forma de visualizar los datos

keys = diccionario.keys()
items = diccionario.items()
values= diccionario.values()
# %%

#Funcion para traducir
def trad(c):
    cont = 0
    #Creando un diccionario del abecedario español
    morse = {
        "A" : ".-", "B" : "-...",
        "C" : "-.-.", "CH" : "----",
        "D" : "-..", "E" : ".",
        "F" : "..-.", "G" : "--.",
        "H" : "....", "I" : "..", 
        "J" : ".---", "K" : "-.-", 
        "L" : ".-..", "M" : "--", 
        "N" : "-.", "Ñ" : "--.--", 
        "O" : "---", "P" : ".--.",
        "Q" : "--.-", "R" : ".-.",
        "S" : "...", "T" : "-",
        "U" : "..-", "V" : "...-",
        "W" : ".--", "X" : "-..-",
        "Y" : "-.--", "Z" : "--..",
} 
    for i in range(len(c)):
        letra=c[i]
        for clave,valor in morse.items():
            if (clave.lower() == letra):
                if (c[i]== "c" and c[i+1] == "h" ):
                    print(" --> reemplazar CH por -->",morse.get("CH"))
                print(" ",c[i]," --> Código -->",valor)
                #print("Mayuscula:",clave)
                #print("Codigo Morse:",valor)  
                
                

# %%
def traductor():
    texto = input("Ingrese una palabra o frase: ")
    copia = texto.lower()
    s_e = copia.replace(" ", "")
    trad(s_e)
    print("Eliminando espacios: ",s_e)
    print("Reducción: ",len(s_e)," letras")
    return  

traductor()
# %%
def play():
    A = {1 : "DE", 2 : "ES", 3 : "CN", 4 : "DE", 5 : "FR", 
         6 : "AU", 7 : "GRE", 8 : "RUS"}
    launch = {2 : "3 de diciembre de 1994", 4 : "4 de marzo del año 2000",
              6 : "11 de noviembre de 2006", 8 : "15 de noviembre de 2013"}
    for A in launch:
        print("Claves: ", A)
    return
    
play()

#%%

def criba(n):
	primos = []
	espr = [1 for i in range(n)]
	espr[0] = espr[1] = 0

	for i in range(n):
		if espr[i]:
			primos.append(i)
			h = 2
			while i*h < n:
				espr[i*h] = 0
				h += 1

	print("""Solución:
            primos = {}
            es primo = {} """.format(primos, espr))

criba(52)
# %%
def frase():
    texto = input("Ingrese una frase: ")
    copia = texto.title()
    print(copia)
frase()

#%%
def maxn():
    x = input("Ingrese un valor: ")
    y = input("Ingrese otro valor: ")
    return print("Máximo común divisor ",max(x,y))
maxn()

#%%

import string

def cesar():
    abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    frase = str(input("Ingrese la frase:  --> "))
    texto = frase.upper()
    ind_abc = 0
    ind_texto = 0
    n = 3 #Clave de desplazamiento
    p = int(len(abc)) 
    encrip = ""
    
    for t in range(0,len(texto)):
        texto_letra = texto[t]
        pos_t = len(texto) - len(texto) + ind_texto
        ind_texto +=1 
        
        for i in range(0,len(abc)):
            letra = abc[i]
            pos_x = len(abc) - len(abc) + ind_abc #número asociado a la letra
            
            #Formula matemática
            f = (pos_x + n) % p 
            ind_abc+=1    
            
            if (texto_letra == letra):
                encrip += abc[f]
                print("Palabra",texto_letra,"posc:",pos_t,"=",letra,"pos",pos_x,
                      "Encr:",abc[f],"pos",f)
    print("Palabra encrp --> ",encrip)
    
cesar()

#%%

def sortx():
    print("Orden")
    lista_nombres = ['Juan', 'María', 'Horacio' ,'Ana', 'Xee', 'Daniel', 
                     'Patricio', 'Carlos','Walter']
    lista_nombres.sort(key = str.lower)
    print("A - Z : ",lista_nombres)
    lista_nombres.sort(key=str.lower, reverse=True)
    print("Inverso : ",lista_nombres)
    lista_nombres.sort(key = len)
    print("Longitud: ",lista_nombres)
    
sortx()