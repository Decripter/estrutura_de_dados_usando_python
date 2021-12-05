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
        ...

    def mostrar_tamanho_da_fila(self):
        ...

    def limpar_fila(self):
        ...
