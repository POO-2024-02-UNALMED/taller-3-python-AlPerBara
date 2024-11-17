class Control:
    def __init__(self):

        self.tv=None;

    def turnOn(self):
        self.tv.turnOn();

    def turnOff(self):
        self.tv.turnOff();

    def canalUp(self):
        self.tv.canalUp();

    def canalDown(self):
        self.tv.canalDown();

    def volumenUp(self):
        self.tv.volumenUp();

    def volumenDown(self):
        self.tv.volumenDown();

    def setCanal(self, canalPorConfigurar):
        self.tv.setCanal(canalPorConfigurar);

    def setVolumen(self, volumenPorColocar):
        self.tv.setVolumen(volumenPorColocar);
    

    def enlazar(self, televisorAlQueVamosAConectarElControl):
        self.tv=televisorAlQueVamosAConectarElControl;
        televisorAlQueVamosAConectarElControl.setControl(self);


    def setTv(self, tvNuevo):
        self.tv=tvNuevo;

    def getTv(self):
        return self.tv;
