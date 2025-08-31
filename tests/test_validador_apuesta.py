import pytest
import sys
sys.path.append("src")
from juego.validador_apuestas import validador_apuestas

@pytest.fixture
def validador():
    return validador_apuestas()

## casos normales normal-normal
def test_apuesta_valida_cantidad(validador):
    actual = (2,3) ### formato (pinta, cantidad)
    apuesta = (2,4)
    resultado = validador.validar_apuesta(apuesta, actual)
    assert resultado == True

def test_apuesta_invalida_cantidad(validador):
    actual = (2,3) ### formato (pinta, cantidad)
    apuesta = (2,2)
    resultado = validador.validar_apuesta(apuesta, actual)
    assert resultado == False

def test_apuesta_valida_pinta(validador):
    actual = (2,3) ### formato (pinta, cantidad)
    apuesta = (3,1)
    resultado = validador.validar_apuesta(apuesta, actual)
    assert resultado == True

def test_apuesta_invalida_pinta(validador):
    actual = (4,3) ### formato (pinta, cantidad)
    apuesta = (3,3)
    resultado = validador.validar_apuesta(apuesta, actual)
    assert resultado == False

## caso especial de los As-normal
def test_apuesta_valida_as_a_normal(validador):
    actual = (1,3)
    apuesta = (2,7)
    resultado = validador.validar_apuesta(apuesta, actual)
    assert resultado == True

def test_apuesta_invalida_as_a_normal(validador):
    actual = (1,3)
    apuesta = (2,6)
    resultado = validador.validar_apuesta(apuesta, actual)
    assert resultado == False

### casos normales normal-As###
def test_apuesta_valida_normal_a_as(validador):
    actual =  (3,5)
    apuesta = (1,3)
    resultado = validador.validar_apuesta(apuesta, actual)
    assert resultado == True

def test_apuesta_invalida_normal_a_as(validador):
    actual =  (3,5)
    apuesta = (1,2)
    resultado = validador.validar_apuesta(apuesta, actual)
    assert resultado == False

### casos especiales As-As
def test_apuesta_valida_as_a_as(validador):
    actual = (1,4)
    apuesta = (1,5)
    resultado = validador.validar_apuesta(apuesta, actual)
    assert resultado == True

def test_apuesta_invalida_as_a_as(validador):
    actual = (1,4)
    apuesta = (1,3)
    resultado = validador.validar_apuesta(apuesta, actual)
    assert resultado == False


