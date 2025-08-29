import pytest
from src.juego.arbitro_ronda import ArbitroRonda

class FakeContadorPintas:
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def contar(self, pinta):
        return self.cantidad

class TestArbitroRonda:
    def test_pierde_el_que_duda(self):
        contador = FakeContadorPintas(3)
        arbitro = ArbitroRonda(contador)
        resultado = arbitro.determinar_duda(apuesta=(3, 2), jugador_apuesta="Jugador1", jugador_duda="Jugador2")
        assert resultado['pierde'] == "Jugador2"

    def test_pierde_el_que_apuesta(self):
        contador = FakeContadorPintas(2)
        arbitro = ArbitroRonda(contador)
        resultado = arbitro.determinar_duda(apuesta=(3, 2), jugador_apuesta="Jugador1", jugador_duda="Jugador2")
        assert resultado['pierde'] == "Jugador1"

    def test_calzar_correcto(self):
        contador = FakeContadorPintas(3)
        arbitro = ArbitroRonda(contador)
        resultado = arbitro.determinar_calza(apuesta=(3, 2), jugador_calza="Jugador1", dados_en_juego=10, cant_jugadores=4)
        assert resultado == True

    def test_calzar_incorrecto(self):
        contador = FakeContadorPintas(2)
        arbitro = ArbitroRonda(contador)
        resultado = arbitro.determinar_calza(apuesta=(3, 2), jugador_calza="Jugador1", dados_en_juego=10, cant_jugadores=4)
        assert resultado == False

    def test_calzar_invalido_por_cantidad_dados(self):
        contador = FakeContadorPintas(2)
        arbitro = ArbitroRonda(contador)
        with pytest.raises(Exception):
            arbitro.determinar_calza(apuesta=(3, 2), jugador_calza="Jugador1", dados_en_juego=9, cant_jugadores=4)
