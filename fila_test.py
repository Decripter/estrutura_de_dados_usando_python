from pytest import fixture
import pytest
import fila

obj_fila =fila.Fila

@fixture
def nova_fila():
    fila_test = obj_fila()
    yield fila_test

def fila_preenchida():
    fila_test = obj_fila()
    fila_test.enfileirar(1)
    fila_test.enfileirar(2)
    fila_test.enfileirar(3)
    fila_test.enfileirar(4)
    fila_test.enfileirar(5)
    yield fila_test

def test_preencher_fila(nova_fila):
    nova_fila.enfileirar(1)
    nova_fila.enfileirar(2)
    nova_fila.enfileirar(3)
    test = nova_fila.fila_conteudo
    assert test == [1, 2, 3]