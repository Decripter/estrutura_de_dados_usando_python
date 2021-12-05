class Fila:

    def __init__(self):
        self.fila_conteudo = []
        self.fila_vazia = True

    def enfileirar(self, item):
        self.fila_conteudo.append(item)

    def desenfileirar(self):
        desenfileirado = self.fila_conteudo.pop(0)
        return desenfileirado

    def mostrar_inicio_da_fila(self):
        return self.fila_conteudo[0]

    def mostrar_tamanho_da_fila(self):
        tamanho = len(self.fila_conteudo)
        return tamanho

    def limpar_fila(self):
        ...
