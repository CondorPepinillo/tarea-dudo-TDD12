class ArbitroRonda:
    def __init__(self, contador_pintas):
        self.contador_pintas = contador_pintas

    def determinar_duda(self, apuesta, jugador_apuesta, jugador_duda):
        cantidad, pinta = apuesta
        cantidad_real = self.contador_pintas.contar(pinta)
        if cantidad_real >= cantidad:
            return {'pierde': jugador_duda, 'cantidad_real': cantidad_real}
        else:
            return {'pierde': jugador_apuesta, 'cantidad_real': cantidad_real}

    def determinar_calza(self, apuesta, jugador_calza, dados_en_juego, cant_jugadores): 
        if dados_en_juego < (cant_jugadores * 5) // 2:
            raise Exception("Calzar no es válido en esta situación")

        cantidad, pinta = apuesta
        cantidad_real = self.contador_pintas.contar(pinta)
        if cantidad_real == cantidad:
            return True
        else:
            return False
