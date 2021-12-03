import pytest
import pilha



# metodo empilhar
def test_empilhar():
    nova_pilha = pilha.Pilha()
    test = nova_pilha.empilhar(3)
    assert test == 3


# metodo desenpilhar
def test_desempilhar():
    nova_pilha = pilha.Pilha()
    nova_pilha.empilhar(3)
    nova_pilha.empilhar(5)
    nova_pilha.empilhar(10)
    test = nova_pilha.desempilhar()
    assert test == 10



# metodo topo


# tamanho da pilha


# imprimir a pilha completa



# checar se a pilha esta vazia