import random
class Juego:
    def __init__(self, v):
        self.vidas = v
        self.record = 0

    def reinicia(self):
        self.vidas = 3

    def actuRecord(self):
        self.record += 1
        print("Record:", self.record)

    def quitaVida(self):
        self.vidas -= 1
        print("Vidas:", self.vidas)
        return self.vidas > 0
    
class JuegoAdivinaNumero(Juego):
    def __init__(self, v):
        super().__init__(v)
        self.numAdivinar = 0

    def juega(self):
        self.reinicia()
        self.numAdivinar = random.randint(0, 10)
        print("Adivina un numero (0-10)")
        while True:
            n = int(input("Numero: "))
            if n == self.numAdivinar:
                print("Acertaste!!")
                self.actuRecord()
                break
            else:
                if self.quitaVida():

                    if n < self.numAdivinar:
                        print("Mayor")
                    else:
                        print("Menor")
                else:
                    print("Perdiste!! Era:", self.numAdivinar)
                    break
class Aplicacion:
    def main():
        print("=== Juego Normal ===")
        j = JuegoAdivinaNumero(3)
        j.juega()
Aplicacion.main()