class Componente:
    def __init__(self, nombre:str, fabricante:str, serie:str, tipo:str="", modelo:str="", transmision=None, velocidades:int=0):
        self.nombre = nombre
        self.fabricante = fabricante
        self.serie = serie
        self.tipo = tipo
        self.modelo = modelo
        self.transmision = transmision
        self.velocidades = velocidades
    
    def __str__(self):
        return f"[{self.tipo}] {self.nombre} - {self.fabricante} ({self.serie}) - {self.modelo}"

class Transmision(Componente):
    def __init__(self, tipo):
        self.tipo = tipo
    
    def __str__(self):
        return f"Transmision tipo:{self.tipo}"

class desviadorTrasero(Transmision):
    def __init__(self, caja_larga:bool, capacidad_max:int, capacidad_total:int):
        super().__init__("Desviador Trasero")
        self.caja_larga = caja_larga
        self.capacidad_max = capacidad_max
        self.capacidad_total = capacidad_total

class desviadorDelantero(Transmision):
    def __init__(self, caja_larga:bool, capacidad_max:int, capacidad_total:int):
        super().__init__("Desviador Delantero")
        self.caja_larga = caja_larga
        self.capacidad_max = capacidad_max
        self.capacidad_total = capacidad_total   

class Cassette(Transmision):
    def __init__(self, dientes_min:int, dientes_max:int, nucleo_compatibilidad:str):
        super().__init__("Cassette")
        self.dientes_min = dientes_min
        self.dientes_max = dientes_max
        self.nucleo_compatibilidad = nucleo_compatibilidad

class Cadena(Transmision):
    def __init__(self, paso, compatibilidad_plato):
        super().__init__("Cadena")
        self.paso = paso
        self.compatibilidad_plato = compatibilidad_plato

class Plato(Transmision):
    def __init__(self, dientes:int, bcd:float, compatibilidad_montaje:str):
        super().__init__("Plato")
        self.dientes = dientes
        self.bcd = bcd
        self.compatibilidad_montaje = compatibilidad_montaje

class Bielas(Transmision):
    def __init__(self, largo:int, tipo_eje:str, platos:list):
        super().__init__("Bielas")
        self.largo = largo
        self.tipo_eje = tipo_eje
        self.platos = platos

class Frenos(Componente):
    def __init__(self, nombre:str, fabricante:str, serie:str, tipo_freno:str, montaje_caliper:str):
        super().__init__(nombre=nombre, fabricante=fabricante, serie=serie,tipo="Frenos",modelo=montaje_caliper, transmision=None, velocidades=0)
        self.tipo_freno = tipo_freno
        self.montaje_caliper = montaje_caliper

class Rueda(Componente):
    def __init__(self, nombre, fabricante, serie, diametro:int, ancho_interno:int, tipo_eje:str, nucleo_compatibilidad:str):
        super().__init__(nombre, fabricante, serie, diametro, ancho_interno, tipo_eje, nucleo_compatibilidad)
        self.diametro = diametro # ej. 29, 27.5, 700c
        self.ancho_interno = ancho_interno # en mm
        self.tipo_eje = tipo_eje # 'quick release', 'eje pasante 12mm'
        self.nucleo_compatibilidad = nucleo_compatibilidad # 'HG', 'Microspline', 'XD'

class Horquilla(Componente):
    def __init__(self, nombre: str, fabricante: str, serie: str, diametro_direccion: str, tipo_freno: str, tipo_eje: str):
        super().__init__(nombre, fabricante, serie, diametro_direccion, tipo_freno, tipo_eje)
        self.diametro_direccion = diametro_direccion # 'recto' o 'cónico'
        self.tipo_freno = tipo_freno # 'disco' o 'llanta'
        self.tipo_eje = tipo_eje # 'quick release', 'eje pasante 15mm'

class TijaSillin(Componente):
    def __init__(self, nombre: str, fabricante: str, serie: str, diametro: int):
        super().__init__(nombre, fabricante, serie, diametro)
        self.diametro = diametro # en mm

class Manillar(Componente):
    def __init__(self, nombre: str, fabricante: str, serie: str, ancho: int, diametro_potencia: int):
        super().__init__(nombre, fabricante, serie, ancho, diametro_potencia)
        self.ancho = ancho # en mm
        self.diametro_potencia = diametro_potencia # en mm (25.4, 31.8, 35)



# Crear un cassette
cassette = Cassette(11, 32, "Shimano HG")

# Crear una cadena
cadena = Cadena(0.5, "Shimano/SRAM")

# Crear un plato
plato = Plato(52, 110.0, "5 tornillos")

# Crear unas bielas con el plato
bielas = Bielas(175, "BB86", [plato])

#Crear unos frenos
frenos = Frenos("Frenos de pinza", "Shimano", "Deore", "Caliper", "Perno")

# Crear un componente bicicleta (ej. transmisión completa)
bicicleta = Componente("Grupo Shimano 105", "Shimano", "R7000", "R7000-GS" , "Transmisión", cassette, 22)

bicicletaDos = Componente(nombre="Cadena",
                          fabricante="Shimano",
                          serie = "Alivio",
                          tipo = "Transmisión",
                          modelo = "CN-HG53",
                          transmision=cadena,
                          velocidades= 21)
# print(bicicleta)
# print(bicicletaDos)
#print(cadena.__dict__)
# print(bielas.platos[0].dientes)
#print(list(frenos.__dict__.values()))
#print(frenos)
