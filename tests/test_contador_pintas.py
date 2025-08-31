import pytest
import sys
sys.path.append("src")
from juego.contador_pintas import contador_pintas


@pytest.fixture
def contador():
    return contador_pintas()


def test_contar_pintas_con_valores(contador,mocker): ## debemnos usar mock para controalar los valores de los dados
    from src.juego.dado import Dado
    from src.juego.cacho import Cacho
    dados_fijos = [1, 2, 2, 3, 3, 3]
    mock_dados_lista = []
    for pinta in dados_fijos:
        mock_dado = mocker.Mock(spec=Dado)
        mock_dado.get_pinta.return_value = pinta
        mock_dados_lista.append(mock_dado)
    mock_cacho = mocker.Mock(spec=Cacho)
    mock_cacho.get_lista_de_dados.return_value = mock_dados_lista
    apuesta_actual = (2, 4)  # Apuesta actual (pinta, cantidad)
    resultado = contador.contar_pintas(mock_cacho,apuesta_actual)
    assert resultado == {'Tonto': 3, 'Tren': 3} 
    





def test_es_ronda_especial_inicial(contador):
    assert not contador.es_ronda_especial() # Debería ser False inicialmente

def test_activar_ronda_especial(contador):
    contador.activar_ronda_especial()
    assert contador.es_ronda_especial() # Debería ser True después de activar






