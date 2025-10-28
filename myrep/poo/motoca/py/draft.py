class Pessoa:
    def __init__(self, name: str, age: int):
        self.__name: str = name
        self.__age: int = age 
    
    def getName(self) -> str:
        return self.__name

    def getAge(self) -> int:
        return self.__age

    def toString(self) -> str: 
        return f"{self.__name}:{self.__age}"

    def __str__(self) -> str:
        return self.toString()

class Motoca:
    def __init__(self):
        self.__potencia: int = 1
        self.__time: int = 0
        self.__pessoa: Pessoa | None = None

    def init(self, potencia: int):
        self.__potencia = potencia
        self.__time = 0
        self.__pessoa = None

    def inserir(self, pessoa: Pessoa) -> bool:
            if self.__pessoa is not None:
                print("fail: busy motorcycle") 
                return False 
            self.__pessoa = pessoa 
            return True 

    def remover(self) -> Pessoa | None:
        if self.__pessoa is None:
            print("fail: empty motorcycle")
            return None
        pessoa_removida = self.__pessoa
        self.__pessoa = None 
        return pessoa_removida

    def buyTime(self, time: int):
        self.__time += time

    def drive (self, time: int):
        if self.__time == 0:
            print("fail: buy time first")
            return
        if self.__pessoa is None: 
            print("fail: empty motorcycle")
            return
        if self.__pessoa.getAge() > 10:
            print("fail: too old to drive")
            return

        if time >= self.__time:
            print(f"fail: time finished after {self.__time} minutes")
            self.__time = 0
        else: 
            self.__time -= time

    def honk(self) -> str:
        return "P" + ("e" * self.__potencia) + "m"

    def toString(self) -> str:
        person_str = "(empty)"
        if self.__pessoa is not None:
            person_str = f"({self.__pessoa.toString()})"
        return f"power:{self.__potencia}, time:{self.__time}, person:{person_str}"

    def __str__(self) -> str:
        return self.toString()


def main():
    moto = Motoca()
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

            elif cmd == "init":
                moto.init(int(ui[1]))

            elif cmd == "show":
                print(moto.toString())

            elif cmd == "enter":
                pessoa = Pessoa(ui[1], int(ui[2]))
                moto.inserir(pessoa)

            elif cmd == "leave":
                pessoa_removida = moto.remover()
                if pessoa_removida is not None:
                    print(pessoa_removida.toString())
            
            elif cmd == "buy":
                moto.buyTime(int(ui[1]))

            elif cmd == "drive":
                moto.drive(int(ui[1]))

            elif cmd == "honk":
                print(moto.honk())

            else:
                print("fail: unknown command")

        except EOFError:
            break
        except Exception as e: 
            print(f"fail: processing error: {e}")
        
if __name__ == "__main__":
    main()