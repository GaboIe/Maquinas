print("Ingrese los valores solicitados:")
 

I1 = 0
I2 = 0
pi = 3.1415926535

 # Se solicitan los valores al usuario 
N1 =  100 #float(input("Ingrese el numero de vueltas pata el primer arrollado de cables: "))
N2 =  50 #float(input("Ingrese el numero de vueltas pata el segundo arrollado de cables: "))
I1  =  1 #float(input("Tiene la corriente I1 o I2?: "))
i2 = 0
fp =  0.97 #float(input("Ingrese el factor de apilado: "))
Sc =  0.02 #float(input("Ingrese la seccion transversal de la columna central: "))
Sl =  0.01 #float(input("Ingrese la seccion transversal del resto: "))
A  =  0.01 #float(input("Ingrese el ancho del material ferromagnetico: "))
L1 =  1.10 #float(input("Ingrese la longitud de la parte izquiera del circuito: "))
L2 =  1.10 #float(input("Ingrese la longitud de la parte derecha del circuito: "))
L3 =  0.30 #float(input("Ingrese el alto de la Columna: "))
LE =  0.002 #float(input("Ingrese el ancho de entrehierro: "))
Q3 =  0.02 #float(input("Ingrese la magnitud del flujo magnetico en el entrehierro: "))
HB =  2 #float(input("Desea ingresar los valores de la curva H'B en forma de ecuación(1) o de tabla(2) "))

# Valor que se puede calcular de una vez
B3 = (Q3)/(Sc*fp)

if(I == 1):
    I1 = 20 #float(input("Inregre la corriente: "))
else:
    I2 = float(input("Inregre la corriente: "))
# Se Calcula la corriente 2
# Se calcula la densidad de flujo y la intensidad  en la columna
if (I2 == 0):
    if HB == 1:
        print("Ingrese los parametros")
        a = int(input("Ingrese el parametro a: "))
        b = int(input("Ingrese el parametro b: "))       
        B3 = (Q3)/Sc*fp
        H3 = B3/(a-B3*b)
    if HB ==2:
        Bn = []
        Hn = []    
        n = int(input("Cuantos parametros desea ingresar en su curva: "))
        for i in range(n):
            Bn.append(float(input("Ingrese el actual valor de B: ")))
            Hn.append(float(input("Ingrese el actual valor de H: ")))
        for i in range(n-1):
            if (B3 >= Bn[i]): 
                m = (Hn[i+1]-Hn[i])/(Bn[i+1]-Bn[i])
                k = Hn[i] -Bn[i]*m
                H3 = m*B3+ k
                
def H_B(self):
    if self.HB ==1:
        print("Ingrese los parametros")
        a = int(input("Ingrese el parametro a: "))
        b = int(input("Ingrese el parametro b: "))
        B3 = (Q3)/Sc*fp
        H3 = B3/(a-B3*b)
        for i in range(n):
            Bn.append(float(input("Ingrese el actual valor de B: ")))
            Hn.append(float(input("Ingrese el actual valor de H: ")))
        for i in range(n-1):
            if (B3 >= Bn[i]):
                m = (Hn[i+1]-Hn[i])/(Bn[i+1]-Bn[i])
                k = Hn[i] -Bn[i]*m
                H3 = m*B3+ k              
     
         
# Se calcula la longitud de la columna
Lf = L3 - LE
   # Hasta aqui, bien

# Se calcula la densidad y la intensidad en el entrehierro, el aire
Ba = Q3/Sc

# Esta siempre sigue la ecuacion
Ha = Ba/(4*pi *(10 **-7))


# Ahora se calcula la fuera electromotriz En la columna central

Fmh = float(H3*Lf + LE*Ha)

# Ahora se usa una ley de tensiones para calcular la intensidad en la parte izquierda
# N1*I1 = H1*L1 + Fmh
H1 = float((N1*I1-Fmh)/L1)

# Con esta intensidad se calcula la densidad de flujo en la parte izquierda, a esto hay que agregarle condicionales

if HB == 1:
      
    B1 = a*H1/(1+b*H1)

if HB ==2:

    for i in range(n-1):
        if (H1 >= Hn[i]):
            m = (Hn[i+1]-Hn[i])/(Bn[i+1]-Bn[i])
            k = Hn[i] -Bn[i]*m
            B1 = (H3 - k)/m
#print("B1", B1)

# Ahora se calcula el flujo en la parte izquierda
Q1 = B1*Sl*fp


# Ahora se aplica una ley de corrientes para calcular la corriente en el flujo de la derecha
Q2 = Q3-Q1


# Con el flujo se calcula la densidad en el lado derecho de la bobina
B2 = Q2/(Sl*fp)

if HB == 1:

    H2 = B2/(a-B2*b)
if HB ==2:

    for i in range(n-1):
        if (B2 >= Bn[i]):
                m = (Hn[i+1]-Hn[i])/(Bn[i+1]-Bn[i])
    k = Hn[i] -Bn[i]*m
    H2 = m*B2+ k

I2 = (H2*L2+Fmh)/N2
print(I2)
