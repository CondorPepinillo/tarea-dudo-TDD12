import math
class validador_apuestas:
    def __init__(self):
        self.ronda_especial = False ## asuminos que no estamos en una ronda  de un 1 dado

    def cambiar_a_ases(self,num):
        if num % 2 == 0:
            return (num // 2) + 1
        else:
            return math.ceil(num / 2)

    def reglas_normales(self,apuesta_nueva, apuesta_actual):
        if apuesta_nueva[0] < apuesta_actual[0]:### si la pinta es menor
            return False
        elif apuesta_nueva[0] == apuesta_actual[0] and apuesta_nueva[1] <= apuesta_actual[1]:### si la pinta es igual pero la cantidad es menor o igual
            return False
        else:
            return True### si la pinta es mayor o la cantidad es mayor
            

    def pintura_valida(self,p):
        if p < 1 or p > 6:
            raise ValueError("Pinta debe estar entre 1 y 6.")
        return p
    



    def validar_apuesta(self, apuesta_nueva, apuesta_actual):### debemos asumir que las apuestas vienen en formato (pinta, cantidad)
        nombres = {1: "As", 2: "Tonto", 3: "Tren", 4: "Cuadra", 5: "Quina", 6: "Sexto"}
        if not self.ronda_especial:
            if apuesta_nueva[0] == 1 and apuesta_actual[0] != 1:### si la nueva pinta es un 1 y la actual no
                return apuesta_nueva[1] >= self.cambiar_a_ases(apuesta_actual[1])
            elif apuesta_nueva[0] != 1 and apuesta_actual[0] == 1:### si la nueva pinta no es un 1 y la actual si
                return apuesta_nueva[1] >= (apuesta_actual[1] * 2) + 1
            else:
                return self.reglas_normales(apuesta_nueva, apuesta_actual)
        else:
            return self.reglas_normales(apuesta_nueva, apuesta_actual)
        

    def iniciar_ronda_especial(self):
        self.ronda_especial = True

    def finalizar_ronda_especial(self):
        self.ronda_especial = False 