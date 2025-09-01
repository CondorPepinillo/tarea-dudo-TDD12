import pytest
from src.juego.arbitro_ronda import ArbitroRonda
from src.juego.contador_pintas import contador_pintas
from src.juego.cacho import Cacho

class TestArbitroRonda:
    def test_pierde_el_que_duda(self):
        cachos = []
        for _ in range(4):
            cacho = Cacho()

            cacho.lista_de_dados[0].pinta = 1  
            cacho.lista_de_dados[1].pinta = 2  
            cacho.lista_de_dados[2].pinta = 2  
            cacho.lista_de_dados[3].pinta = 3  
            cacho.lista_de_dados[4].pinta = 4  

            cachos.append(cacho)

        contador = contador_pintas()
        arbitro = ArbitroRonda(contador)
        resultado = arbitro.determinar_duda(apuesta=(2, 12), jugador_apuesta="Jugador1", jugador_duda="Jugador2", cachos=cachos)
        assert resultado['pierde'] == "Jugador2"

    def test_pierde_el_que_apuesta(self):
        cachos = []
        for _ in range(4):
            cacho = Cacho()

            cacho.lista_de_dados[0].pinta = 1  
            cacho.lista_de_dados[1].pinta = 2  
            cacho.lista_de_dados[2].pinta = 2  
            cacho.lista_de_dados[3].pinta = 3  
            cacho.lista_de_dados[4].pinta = 6  

            cachos.append(cacho)
        
        contador = contador_pintas()
        arbitro = ArbitroRonda(contador)
        resultado = arbitro.determinar_duda(apuesta=(6, 9), jugador_apuesta="Jugador1", jugador_duda="Jugador2", cachos=cachos)
        assert resultado['pierde'] == "Jugador1"

    def test_calzar_correcto(self):
        cachos = []
        for _ in range(4):
            cacho = Cacho()

            cacho.lista_de_dados[0].pinta = 1  
            cacho.lista_de_dados[1].pinta = 2  
            cacho.lista_de_dados[2].pinta = 2  
            cacho.lista_de_dados[3].pinta = 3  
            cacho.lista_de_dados[4].pinta = 4  

            cachos.append(cacho)
        
        contador = contador_pintas()
        arbitro = ArbitroRonda(contador)
        resultado = arbitro.determinar_calza(apuesta=(3, 8), cachos=cachos)
        assert resultado == True

    def test_calzar_incorrecto(self):
        cachos = []
        for _ in range(4):
            cacho = Cacho()

            cacho.lista_de_dados[0].pinta = 1  
            cacho.lista_de_dados[1].pinta = 2  
            cacho.lista_de_dados[2].pinta = 2  
            cacho.lista_de_dados[3].pinta = 3  
            cacho.lista_de_dados[4].pinta = 4  

            cachos.append(cacho)

        contador = contador_pintas()
        arbitro = ArbitroRonda(contador)
        resultado = arbitro.determinar_calza(apuesta=(3, 2),cachos=cachos)
        assert resultado == False

    def test_calzar_invalido_por_cantidad_dados(self):
        cachos = []
        for _ in range(4):
            cacho = Cacho()
            cacho.remover_dado(0)
            cacho.remover_dado(0)
            cacho.remover_dado(0)
            cachos.append(cacho)
        
        contador = contador_pintas()
        arbitro = ArbitroRonda(contador)
        with pytest.raises(Exception):
            arbitro.determinar_calza(apuesta=(3, 2), cachos=cachos)
