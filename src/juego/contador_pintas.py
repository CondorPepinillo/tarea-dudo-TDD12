class contador_pintas:
    def __init__(self):
        self.ronda_especial = False

    def contar_pintas(self, cacho,apuesta_actual=None):
        if apuesta_actual == None:
            return {}
            
        nombres = {1: "As", 2: "Tonto", 3: "Tren", 4: "Cuadra", 5: "Quina", 6: "Sexto"}
        pintas = []
        for dado in cacho.gte_lista_de_dados():
            pintas.append(nombres[dado.get_pinta()])
        count = {}
        for pinta in pintas:
            if pinta in count:
                count[pinta] += 1
            else:
                count[pinta] = 1
        if not self.ronda_especial:
            count[apuesta_actual] += count.pop("As")
            return count
        else:
            return count
    
    def es_ronda_especial(self):
        return self.ronda_especial

    def activar_ronda_especial(self):
        self.ronda_especial = True

    def desactivar_ronda_especial(self):
        self.ronda_especial = False
    