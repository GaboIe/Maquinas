print("Ingrese los valores solicitados:")
 
I1 = 0
I2 = 0
pi = 3.1415926535
H3=1
 # Se solicitan los valores al usuario 
N1 =  int(input("Ingrese el numero de vueltas pata el primer arrollado de cables: "))
N2 =  int(input("Ingrese el numero de vueltas pata el segundo arrollado de cables: "))
I  =  int(input("Tiene la corriente I1 o I2?: "))
fp =  int(input("Ingrese el factor de apilado: "))
Sc =  int(input("Ingrese la seccion transversal de la columna central: "))
Sl =  int(input("Ingrese la seccion transversal del resto: "))
A  =  int(input("Ingrese el ancho del material ferromagnetico: "))
L1 =  int(input("Ingrese la longitud de la parte izquiera del circuito: "))
L2 =  int(input("Ingrese la longitud de la parte derecha del circuito: "))
L3 =  int(input("Ingrese el alto de la Columna: "))
LE =  int(input("Ingrese el ancho de entrehierro: "))
Q3 =  int(input("Ingrese la magnitud del flujo magnetico en el entrehierro: "))
HB =  int(input("Desea ingresar los valores de la curva H'B en forma de ecuación(1) o de tabla(2) "))
if(I == 1):
    I1 = I
else:
    I2 = I
if HB ==1:
    print("Ingrese los parametros")
    a = int(input("Ingrese el parametro a: "))
    b = int(input("Ingrese el parametro b: "))   
if HB ==2:
    Bn = []
    Hn = []    
    n = int(input("Cuantos parametros desea ingresar en su curva: "))
    for i in range(n):
        Bn.append(int(input("Ingrese el actual valor de B: ")))
        Hn.append(int(input("Ingrese el actual valor de H: ")))

# Se Calcula la corriente 2
# Se calcula la densidad de flujo y la intensidad  en la columna
if (I2 == 0):      
    B3 = (Q3)/Sc*fp
    H3 = B3/(a-B3*b)
    
# Se calcula la longitud de la columna
Lf = L3 - LE    

# Se calcula la densidad y la intensidad en el entrehierro
Ba = Q3/Sc
if (HB == 1):
    Ha = Ba/4*pi *(10 **-7)

    

# Ahora se calcula la fuera electromotriz En la columna central
Fmh = int(Lf*H3 + LE*Ba)

# Ahora se usa una ley de tensiones para calcular la intensidad en la parte izquierda
# N1*I1 = H1*L1 + Fmh
H1 = int((N1*I1*Fmh)/L1)

# Con esta intensidad se calcula la densidad de flujo en la parte izquierda
B1 =  a*H1/(1+b*H1)

# Ahora se calcula el flujo en la parte izquierda
Q1 = B1*Sl*fp

# Ahora se aplica una ley de corrientes para calcular la corriente en el flujo de la derecha
Q2 = Q3-Q1

# Con el flujo se calcula la densidad en el lado derecho de la bobina
B2 = Q2/(Sl*fp)

# Se calcula la intensidad de flujo
H2 = B2/(a-B2*b)

# Se aplica una ley de tensiones para calcular la corriente en la Bobina 2
# N2*I2 = H2*L2* + Fmh
I2 = (H2*L2+Fmh)/N2
print(I2)
