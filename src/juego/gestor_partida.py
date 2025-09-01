from src.juego.cacho import Cacho
from src.juego.contador_pintas import contador_pintas
from src.juego.arbitro_ronda import ArbitroRonda
from src.juego.dado import Dado

class GestorPartida:
    def __init__(self, jugadores, pos_inicial = 0):
        self.jugadores = []
        self.pos_inicial = pos_inicial
        self.turno_actual = pos_inicial
        
        for jugador in jugadores:
            nuevo_jugador = {
                'nombre': jugador,
                'cacho': Cacho()
            }
            self.jugadores.append(nuevo_jugador)
            
    def get_jugadores(self):
        return self.jugadores
    
    def decidir_inicial(self):
        return self.jugadores[self.pos_inicial]
    
    def get_turno_actual(self):
        return self.jugadores[self.turno_actual]
    
    def siguiente_turno(self):
        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)
        return self.get_turno_actual()

    def ronda_especial(self):
        for jugador in self.jugadores:
            if len(jugador["cacho"].get_lista_de_dados()) == 1:
                return True
        return False

    def validar_apuesta(self, apuesta_actual, apuesta_nueva):
        cantidad_actual, pinta_actual = apuesta_actual
        cantidad_nueva, pinta_nueva = apuesta_nueva

        # Verificar si la apuesta actual es de ases
        if pinta_actual == 1:
            if pinta_nueva == 1 and cantidad_nueva > cantidad_actual:
                return True
            if pinta_nueva != 1 and cantidad_nueva > (cantidad_actual * 2):
                return True
            return False
        
        # Verificar si la apuesta nueva es de ases
        if pinta_nueva == 1:
            if cantidad_nueva > (cantidad_actual // 2):
                return True
            return False

        mayor_pinta = pinta_nueva > pinta_actual
        mayor_cantidad = cantidad_nueva > cantidad_actual
        if mayor_pinta or mayor_cantidad:
            return True
        return False
