import random

class Dado:
    pinta = random.randint(1, 6) #un dado aunque no haya sido tirado siempre tendra ya una pinta, no hay un dado neutro

    def __init__(self):
        self.valor = None

    def tirar_dado(self): 
        self.pinta = random.randint(1, 6)
        return self.pinta   
    
    def get_pinta(self):
        return self.pinta

#main_dado = Dado()
#main_dado.tirar_dado()
