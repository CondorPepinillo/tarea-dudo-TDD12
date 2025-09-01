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
