class Charger:
    def __init__(self, potencia: int):
        self.__potencia: int = potencia
    
    def getPotencia(self) -> int:
        return self.__potencia

    def toString(self) -> str:
        return f"{self.__potencia}W"

    def __str__(self) -> str:
        return self.toString()

class Battery:
    def __init__(self, capacidade: int):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

    def getCarga(self) -> int: 
        return self.__carga

    def getCapacidade(self) -> int: 
        return self.__capacidade

    def charge(self, valor: int):
        self.__carga += valor
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade

    def discharge(self, valor: int) -> bool:
        if self.__carga == 0:
            return True
        self.__carga -= valor
        if self.__carga <= 0:
            self.__carga = 0
            return True
        return False

    def toString(self) -> str:
        return f"{self.__carga}/{self.__capacidade}"

    def __str__(self) -> str:
        return self.toString()

class Notebook:
    def __init__(self):
        self.__ligado: bool = False
        self.__tempo_uso: int = 0
        self.__carregador: Charger | None = None
        self.__bateria: Battery | None = None 

    def set_charger(self, potencia: int):
        if self.__carregador is not None:
            print("fail: careggador já conectado")
            return
        self.__carregador = Charger(potencia)

    def rm_charger(self):
        if self.__carregador is None:
            print("fail: Sem carregador")
            return 
        print(f"Removido {self.__carregador.toString()}")
        self.__carregador = None
        if self.__ligado:
            if self.__bateria is None or self.__bateria.getCarga() == 0:
                self.turn_off()

    def set_battery(self, capacidade: int):
        if self.__bateria is not None:
            print("fail: bateria já conectada")
            return
        self.__bateria = Battery(capacidade)

    def rm_battery(self):
        if self.__bateria is None: 
            print("fail: Sem bateria")
            return 
        print(f"Removido {self.__bateria.toString()}")
        self.__bateria = None
        if self.__ligado:
            if self.__carregador is None: 
                self.turn_off()

    def turn_on(self):
        if self.__ligado:
            return
        tem_carregador = self.__carregador is not None
        tem_bateria = (self.__bateria is not None and self.__bateria.getCarga() > 0)
        if tem_carregador or tem_bateria:
            self.__ligado = True
            self.__tempo_uso = 0
        else: 
            print("fail: não foi possível ligar")

    def turn_off(self):
        self.__ligado = False 

    def use(self, tempo: int):
        if not self.__ligado:
            print("fail: desligado")
            return
        self.__tempo_uso += tempo
        tem_carregador = self.__carregador is not None
        tem_bateria = self.__bateria is not None

        if tem_bateria and tem_carregador:
            potencia = self.__carregador.getPotencia()
            self.__bateria.charge(potencia * tempo)

        elif tem_bateria:
            descarregou = self.__bateria.discharge(tempo)
            if descarregou:
                print("fail: descarregou")
                self.turn_off()

        elif tem_carregador:
            pass

    def show(self) -> str:
        if not self.__ligado:
            status = "Notebook: desligado"
        else:
            status = f"Notebook: ligado por {self.__tempo_uso} min"

        if self.__carregador is not None:
            status += f", Bateria {self.__bateria.toString()}"
        return status

    def __str__(self) -> str:
        return self.show()

def main():
    nb = Notebook ()
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
                print(nb.show())
            elif cmd == "turn_on":
                nb.turn_on()
            elif cmd == "turn_off":
                nb.turn_off()
            elif cmd == "use":
                nb.use(int(ui[1]))
            elif cmd == "set_charger":
                nb.set_charger(int(ui[1]))
            elif cmd == "rm_charger":
                nb.rm_charger()
            elif cmd == "set_battery":
                nb.set_battery(int(ui[1]))
            elif cmd == "rm_battery":
                nb.rm_battery()
            else: 
                print (f"fail: unknown command {cmd}")

        except EOFError:
            break
        except Exception as e:
            print(f"fail: processing error: {e}")

if __name__ == "__main__":
    main()    
