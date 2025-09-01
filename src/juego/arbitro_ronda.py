class ArbitroRonda:
    def __init__(self, contador_pintas):
        self.contador_pintas = contador_pintas

    def determinar_duda(self, apuesta, jugador_apuesta, jugador_duda, cachos):
        pinta, cantidad = apuesta
        cantidad_real = 0

        for cacho in cachos:
            cacho.lista_de_dados = cacho.lista_de_dados[0:5]
            conteo = self.contador_pintas.contar_pintas(cacho, apuesta)
            nombres = {1: "As", 2: "Tonto", 3: "Tren", 4: "Cuadra", 5: "Quina", 6: "Sexto"}
            pinta_nombre = nombres[pinta]  

            if pinta_nombre in conteo:
                cantidad_real += conteo[pinta_nombre]

        if cantidad_real >= cantidad:
            return {'pierde': jugador_duda, 'cantidad_real': cantidad_real}
        else:
            return {'pierde': jugador_apuesta, 'cantidad_real': cantidad_real}

    def determinar_calza(self, cachos, apuesta, jugador_apuesta=None): 
        dados_en_juego = sum(len(cacho.get_lista_de_dados()) for cacho in cachos)
        cant_jugadores = len(cachos)
        if dados_en_juego < (cant_jugadores * 5) // 2:
            raise Exception("Calzar no es válido en esta situación")
        
        pinta, cantidad = apuesta
        cantidad_real = 0

        for cacho in cachos:
            cacho.lista_de_dados = cacho.lista_de_dados[0:5]
            conteo = self.contador_pintas.contar_pintas(cacho, apuesta)
            nombres = {1: "As", 2: "Tonto", 3: "Tren", 4: "Cuadra", 5: "Quina", 6: "Sexto"}
            pinta_nombre = nombres[pinta]
            
            if pinta_nombre in conteo:
                cantidad_real += conteo[pinta_nombre]
           
        if cantidad_real == cantidad:
            return True
        else:
            return False
