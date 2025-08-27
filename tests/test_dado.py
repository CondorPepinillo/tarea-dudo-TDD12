from src.juego.dado import Dado

dado_test = Dado()

def test_tirar_dado():
    assert 1 <= dado_test.tirar_dado() <= 6, "El resultado debe estar entre 1 y 6"

def test_get_pinta(): 
    assert 1 <= dado_test.get_pinta() <= 6, "El resultado debe estar entre 1 y 6"