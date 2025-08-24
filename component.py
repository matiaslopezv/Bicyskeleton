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
        return f"{self.tipo}"

class desviadorTrasero(Transmision):
    def __init__(self, nombre:str, fabricante:str, serie:str, velocidades:int, caja:str, piñon_min:int, piñon_max:int, plato_min:int, plato_max:int, capacidad:0, dif_delantera:0, montaje:str):
        super().__init__(nombre, fabricante, serie, velocidades)
        self.tipo = "Desviador Trasero"
        self.caja = caja
        self.piñon_min = piñon_min
        self.piñon_max = piñon_max
        self.plato_min = plato_min
        self.plato_max = plato_max
        self.capacidad =  (plato_max - plato_min)+(piñon_max - piñon_min)
        self.dif_delantera =  plato_max - plato_min
        self.montaje = montaje #directo/hanger(postiza)
    def __str__(self):
        return f"{self.nombre} - {self.fabricante} {self.serie} - velocidades{self.velocidades}v {self.piñon_min}t {self.piñon_max}t {self.plato_min}t {self.piñon_max}t {self.capacidad}t {self.dif_delantera}t {self.montaje}"

class desviadorDelantero(Transmision):
    def __init__(self, nombre:str, fabricante:str, serie:str, velocidades:int, montaje:str, diametro_abr:float, desarrollo_delantero:str, desarrollo_trasero:str):
        super().__init__(nombre, fabricante, serie, velocidades)
        self.tipo = "Desviador Delantero"
        self.montaje = montaje 
        self.desarrollo_delantero = desarrollo_delantero
        self.desarrollo_trasero = desarrollo_trasero
        self.diametro_abr = diametro_abr
    def __str__(self):
        return f"{self.nombre} - {self.fabricante} {self.serie} - {self.velocidades}v {self.montaje} {self.diametro_abr}mm {self.desarrollo_delantero}v/{self.desarrollo_trasero}v"

class Cassette(Transmision):
    def __init__(self, nombre:str, fabricante:str, serie:str, velocidades:int, dientes_min:int, dientes_max:int, nucleo_compatibilidad:str):
        super().__init__(nombre, fabricante, serie, velocidades)
        self.tipo = "Cassette"
        self.dientes_min = dientes_min
        self.dientes_max = dientes_max
        self.nucleo_compatibilidad = nucleo_compatibilidad
    def __str__(self):
        return f"{self.nombre} - {self.fabricante} ({self.serie}) - {self.velocidades}v ({self.dientes_min}-{self.dientes_max} dientes) - Núcleo: {self.nucleo_compatibilidad}"

class Cadena(Transmision):
    def __init__(self, nombre:str, fabricante:str, serie:str, velocidades:int, paso, compatibilidad_plato):
        super().__init__(nombre, fabricante, serie, velocidades)
        self.tipo = "Cadena"
        self.paso = paso
        self.compatibilidad_plato = compatibilidad_plato
    def __str__(self):
        return f"{self.nombre} - {self.fabricante} ({self.serie}) - {self.paso} {self.compatibilidad_plato} "

class Plato(Transmision):
    def __init__(self, nombre:str, fabricante:str, serie:str, velocidades:int, dientes:int, bcd:float, compatibilidad_montaje:str):
        super().__init__(nombre, fabricante, serie, velocidades)
        self.tipo = "Plato"
        self.dientes = dientes
        self.bcd = bcd
        self.compatibilidad_montaje = compatibilidad_montaje
    def __str__(self):
        return f"{self.nombre} - {self.fabricante} ({self.serie}) - {self.bcd} {self.compatibilidad_montaje} "

class Bielas(Transmision):
    def __init__(self, nombre:str, fabricante:str, serie:str, velocidades:int, largo:int, tipo_eje:str, platos:list):
        super().__init__(nombre, fabricante, serie, velocidades)
        self.tipo = "Bielas"
        self.largo = largo
        self.tipo_eje = tipo_eje
        self.platos = platos
    def __str__(self):
        return f"{self.nombre} - {self.fabricante} ({self.serie}) - {self.largo} {self.tipo_eje} {self.platos}"
    
class SistemaTransmision:
    def __init__(self):
        self.desviador_delantero = None
        self.desviador_trasero = None
        self.cassette = None
        self.cadena = None
        self.bielas = None
    
    def __str__(self):
        return (
            f"Sistema de Transmisión:\n"
            f"  - Desviador Delantero: {self.desviador_delantero}\n"
            f"  - Desviador Trasero: {self.desviador_trasero}\n"
            f"  - Cassette: {self.cassette}\n"
            f"  - Cadena: {self.cadena}\n"
            f"  - Bielas: {self.bielas}"
        )
#--------------------------------------------------------------------------------------------------------------------------------

class Frenos(Componente):
    def __init__(self, nombre, fabricante, serie, tipo):
        super().__init__(nombre, fabricante, serie, tipo="Frenos")
    def __str__(self):
        return f"[{self.tipo}]"

class frenoDelantero(Frenos):#tipo: llanta o disco
    def __init__(self, nombre:str, fabricante:str, serie:str, tipo:str, modelo:str, tipo_freno:str, mec_hidr:bool):
        super().__init__(nombre, fabricante, serie, tipo)
        self.tipo = "Freno Delantero"
        self.modelo = modelo
        self.tipo_freno = tipo_freno
        self.mec_hidr = mec_hidr
    def __str__(self):
        return f"{self.modelo} {self.tipo_freno}"    

class frenoTrasero(Frenos):#tipo: llanta o disco/ mec_hidr = mecanico(1) o hidraulico(0)
    def __init__(self, nombre, fabricante, serie, tipo, modelo, tipo_freno:str, mec_hidr:bool):
        super().__init__(nombre, fabricante, serie, tipo)
        self.tipo="Freno Trasero"
        self.modelo = modelo
        self.tipo_freno = tipo_freno
        self.mec_hidr = mec_hidr 
    def __str__(self):
        return f"{self.modelo} {self.tipo_freno}"

class manetaDeFrenos(Frenos):
    def __init__(self, nombre, fabricante, serie, tipo, modelo, tipo_maneta:str):
        super().__init__(nombre, fabricante, serie, tipo)
        self.tipo="Maneta de Frenos"
        self.modelo = modelo
        self.tipo_maneta = tipo_maneta
    def __str__(self):
        return f"{self.modelo} {self.tipo_maneta}"

class SistemaFrenos():
    def __init__(self):
        self.frenoDelantero = None
        self.frenoTrasero = None
        self.manetasDeFreno = None
    
    def __str__(self):
        
        return (
            f"Sistema de Frenos:\n"
            f"  - Freno Delantero: {self.frenoDelantero}\n"
            f"  - Freno Trasero: {self.frenoTrasero}\n"
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


# frontDesviador = desviadorDelantero("FD-R8000", "Shimano", "Ultegra", 11, "Abrazadera", 34.9, 2, 11)
# rearDesviador = desviadorTrasero("M773", "Shimano", "Deore", 11, "GS", 11, 36, 12, 32, 0, 0, "Directo")
# cassette = Cassette("Cassete", "Shimano", "Deore", 11, 11, 34, "HG")
# cadena = Cadena("Cadena Hg","Shimano","Deore XR", 11, 0.5, "Shimano/SRAM")
# plato = Plato("Platos","Shimano","Deore XR", 11, 52, 110.0, "5 tornillos")
# bielas = Bielas("Bielas","Shimano","Deore XR", 11, 175, "BB86", plato)
# sistema_transmision = SistemaTransmision()
# sistema_transmision.desviador_delantero = frontDesviador
# sistema_transmision.desviador_trasero = rearDesviador
# sistema_transmision.cassette = cassette
# sistema_transmision.cadena = cadena
# sistema_transmision.bielas = bielas

# print(sistema_transmision)

# #Crear unos frenos
# frenosDelantero = frenoDelantero("Frenos de pinza", "Shimano", "Deore", "Caliper", "BR-T4000", "V Brake", 0)
# frenosTrasero = frenoDelantero("Frenos de pinza", "Shimano", "Deore", "Caliper", "BR-T4000", "V Brake", 0)
# manetaFrenos = manetaDeFrenos("Manillas de Freno","Shimano", "Deore", "Solo frenos sin cambios", "AXS-44", "tipomaneta")
# sistema_Frenos = SistemaFrenos()
# sistema_Frenos.frenoDelantero = frenosDelantero
# sistema_Frenos.frenoTrasero = frenosTrasero
# sistema_Frenos.manetasDeFreno = manetaFrenos
# print(sistema_Frenos)


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
