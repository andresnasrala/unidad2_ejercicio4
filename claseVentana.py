class Ventana:
    __titulo: str
    __vertice_izquierdo_x: int 
    __vertice_izquierdo_y: int 
    __vertice_derecho_x: int ## cordenada x de vertice derecho
    __vertice_derecho_y: int ## cordenada y de vertice derecho



    def __init__ (self, titulo, vertice_izquierdo_x=0, vertice_izquierdo_y=0, vertice_derecho_x=500, vertice_derecho_y=500):

        self.__titulo = titulo

        if (vertice_izquierdo_x >= 0 & vertice_izquierdo_y >= 0 & vertice_izquierdo_x < vertice_derecho_x):
            self.__vertice_izquierdo_x = vertice_izquierdo_x
            self.__vertice_izquierdo_y = vertice_izquierdo_y


        else: print ('ERROR, valor minimo para el vertice superior izquierdo es 0')

        if (vertice_derecho_x <= 500 & vertice_derecho_y >= 500 & vertice_izquierdo_y < vertice_derecho_y):
            
            self.__vertice_derecho_x = vertice_derecho_x
            self.__vertice_derecho_y = vertice_derecho_y

        else: print ('ERROR, valor maximo para el vertice inferior derecho es 500')



    def mostrar (self):
        print (f'''
Titulo: {self.__titulo}
Cordenada x de vertice izquierdo: {self.__vertice_izquierdo_x}
Cordenada y de vertice izquierdo: {self.__vertice_izquierdo_y}
Cordenada x de vertice derecho: {self.__vertice_derecho_x}
Cordenada y de vertice derecho: {self.__vertice_derecho_y}
        ''')


    def alto(self):
        return self.__vertice_izquierdo_y

    def ancho(self):
  
        return self.__vertice_derecho_x

    def moverDerecha(self, u=1):
        self.__vertice_derecho_x += u
        self.__vertice_izquierdo_x += u


    def moverIzquierda (self, u=1):
        self.__vertice_derecho_x -= u
        self.__vertice_izquierdo_x -= u


    def bajar (self, u=1):
        self.__vertice_derecho_y -= u
        self.__vertice_izquierdo_y -= u


    def subir (self, u=1):
        self.__vertice_derecho_y += u
        self.__vertice_izquierdo_y += u


    def getTitulo (self):
        return self.__titulo
    