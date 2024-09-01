"""
## Ejercicio 1
Escribir una función que aplique un descuento a un precio 
y otra que aplique el IVA a un precio. 
Escribir una tercera 
función que reciba un diccionario con los precios y porcentajes
de una cesta de la compra, y una de las funciones anteriores, y 
utilice la función pasada para aplicar los descuentos o el IVA a 
los productos de la cesta y devolver el precio final de la cesta.
"""
#Listas
mes={1:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}
listaCompra={7:'Manzana',10:'Coca',15:'Bigote(Chocolate)',25:'Bigote(Cajeta)',20:'Galletas(Chookies)'}
#Contadores
dia=0
numeroMes=1
#Numero de elementos en la listaCompra
totalListaCompra = len(listaCompra)

def descuento(precio):  #Funcion que aplica descuento a un precio 
        return precio - (precio * 0.50) 

def ivaAplicado(precio): #Funcion que aplica el IVA a un precio
        return precio * 1.25



while True:
    print("Bienvenido a tu super mercado de lujo! el dia de hoy es ",mes[numeroMes], " ", dia)
    print("Dime que deseas hacer el dia de hoy")
    print("Comprar un producto (1)")
    print("O deseas comprar varios productos?(2)")
    eleccion = int(input("O si deseas salir!:D (3)"))

    if eleccion == 1:
        precio = int(input("Ingrese el precio del producto!"))
        print("Felicidades tiene un descuento del 50%!!! en total pagaria",descuento(precio))
        print("Desgraciadamente como vivimos en un pais capitalista el IVA del 15% se le tiene que aplicar :( y en total seria:  ", ivaAplicado(descuento(precio)))

    if eleccion == 2:
        print("Bueno al parecer deseas adquirir varios productos asi que aqui tienes una lista de lo disponible")
        print("-------------------------------------------------------------------------")
        for 0 in [totalListaCompra]:
             print (listaCompra.values)
             

    if eleccion == 3: 
         break

    if dia == int(30):
        numeroMes +=1
    


