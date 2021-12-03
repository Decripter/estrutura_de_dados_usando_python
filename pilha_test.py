import pytest
import pilha


def test_pilha():
    pilha1 = pilha.Pilha(2)
    assert pilha1.tamanho == 3