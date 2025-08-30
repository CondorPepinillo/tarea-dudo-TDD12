from src.juego.dado import Dado

class Cacho:
    lista_de_dados = []
    def __init__(self):
        for i in range(5):
            self.lista_de_dados.append(Dado())
            self.lista_de_dados[i].tirar_dado()

    def agitar_cacho(self):
        for i in range(len(self.lista_de_dados)):
            self.lista_de_dados[i].tirar_dado()

    def revisar_cacho(self):
        for i in range(len(self.lista_de_dados)):
            match self.lista_de_dados[i].get_pinta():
                case 1:
                    print(f"Dado {i+1}: {self.lista_de_dados[i].get_pinta()} As")
                case 2:
                    print(f"Dado {i+1}: {self.lista_de_dados[i].get_pinta()} Tonto")
                case 3:
                    print(f"Dado {i+1}: {self.lista_de_dados[i].get_pinta()} Tren")
                case 4:
                    print(f"Dado {i+1}: {self.lista_de_dados[i].get_pinta()} Cuadra")
                case 5:
                    print(f"Dado {i+1}: {self.lista_de_dados[i].get_pinta()} Quina")
                case 6:
                    print(f"Dado {i+1}: {self.lista_de_dados[i].get_pinta()} Sexto")
        return [self.lista_de_dados[i].get_pinta() for i in range(len(self.lista_de_dados))]
    
    def remover_dado(self, posicion):
        self.lista_de_dados.pop(posicion)
    
    def get_lista_de_dados(self):
        return self.lista_de_dados


   
    
