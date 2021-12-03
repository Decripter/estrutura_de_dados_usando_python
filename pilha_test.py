import pytest
import pilha



# metodo empilhar
def test_empilhar():
    nova_pilha = pilha.Pilha()
    test = nova_pilha.empilhar(3)
    del(nova_pilha)
    assert test == 3


# metodo desenpilhar
def test_desempilhar():
    nova_pilha = pilha.Pilha()
    nova_pilha.empilhar(3)
    nova_pilha.empilhar(5)
    nova_pilha.empilhar(10)
    test = nova_pilha.desempilhar()
    del(nova_pilha)
    assert test == 10



# metodo topo


# tamanho da pilha


# imprimir a pilha completa



# checar se a pilha esta vazia



def test_pilha_vazia():
    nova_pilha = pilha.Pilha()
    assert nova_pilha.vazia == True

def test_pilha_nao_vazia():
    nova_pilha = pilha.Pilha()
    nova_pilha.empilhar(2)
    test = nova_pilha.vazia
    del(nova_pilha)
    assert test == False

def test_pilha_desempilhar_deixando_vazia():
    nova_pilha = pilha.Pilha()
    nova_pilha.empilhar(2)
    nova_pilha.desempilhar()
    test = nova_pilha.vazia
    del(nova_pilha)
    assert test == False
    