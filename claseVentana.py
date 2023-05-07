class Ventana:
    __titulo=""
    __xSupIz=0
    __ySupIz=0
    __xInfDe=0
    __yInfDe=0

    def __init__(self,titulo,xid=0,yid=0,xsi=0,ysi=0):
        self.__titulo=titulo
        self.__xSupIz=xsi
        self.__ySupIz=ysi
        self.__xInfDe=xid
        self.__yInfDe=yid

    

    def mostrar(self):
        print("Vertice superior izquierdo({},{}) vertice inferior derecho ({},{})".format(self.__xSupIz,self.__ySupIz,self.__xInfDe,self.__yInfDe))

    
    def getTitulo(self):
        return self.__titulo
    

    def ancho(self):
        if (self.__xSupIz<self.__xInfDe):
            ancho=self.__xInfDe-self.__xSupIz
            return ancho
        
        else:
            print("Error no se puede calcular")


    def alto (self):
        if (self.__yInfDe>self.__ySupIz):
            alto=self.__yInfDe-self.__ySupIz
            return alto
        else:
            print("Error no se puede calcular")

    def moverDerecha(self,num1):
        valor= self.verificarDerechoX(num1)
        if (valor==True):
            self.__xSupIz+=num1
            self.__xInfDe+=num1
        else:
            print("No se pueede mover a la derecha la ventana")       

    def moverIzquierda (self,num2):
        valor=self.verificarIzquierdoX(num2)
        if (valor==True):
            self.__xSupIz-=num2
            self.__xInfDe-=num2
        else:
            print("No se pueede mover a la izquierda la ventana")  

    def bajar (self, num3=1):
        valor=self.verificarIzquierdoy(num3)
        if (valor==True):
            self.__yInfDe-=num3
            self.__ySupIz-=num3
        else:
            print("No se pueede bajar la ventana") 

    def subir (self, num4=1):
        valor=self.verificarDerechoy(num4)
        if (valor==True):
            self.__yInfDe+=num4
            self.__ySupIz+=num4  
        else:
            print("No se pueede subir la ventana")    


    def verificarDerechoX(self, num):
        valor=self.__xInfDe + num
        if (valor<=500):
            return True
        else:
            return False
        
    def verificarDerechoy(self, num):
        valor=self.__yInfDe + num
        if (valor<=500):
            return True
        else:
            return False
        
    def verificarIzquierdoX(self, num):
        valor=self.__xSupIz - num
        if (valor>=0):
            return True
        else:
            return False
        

    def verificarIzquierdoy(self, num):
        valor=self.__ySupIz - num
        if (valor>=0):
            return True
        else:
            return False
        




        
    



