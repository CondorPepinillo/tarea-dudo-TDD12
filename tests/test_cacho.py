from src.juego.cacho import Cacho


cacho_test = Cacho()

def test_revisar_cacho():
    dados = cacho_test.revisar_cacho()
    assert all(1 <= i <= 6 for i in dados), "Todos los resultados deben estar entre 1 y 6"

def test_agitar_cacho():
    previous_dados = cacho_test.revisar_cacho()
    cacho_test.agitar_cacho()
    new_dados = cacho_test.revisar_cacho()
    assert previous_dados != new_dados, "Los resultados deben cambiar después de agitar el cacho"

def test_remover_dado():
    initial_count = len(cacho_test.lista_de_dados)
    cacho_test.remover_dado(0)
    assert len(cacho_test.lista_de_dados) == initial_count - 1, "El cacho debe tener un dado menos después de remover uno"