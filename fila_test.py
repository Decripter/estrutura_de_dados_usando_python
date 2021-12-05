from pytest import fixture
import pytest
import fila

fila_obj = fila.Fila

@fixture
def nova_fila():
    fila_test = fila_obj()
    yield fila_test

def fila_preenchida():
    fila_test = fila_obj()
    fila_test.enfileirar(1)
    fila_test.enfileirar(2)
    fila_test.enfileirar(3)
    fila_test.enfileirar(4)
    fila_test.enfileirar(5)
    
    yield fila_test