# La convención de nombres con un doble guion bajo al principio (como __verifica_primo) se utiliza en Python para 
#indicar que un método o atributo es privado y que no debe ser accedido desde fuera de la clase.

class Herramientas:
    def __init__(self, lista): 
        self.lista = lista

    def verifica_primo(self):
        for i in self.lista:
            if(self.__verifica_primo(i)):
                print(f"El elemento {i} SI es un primo")
            else:
                print(f"El elemento {i} NO es un primo")


    def __verifica_primo(self, nro):
        es_primo = True
        for i in range(2, nro):
            if(nro % i == 0):
                es_primo = False
                break
        return es_primo   
    
    def valor_modal(self, lista):
        lista_unicos = []
        lista_repeticiones = []
        for elemento in lista:
            if(elemento in lista_unicos):
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if(lista_repeticiones[i] > maximo):
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        
        return moda, maximo
    
    def conversion_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__conversion_grados(i, origen, destino),'grados',destino)

    def __conversion_grados(self, valor, medida_origen, medida_destino):
        if medida_origen == "celsius":
            if medida_destino == "farenheit":
                valor_destino = valor*(9/5) + 32
            elif medida_destino == "kelvin":
                valor_destino = valor + 273.15
            elif medida_destino == "celsius":
                valor_destino = valor
            else:
                print("Parámetro de destino incorrecto")
        elif medida_origen == "farenheit":
            if medida_destino == "celsius":
                valor_destino = (valor - 32) * 5/9
            elif medida_destino == "kelvin":
                valor_destino = (valor - 32)*5/9 + 273.15
            elif medida_destino == "farenheit":
                valor_destino = valor
            else:
                print("Parámetro de destino incorrecto")
        elif medida_origen == "kelvin":
            if medida_destino == "celsius":
                valor_destino = valor - 273.15
            elif medida_destino == "farenheit":
                valor_destino = (valor - 273.15) *9/5 + 32
            elif medida_destino == "kelvin":
                valor_destino = valor
            else:
                print("Parámetro de destino incorrecto")
        else:
            print("Parámetro de origen incorrecto")

        return valor_destino
    
    
    def factorial(self):
        for i in self.lista:
            print(f"El factorial de {i} es = {self.__factorial(i)}")
    
    
    def __factorial(self, numero):
        if type(numero) != int:
            return "El número debe de ser cardinal"
        if numero <= 1:
            return 1
        numero = numero * self.__factorial(numero - 1)
        
        return numero