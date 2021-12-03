class Pilha:
    vazia = True
    pilha_conteudo = []

    def __init__(self, ):
        pass

    def empilhar(self, item):
        if self.vazia == True:
            self.vazia = False
        self.pilha_conteudo.append(item)
        return item

    def desempilhar(self):
        desempilhado = self.pilha_conteudo.pop()
        return desempilhado