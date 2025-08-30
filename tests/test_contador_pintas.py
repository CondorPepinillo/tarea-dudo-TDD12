import pytest
import sys
sys.path.append("src")
from juego.contador_pintas import contador_pintas


@pytest.fixture
def contador():
    return contador_pintas()



def test_contar_pintas_vacio(contador):
    dado = []
    resultado = contador.contar_pintas(dado)
    assert resultado == {}

def test_contar_pintas_con_valores(contador):
    dado = [1, 2, 2, 3, 3, 3]
    resultado = contador.contar_pintas(dado)
    assert resultado == {1: 1, 2: 2, 3: 3}

def test_es_ronda_especial_inicial(contador):
    assert not contador.es_ronda_especial() # Debería ser False inicialmente

def test_activar_ronda_especial(contador):
    contador.activar_ronda_especial()
    assert contador.es_ronda_especial() # Debería ser True después de activar






