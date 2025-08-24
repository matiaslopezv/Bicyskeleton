from component import Frenos, SistemaTransmision, SistemaFrenos, Rueda

class Bicicleta:
    def __init__(self, nombre_perfil:str, cuadro, frenos):
        self.cuadro = cuadro
        self.transmision = SistemaTransmision()
        self.frenos = sistema_Frenos
        self.ruedas = {}
        self.suspension = {}
        self.manillar = {}
  
    def __str__(self):
        return f"{self.cuadro} {self.frenos} {self.transmision}" 
    
    def agregar_componente(self, componente):
        pass

    def verificar_compatibilidad(self):
        errores = []

        # Verificar tipo de frenos vs montaje del cuadro
        tipo_freno_cuadro = self.cuadro.tipo_frenos.lower()
        tipo_freno_delantero = self.frenos.frenoDelantero[5].lower()  # Ej: "V Brake"

        if "v-brake" in tipo_freno_delantero and "v-brake" not in tipo_freno_cuadro:
            errores.append("Freno delantero incompatible con el tipo de freno del cuadro.")

        # Verificar montaje trasero
        if self.cuadro.dTrasero_montaje.lower() != "hanger":
            errores.append("El cuadro no tiene montaje trasero tipo hanger para desviador estándar.")

        # Verificar manetas vs frenos
        tipo_maneta = self.frenos.manetasDeFreno[5].lower()
        if "tipomaneta" not in tipo_maneta:
            errores.append("Tipo de maneta no especificado o incompatible.")

        # Verificar espacio de eje trasero vs ruedas
        if "135" not in str(self.cuadro.espacio_eje_trasero):
            errores.append("Espacio de eje trasero incompatible con ruedas estándar QR.")

        # Verificar neumáticos vs clearance
        ancho_max = (self.cuadro.neumaticos_max.split("x")[1].strip())
        # Suponiendo que la rueda tiene atributo .ancho
        for rueda in self.ruedas.values():
            if rueda.ancho > ancho_max:
                errores.append(f"Neumático de {rueda.ancho}mm excede el máximo permitido por el cuadro.")

        if errores:
            print("⚠️ Incompatibilidades detectadas:")
            for e in errores:
                print(f"- {e}")
        else:
            print("✅ Todos los componentes son compatibles con el cuadro.")


    def obtener_lista_de_piezas(self): 
        pass

class Cuadro(Bicicleta):
    def __init__(self, marca:str, modelo:str, material:str, tipo_caja_pedalier:str, diametro_caja:str, estandar_eje_trasero:str, espacio_eje_trasero:str, neumaticos_max:str ,tipo_direccion:str, diametro_direccion:float, diametro_tubo_sillin:float, abrazadera_tubo_sillin:float, dDelantero_montaje:str, dTrasero_montaje:str, tipo_frenos:str, cableado:str):
        self.marca = marca
        self.modelo = modelo
        self.material = material
        self.tipo_caja_pedalier = tipo_caja_pedalier
        self.diametro_caja = diametro_caja
        self.estandar_eje_trasero = estandar_eje_trasero
        self.espacio_eje_trasero = espacio_eje_trasero
        self.neumaticos_max = neumaticos_max
        self.tipo_direccion = tipo_direccion
        self.diametro_direccion = diametro_direccion
        self.diametro_tubo_sillin = diametro_tubo_sillin
        self.abrazadera_tubo_sillin = abrazadera_tubo_sillin
        self.dDelantero_montaje = dDelantero_montaje
        self.dTrasero_montaje = dTrasero_montaje
        self.tipo_frenos = tipo_frenos
        self.cableado = cableado
    def __str__(self):
        return (
            "BICICLETA\n"
            "CUADRO:\n"
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Material: {self.material}\n"
            f"Tipo Eje Pedalier: {self.tipo_caja_pedalier}\n"
            f"Diametro Eje Pedalier: {self.diametro_caja}\n"
            f"Estandar Eje Trasero: {self.estandar_eje_trasero}\n"
            f"Espacio Eje Trasero: {self.espacio_eje_trasero}mm\n"
            f"Ancho Max. Neumaticos: {self.neumaticos_max}\n"
            f"Tipo de Dirección: {self.tipo_direccion}\n"
            f"Diametro Dirección: {self.diametro_direccion}mm\n"
            f"Diametro Tubo Sillín: {self.diametro_tubo_sillin}mm\n"
            f"Diametro Abrazadera Sillín: {self.abrazadera_tubo_sillin}\n"
            f"Montaje Desviador Delantero: {self.dDelantero_montaje}\n"
            f"Montaje Desviado Trasero: {self.dTrasero_montaje}\n"
            f"Tipo de Frenos: {self.tipo_frenos}\n"
            f"Cableado: {self.cableado}\n" 
                )


cuadro = Cuadro("Surly", "Crosscheck", "4130 Cr_Moly steel","Standard English Threaded", "68mm", "Dropout Spacing", "132.5", "700 x 42 mm", "No tapered", 11/8, 27.2, 31.8, "Abrazadera", "Hanger", "Cantilever/V-Brake", "Externo")

# Crear unos frenos
frenosDelantero = "Frenos de pinza", "Shimano", "Deore", "Caliper", "BR-T4000", "V Brake", 0
frenosTrasero = "Frenos de pinza", "Shimano", "Deore", "Caliper", "BR-T4000", "V Brake", 0
manetaFrenos = "Manillas de Freno","Shimano", "Deore", "Solo frenos sin cambios", "AXS-44", "tipomaneta"
sistema_Frenos = SistemaFrenos()
sistema_Frenos.frenoDelantero = frenosDelantero
sistema_Frenos.frenoTrasero = frenosTrasero
sistema_Frenos.manetasDeFreno = manetaFrenos
bicicleta = Bicicleta("mi bici", cuadro, sistema_Frenos)
print(bicicleta)
bicicleta.verificar_compatibilidad()



