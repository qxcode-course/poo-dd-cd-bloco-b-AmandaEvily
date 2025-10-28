class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor: int):
        if valor <= 20 or valor >= 50:
            print ("fail: tamanho fora do intervalo permitido")
        elif valor % 2 != 0:
            print ("fail: o tamanho deve sert um número par")
        else:
            self.__tamanho = valor 
            print ("tamanho definido com sucesso")

chinela = Chinela()
while chinela.getTamanho() == 0
    print("Digite seu tamanho de chinela")
    tamanho = int(input())

    chinela.setTamanho(tamanho)

print("Parabens, você comprou uma chinela tamanho", chinela.getTamanho())



class Pessoa:
    def __init__(self, nome:str):
        self.__nome = nome
    def get_nome


class Moto:
    def __init__(self): #type union
        self.cliente: Pessoa | None = None

    def inserir(self, cliente: Pessoa):
        if self.cliente != None:
            print("moto ocupada")
            return False
        self.cliente = cliente 
        return True

    def remover(self) -> Pessoa | None:
        if self.cliente == None:
            print("moto vazia")
            return None
        aux = self.cliente
        self.cliente = None
        return aux

    def __str__(self):
        return f"moto: {self.cliente}"

moto = Moto()
jose = Pessoa("jose")
moto.inserir(jose)
saiu = moto.remover()
print(saiu == jose) # True

