from src.juego.gestor_partida import GestorPartida

class TestGestorPartida:
    def test_agregar_jugadores(self):
        gestor = GestorPartida(["A", "B", "C"])
        jugadores = gestor.get_jugadores()
    
        assert len(jugadores) == 3
        assert all(len(jugador['cacho'].get_lista_de_dados()) == 5 for jugador in jugadores)

    def test_decidir_inicial(self):
        gestor = GestorPartida(["A", "B", "C"])
        inicial = gestor.decidir_inicial()['nombre']

        assert inicial in ["A", "B", "C"]

    def test_flujo_turnos(self):
        gestor = GestorPartida(["A", "B", "C"])

        actual = gestor.get_turno_actual()['nombre']
        siguiente = gestor.siguiente_turno()['nombre']
        assert siguiente != actual

        gestor = GestorPartida(["A", "B", "C"])
        actual = gestor.get_turno_actual()['nombre']

        for _ in range(len(gestor.get_jugadores())):
            gestor.siguiente_turno()
        assert gestor.get_turno_actual()['nombre'] == actual

    def test_ronda_especial(self):
        gestor = GestorPartida(["A", "B", "C"])
        jugador = gestor.get_jugadores()[0]
        jugador["cacho"].lista_de_dados = [1]

        assert gestor.ronda_especial() == True

    def test_validar_apuesta(self):
        gestor = GestorPartida(["A", "B"])

        # sube cantidad
        assert gestor.validar_apuesta(apuesta_actual=(2, 3), apuesta_nueva=(3,3)) == True
        # sube pinta
        assert gestor.validar_apuesta((1, 2), (1,3)) == True
        # apuesta no valida
        assert gestor.validar_apuesta((1,2), (1,3)) == False

    def test_validar_apuesta_caso_ases(self):
        gestor = GestorPartida(["A", "B"])

        # baja a la mitad 
        assert gestor.validar_apuesta((5, 3), (3, 1)) == True
        assert gestor.validar_apuesta((6, 6), (4, 1)) == True

        # baja a menos de la mitad
        assert gestor.validar_apuesta((5,3), (2, 1)) == False

        # sube de ases
        assert gestor.validar_apuesta((2, 1), (5,4)) == True

        # subida de pinta no valida
        assert gestor.validar_apuesta((2,1), (4,4)) == False