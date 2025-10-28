import sys
from typing import Optional

class Lead: 
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness: float = thickness
        self.__hardness: str = hardness
        self.__size: int = size

    def getThickness(self) -> float:
        return self.__thickness

    def getSize(self) -> int:
        return self.__size
    
    def setSize(self, new_size: int):
        self.__size = new_size

    def getHardness(self) -> str:
        return self.__hardness

    def usagePerSheet(self) -> int:
        if self.__hardness == "HB":
            return 1
        elif self.__hardness == "2B":
            return 2
        elif self.__hardness == "4B":
            return 4
        elif self.__hardness == "6B":
            return 6
        return 0

    def toString(self) -> str:
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"

    def __str__(self) -> str:
        return self.toString()

class Pencil:
    def __init__(self):
        self.__thickness: float = 0.0
        self.__tip: Optional[Lead] = None 

    def init(self, thickness: float) -> bool:
        self.__thickness = thickness
        self.__tip = None
        return True

    def hasGrafite(self) -> bool:
        return self.__tip is not None

    def insert(self, lead: Lead) -> bool:
        if lead.getThickness() != self.__thickness:
            print("fail: calibre incompativel")
            return False

        if self.hasGrafite():
            print("fail: ja existe grafite")
            return False

        self.__tip = lead
        return True

    def remove(self) -> Optional[Lead]:
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return None

        remove_lead = self.__tip
        self.__tip = None
        return remove_lead

    def writePage(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return

        if self.__tip.getSize() <= 10:
            print("fail: tamanho insuficiente")
            return

        usage = self.__tip.usagePerSheet()
        final_size = self.__tip.getSize() - usage

        if final_size < 10:
            self.__tip.setSize(10)
            print("fail: folha incompleta")
        else:
            self.__tip.setSize(final_size)

    def toString(self) -> str:
        tip_str = "null"
        if self.hasGrafite():
            tip_str = self.__tip.toString()
        return f"calibre: {self.__thickness}, grafite: {tip_str}"

    def __str__(self) -> str: 
        return self.toString()

def main():
    pencil = Pencil()
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
                pencil.init(float(ui[1]))
            elif cmd == "insert":
                lead = Lead(float(ui[1]), ui[2], int(ui[3]))
                pencil.insert(lead)
            elif cmd == "remove":
                pencil.remove()
            elif cmd == "write":
                pencil.writePage()
            elif cmd == "show":
                print(pencil.toString())
            else:
                print(f"fail: unknown command {cmd}")

        except EOFError: 
            break
        except Exception as e: 
            print(f"fail: processing error: {e}", file = sys.stderr)

if __name__ == "__main__":
    main()
            