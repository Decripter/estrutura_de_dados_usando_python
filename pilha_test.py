from pytest import fixture
import pytest
import pilha

@fixture
def nova_pilha():
    pilha_test = pilha.Pilha()
    yield pilha_test

@fixture
def pilha_empilhada():
    pilha_test = pilha.Pilha()
    pilha_test.empilhar(1)
    pilha_test.empilhar(2)
    pilha_test.empilhar(3)
    pilha_test.empilhar(4)
    return pilha_test

# metodo empilhar
def test_empilhar(nova_pilha):
    test = nova_pilha.empilhar(3)
    assert test == 3


# metodo desenpilhar
def test_desempilhar(nova_pilha):
    nova_pilha.empilhar(3)
    nova_pilha.empilhar(5)
    nova_pilha.empilhar(10)
    test = nova_pilha.desempilhar()
    assert test == 10



# metodo topo
def test_verificar_topo(nova_pilha):
    nova_pilha.empilhar(5)
    nova_pilha.empilhar(4)
    test = nova_pilha.retorna_topo()
    assert test == 4


# tamanho da pilha
def test_verificar_tamanho_da_pilha(pilha_empilhada):
    test = pilha_empilhada.verificar_tamanho()
    assert test == 4


# imprimir a pilha completa
def test_imprimir_pilha(pilha_empilhada):
    test = pilha_empilhada.imprimir_pilha()
    esperado = [4, 3, 2, 1]
    assert test == esperado


# checar se a pilha esta vazia

def test_pilha_vazia(nova_pilha):
    assert nova_pilha.vazia == True

def test_pilha_nao_vazia(nova_pilha):
    nova_pilha.empilhar(2)
    test = nova_pilha.vazia
    assert test == False

def test_pilha_desempilhar_deixando_vazia(nova_pilha):
    nova_pilha.empilhar(2)
    nova_pilha.desempilhar()
    test = nova_pilha.vazia
    assert test == True
    
