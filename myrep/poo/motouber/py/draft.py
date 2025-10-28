class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self.__nome: str = nome
        self.__dinheiro: int = dinheiro
    
    def getNome(self) -> str:
        return self.__nome

    def getDinheiro(self) -> int:
        return self.__dinheiro

    def receber(self, valor:int):
        self.__dinheiro += valor 

    def pagar(self, valor) -> int:
        if self.__dinheiro < valor:
             print("fail: Passenger does not have enough money")
             valor_pago = self.__dinheiro
             self.__dinheiro = 0
             return valor_pago
        self.__dinheiro -= valor
        return valor 

    def toString(self) -> str:
        return f"{self.__nome}:{self.__dinheiro}"

    def __str__(self) -> str:
        return self.toString()

class Moto:
    def __init__(self):
        self.__custo: int = 0
        self.__motorista: Pessoa | None = None 
        self.__passageiro: Pessoa | None = None

    def setDriver(self, motorista: Pessoa):
        self.__motorista = motorista 

    def setPass(self, passageiro: Pessoa):
        if self.__motorista is None:
            print("fail: No driver on the bike")
            return

        if self.__passageiro is not None:
            print("fail: Already a passenger on the bike")
            return
        self.__passageiro = passageiro
        self.__custo = 0

    def drive(self, km: int):
        if self.__motorista is None: 
            print("fail: No driver on the bike")
            return 

        if self.__passageiro is None: 
            print("fail: No passenger on the bike")
            return

        self.__custo += km

    def leavePass(self):
        if self.__passageiro is None: 
            print("fail: No passenger to leave")
            return
        valor_pago = self.__passageiro.pagar(self.__custo)
        self.__motorista.receber(self.__custo)
        passageiro_final = self.__passageiro.toString()
        print(f"{passageiro_final} left")
        self.__passageiro = None
        self.__custo = 0

    def toString(self) -> str:
        driver_str = str(self.__motorista) if self.__motorista  else "None"
        pass_str = str(self.__passageiro) if self.__passageiro else "None"
        return f"Cost: {self.__custo}, Driver: {driver_str}, Passenger: {pass_str}"

    def __str__(self) -> str: 
        return self.toString()

def main():
    moto = Moto()
    while True:
        try:
            line = input().strip()
            if line == "":
                continue

            print(f"${line}")
            ui = line.split()
            cmd = ui[0]

            if cmd == "end":
                break 
            
            elif cmd == "show":
                print(moto)

            elif cmd == "setDriver":
                moto.setDriver(Pessoa(ui[1], int(ui[2])))

            elif cmd == "setPass":
                moto.setPass(Pessoa(ui[1], int(ui[2]))) 

            elif cmd == "drive":
                moto.drive(int(ui[1]))
            
            elif cmd == "leavePass":
                moto.leavePass()
            
            else: 
                print(f"fail: unknown command {cmd}")

        except EOFError:
            break
        except Exception as e:
            print(f"fail: processing error: {e}")


main()
