# Acceso básico
L = [12, 34, 56, 78]
primero = L[0]
ultimo = L[-1]

# Listas anidadas 
L2 = [56, True , "texto", [1,2,3]]
valor = L2[3][1]  

print(len(L2))

# Longitud de la Lista
n = len (L)

# [Incio:Final]
L = [0,1,2,3,4,5,6,7,8,9]
sub = L[2:5]

#Omitir Valores
ini = L[:4]
fin = L [5:]

#Con paso (step)
paso = L [::2]

#indices negativos
neg = L[-4:-1]

#Copia completa
copia = L[:]

#Modificar elementos dentro de una Lista
L = [42, 45, 67, 109]
