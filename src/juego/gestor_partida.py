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
        pass