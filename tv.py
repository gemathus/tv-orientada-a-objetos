# lista de canales, volumen, contraste,
class TV:
    def __init__(self, marca, tamanio, volumen=5):
        self.marca = marca
        self.tamanio = tamanio
        
        self.prendida = False
        self.VOLUMEN_MAXIMO = 10
        self.VOLUMEN_MINIMO = 0
        self.volumen_actual = volumen
        self.lista_canales = [2,4,5,6,7,10,13,21]
    
    def cambiar_volumen(self, val):
        if self.prendida:
            #Validar que no exceda el volumen máximo
            self.volumen_actual = self.volumen_actual + val
            if self.volumen_actual > self.VOLUMEN_MAXIMO:
                self.volumen_actual = self.VOLUMEN_MAXIMO
            if self.volumen_actual < self.VOLUMEN_MINIMO:
                self.volumen_actual = self.VOLUMEN_MINIMO

    def power(self):
        if (self.prendida):
            self.prendida = False
        else:
            self.prendida = True

    def estatus_actual(self):
        return f"====================\n{self}\n\tPower: {self.prendida}\n\tVolumen: {self.volumen_actual}\n====================="
    
    def __repr__(self):
        return f"{self.marca} - {self.tamanio}"