class Pilha:

# os atributos foram movidos para __init__
# fora do metodo init eles estavam gerando um problema durante os testes,
# os atributos nao estavam sendo resetados e estavam passando de um teste para o outro
# isso significa que os atributos estavam sendo cmpartilhados pelos objetos
# já que os atributos nao tinham o parametro self eles na sao compartilhados por todos
# os objetos criados a partir desta classe.

    def __init__(self, ):
        # movendo os atributos para dentro do metodo __init__ pois aqui eles sao atribuidos com o self que associa 
        # o o atributo a cada instancia da classe
        self.vazia = True
        self.pilha_conteudo = []


    def empilhar(self, item):
        if self.vazia == True:
            self.vazia = False
        head_list = [item]
        tail_list = self.pilha_conteudo.copy()
        self.pilha_conteudo=head_list+tail_list
        return item

    def desempilhar(self):
        if self.vazia == False:
            desempilhado = self.pilha_conteudo.pop(0)
            if len(self.pilha_conteudo) == 0:
                self.vazia = True
            return desempilhado
    
    def imprimir_pilha(self):
        return self.pilha_conteudo

    def esvaziar_pilha(self):
        self.vazia = True
        self.pilha_conteudo = []

