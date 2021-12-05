from pytest import fixture
import pytest
import pilha

@fixture
def nova_pilha():
    pilha_test = pilha.Pilha()
    yield pilha_test
    

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
    nova_pilha.esvaziar_pilha()
    nova_pilha.imprimir_pilha()
    assert test == 10



# metodo topo


# tamanho da pilha


# imprimir a pilha completa
def test_imprimir_pilha(nova_pilha):
    nova_pilha.empilhar(1)
    nova_pilha.empilhar(2)
    nova_pilha.empilhar(3)
    nova_pilha.empilhar(4)
    test = nova_pilha.imprimir_pilha()
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
    
