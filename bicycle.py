from component import Frenos

class Bicicleta:
    def __init__(self, nombre_perfil:str, cuadro, frenos):
        self.cuadro = cuadro
        self.transmision = {}
        self.frenos = frenos
        self.ruedas = {}
        self.suspension = {}
        self.manillar = {}
  
    def __str__(self):
        return f"Bicicleta: {self.cuadro} {self.frenos}" 
    
    def agregar_componente(self, componente):
        pass

    def verificar_compatibilidad(self):
        pass
        

    def obtener_lista_de_piezas(self): 
        pass

class Cuadro(Bicicleta):
    def __init__(self, marca:str, modelo:str, tipo_caja_pedalier:str, tipo_eje_trasero:str):
        self.tipo_caja_pedalier = tipo_caja_pedalier
        self.tipo_eje_trasero = tipo_eje_trasero
    
    def __str__(self):
        return f"Cuadro: {self.tipo_eje_trasero} {self.tipo_caja_pedalier}" 


cuadro = Cuadro("Surly", "Crosscheck", "68mm wide, standard English threaded 1.37 x 24t", "Semi-horizontal dropouts")


#Crear unos frenos
frenos = Frenos("Frenos de pinza", "Shimano", "Deore", "Caliper", "Perno")
bicicleta = Bicicleta("mi bici", cuadro, frenos)
print(bicicleta)
