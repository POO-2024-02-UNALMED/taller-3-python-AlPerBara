class TV:

    numTV=0;

    def __init__(self, marca,  estado):
        
        self.marca=marca;
        self.canal=1;
        self.precio=500;
        self.estado=estado;
        self.volumen=1;
        self.control=None;
        TV.numTV+=1;

    #m ́etodos set y get para los atributos marca, canal, precio, volumen y control.

    def setMarca(self, marcaNueva):
        self.marca=marcaNueva;
    
    def getMarca(self):
        return self.marca;


    def setCanal(self, canalNuevo):
        if (self.estado==True) and (1<=canalNuevo<=120):
            self.canal=canalNuevo;

    def getCanal(self):
        return self.canal;


    def setPrecio(self, precioNuevo):
        self.precio=precioNuevo;

    def getPrecio(self):
        return self.precio;


    def setVolumen(self,volumenNuevo):
        if (self.estado==True) and (0<=volumenNuevo<=7):
            self.volumen=volumenNuevo;

    def getVolumen(self):
        return self.volumen;


    def setControl(self, controlNuevo):
        self.control=controlNuevo;
        self.control.setTv(self);

    def getControl(self):
        return self.control;


    @classmethod
    def setNumTV(cls, numeroNuevo):
        cls.numTV=numeroNuevo;

    @classmethod
    def getNumTV(cls):
        return cls.numTV;



    def turnOn(self):
        self.estado=True;

    def turnOff(self):
        self.estado=False;

    def getEstado(self):
        return self.estado;


    def canalUp(self):
        if (self.estado==True) and (self.canal<120):
            self.canal+=1;

    def canalDown(self):
        if (self.estado==True) and (self.canal>1):
            self.canal-=1;

    def volumenUp(self):
        if (self.estado==True) and (self.volumen<7):
            self.volumen+=1;

    def volumenDown(self):
        if (self.estado==True) and (self.volumen>0):
            self.volumen-=1;
