class Componente:
    def __init__(self, nombre:str, fabricante:str, serie:str, tipo:str="", modelo:str=""):
        self.nombre = nombre
        self.fabricante = fabricante
        self.serie = serie
        self.tipo = tipo
        self.modelo = modelo
      
    
    def __str__(self):
        return f"[{self.tipo}] {self.nombre} - {self.fabricante} ({self.serie}) - {self.modelo}"

class Transmision(Componente):
    def __init__(self, nombre:str, fabricante:str, serie:str, velocidades:int=0):
        super().__init__(nombre, fabricante, serie, tipo="Transmisión")
        self.velocidades = velocidades
    def __str__(self):
        return f"Transmision tipo:{self.tipo}"

class desviadorTrasero(Transmision):
    def __init__(self, nombre:str, fabricante:str, serie:str, velocidades:int, caja_larga:bool, capacidad_max:int, capacidad_total:int):
        super().__init__(nombre, fabricante, serie, velocidades)
        self.tipo = "Desviador Trasero"
        self.caja_larga = caja_larga
        self.capacidad_max = capacidad_max
        self.capacidad_total = capacidad_total

class desviadorDelantero(Transmision):
    def __init__(self, nombre:str, fabricante:str, serie:str, velocidades:int, caja_larga:bool, capacidad_max:int, capacidad_total:int):
        super().__init__(nombre, fabricante, serie, velocidades)
        self.tipo = "Desviador Delantero"
        self.caja_larga = caja_larga
        self.capacidad_max = capacidad_max
        self.capacidad_total = capacidad_total   

class Cassette(Transmision):
    def __init__(self, nombre:str, fabricante:str, serie:str, velocidades:int, dientes_min:int, dientes_max:int, nucleo_compatibilidad:str):
        super().__init__(nombre, fabricante, serie, velocidades)
        self.tipo = "Cassette"
        self.dientes_min = dientes_min
        self.dientes_max = dientes_max
        self.nucleo_compatibilidad = nucleo_compatibilidad
    def __str__(self):
        return f"[{self.tipo}] {self.nombre} - {self.fabricante} ({self.serie}) - {self.velocidades}v ({self.dientes_min}-{self.dientes_max} dientes) - Núcleo: {self.nucleo_compatibilidad}"

class Cadena(Transmision):
    def __init__(self, nombre:str, fabricante:str, serie:str, velocidades:int, paso, compatibilidad_plato):
        super().__init__(nombre, fabricante, serie, velocidades)
        self.tipo = "Cadena"
        self.paso = paso
        self.compatibilidad_plato = compatibilidad_plato
    def __str__(self):
        return f"[{self.tipo}] {self.nombre} - {self.fabricante} ({self.serie}) - {self.paso} {self.compatibilidad_plato} "

class Plato(Transmision):
    def __init__(self, nombre:str, fabricante:str, serie:str, velocidades:int, dientes:int, bcd:float, compatibilidad_montaje:str):
        super().__init__(nombre, fabricante, serie, velocidades)
        self.tipo = "Plato"
        self.dientes = dientes
        self.bcd = bcd
        self.compatibilidad_montaje = compatibilidad_montaje
    def __str__(self):
        return f"[{self.tipo}] {self.nombre} - {self.fabricante} ({self.serie}) - {self.bcd} {self.compatibilidad_montaje} "

class Bielas(Transmision):
    def __init__(self, nombre:str, fabricante:str, serie:str, velocidades:int, largo:int, tipo_eje:str, platos:list):
        super().__init__(nombre, fabricante, serie, velocidades)
        self.tipo = "Bielas"
        self.largo = largo
        self.tipo_eje = tipo_eje
        self.platos = platos
    def __str__(self):
        return f"[{self.tipo}] {self.nombre} - {self.fabricante} ({self.serie}) - {self.largo} {self.tipo_eje} {self.platos}"
    
class SistemaTransmision:
    def __init__(self):
        # Los atributos son de los objetos de tus clases.
        self.desviador_delantero = None
        self.desviador_trasero = None
        self.cassette = None
        self.cadena = None
        self.bielas = None
    
    def __str__(self):
        # Aquí imprimes los detalles de cada componente
        return (
            f"Sistema de Transmisión:\n"
            f"  - Desviador Delantero: {self.desviador_delantero}\n"
            f"  - Desviador Trasero: {self.desviador_trasero}\n"
            f"  - Cassette: {self.cassette}\n"
            f"  - Cadena: {self.cadena}\n"
            f"  - Bielas: {self.bielas}"
        )
#--------------------------------------------------------------------------------------------------------------------------------

# class Frenos(Componente):
#     def __init__(self, nombre:str, fabricante:str, serie:str, tipo_freno:str, montaje_caliper:str):
#         super().__init__(nombre, fabricante, serie, tipo="Frenos", modelo=montaje_caliper)
#         self.tipo_freno = tipo_freno
#         self.montaje_caliper = montaje_caliper
#     def __str__(self):
#         return f"[{self.tipo}] - {self.fabricante} - {self.serie} - {self.tipo_freno} - {self.montaje_caliper}"
class Frenos(Componente):
    def __init__(self, nombre, fabricante, serie, tipo):
        super().__init__(nombre, fabricante, serie, tipo="Frenos")
    def __str__(self):
        return f"[{self.tipo}]"

class frenoDelantero(Frenos):#tipo: llanta o disco
    def __init__(self, nombre:str, fabricante:str, serie:str, tipo:str, modelo:str, ):
        super().__init__(nombre, fabricante, serie, tipo, modelo)
        self.tipo = "Freno Delantero"
        self.modelo = modelo

class frenoTrasero(Frenos):#tipo: llanta o disco
    def __init__(self, nombre, fabricante, serie, tipo, modelo):
        super().__init__(nombre, fabricante, serie, tipo)
        self.tipo="Freno Trasero"
        self.modelo = modelo

class manetaDeFrenos(Frenos):
    def __init__(self, nombre, fabricante, serie, tipo, modelo):
        super().__init__(nombre, fabricante, serie, tipo)
        self.tipo="Maneta de Frenos"
        self.modelo = modelo

class SistemaFrenos():
    def __init__(self):
        self.frenoDelantero = None
        self.frenoTrasero = None
        self.manetasDeFreno = None
    
    def __str__(self):
        # Aquí imprimes los detalles de cada componente
        return (
            f"Sistema de Frenos:\n"
            f"  - Freno Delantero: {self.frenoDelantero}\n"
            f"  - Freno Trasero: {self.frenoTraserotrasero}\n"
            f"  - Manetas de freno: {self.manetasDeFreno}"
        )

class Rueda(Componente):
    def __init__(self, nombre:str, fabricante:str, serie:str, diametro:int, ancho_interno:int, tipo_eje:str, nucleo_compatibilidad:str):
        super().__init__(nombre, fabricante, serie, tipo="Rueda")
        self.diametro = diametro
        self.ancho_interno = ancho_interno
        self.tipo_eje = tipo_eje
        self.nucleo_compatibilidad = nucleo_compatibilidad
    def __str__(self):
        return f"[{self.tipo}] - {self.nombre} - {self.fabricante} ({self.serie}) - {self.diametro}c"

class Horquilla(Componente):
    def __init__(self, nombre: str, fabricante: str, serie: str, diametro_direccion: str, tipo_freno: str, tipo_eje: str):
        super().__init__(nombre, fabricante, serie, tipo="Horquilla")
        self.diametro_direccion = diametro_direccion # 'recto' o 'cónico'
        self.tipo_freno = tipo_freno # 'disco' o 'llanta'
        self.tipo_eje = tipo_eje # 'quick release', 'eje pasante 15mm'
    def __str__(self):
        return f"[{self.tipo}] - {self.nombre} - {self.fabricante} ({self.serie}) - {self.diametro_direccion}"

class TijaSillin(Componente):
    def __init__(self, nombre: str, fabricante: str, serie: str, diametro: int):
        super().__init__(nombre, fabricante, serie, tipo="Tija Sillín")
        self.diametro = diametro # en mm
    def __str__(self):
        return f"[{self.tipo} - {self.nombre} - {self.fabricante} ({self.serie}) - {self.diametro}]"
    
class Manillar(Componente):
    def __init__(self, nombre: str, fabricante: str, serie: str, ancho: int, diametro_potencia: int):
        super().__init__(nombre, fabricante, serie, ancho, diametro_potencia)
        self.ancho = ancho # en mm
        self.diametro_potencia = diametro_potencia # en mm (25.4, 31.8, 35)
    def __str__(self):
        return f"[{self.tipo}] - {self.nombre} - {self.fabricante} - {self.ancho} - {self.diametro_potencia}"



# # Crear un cassette
# cassette = Cassette("Cassete", "Shimano", "Deore", 11, 11, 34, "HG")

# # Crear una cadena
# cadena = Cadena("Cadena Hg","Shimano","Deore XR", 11, 0.5, "Shimano/SRAM")

# # Crear un plato
# plato = Plato("Platos","Shimano","Deore XR", 11, 52, 110.0, "5 tornillos")

# # Crear unas bielas con el plato
# bielas = Bielas("Bielas","Shimano","Deore XR", 11, 175, "BB86", plato)

# #Crear unos frenos
# frenos = Frenos("Frenos de pinza", "Shimano", "Deore", "Caliper", "Perno")

# # #crear una rueda
# rueda = Rueda("Rueda", "Shimano", "Deore", 29, 25,"tipo_eje1", "HG")

# print(cassette)
# print(cadena)
# print(plato)
# print(bielas)
# print(frenos)
# print(rueda)
# Crear un componente bicicleta (ej. transmisión completa)
# bicicleta = Componente("Grupo Shimano 105", "Shimano", "R7000", "R7000-GS" , "Transmisión", cassette, 22)

# bicicletaDos = Componente(nombre="Cadena",
#                           fabricante="Shimano",
#                           serie = "Alivio",
#                           tipo = "Transmisión",
#                           modelo = "CN-HG53",
#                           transmision=cadena,
#                           velocidades= 21)
# # print(bicicleta)
# print(bicicletaDos)
#print(cadena.__dict__)
# print(bielas.platos[0].dientes)
#print(list(frenos.__dict__.values()))
#print(frenos)
