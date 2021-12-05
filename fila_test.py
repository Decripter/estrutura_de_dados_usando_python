from pytest import fixture
import pytest
import fila

obj_fila =fila.Fila

@fixture
def nova_fila():
    fila_test = obj_fila()
    yield fila_test

@fixture
def fila_preenchida():
    fila_test = obj_fila()
    fila_test.enfileirar(1)
    fila_test.enfileirar(2)
    fila_test.enfileirar(3)
    fila_test.enfileirar(4)
    fila_test.enfileirar(5)
    yield fila_test

def test_enfileirar(nova_fila):
    nova_fila.enfileirar(1)
    nova_fila.enfileirar(2)
    nova_fila.enfileirar(3)
    test = nova_fila.fila_conteudo
    assert test == [1, 2, 3]

def test_desenfileirar(fila_preenchida):
    test = fila_preenchida.desenfileirar()
    assert test == 1

def test_mostrar_inicio_fila(fila_preenchida):
    test = fila_preenchida.mostrar_inicio_da_fila()
    assert test == 1

def test_mostra_tamanho_da_fila(fila_preenchida):
    test = fila_preenchida.mostrar_tamanho_da_fila()
    assert test == 5