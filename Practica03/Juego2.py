import random
class Juego:
    record = 0
    def __init__(self, v):
        self.vidas = v
        self.record = 0

    def reinicia(self):
        self.vidas = 3

    def actuRecord(self):
        Juego.record += 1
        print("Record:", Juego.record)

    def quitaVida(self):
        self.vidas -= 1
        print("Vidas:", self.vidas)
        return self.vidas > 0
    
class JuegoAdivinaNumero(Juego):
    def __init__(self, v):
        super().__init__(v)
        self.numAdivinar = 0

    def validaNumero(self, n): #agregando validacion de numero
        return 0 <= n <= 10

    def juega(self):
        self.reinicia()
        if self.numAdivinar == 0:
            self.numAdivinar = random.randint(0, 10)
            print("Adivina un numero (0-10)")
        while True:
            n = int(input("Numero: "))
            if not self.validaNumero(n):
                print("Numero invalido")
                continue
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
# Juego Par
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def juega(self):
        self.reinicia()
        self.numAdivinar = random.choice([0,2,4,6,8,10])
        super().juega()

# Juego Impar
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def juega(self):
        self.reinicia()
        self.numAdivinar = random.choice([1,3,5,7,9])
        super().juega()

class Aplicacion:
    def main():
        print("=== Juego Normal ===")
        j1 = JuegoAdivinaNumero(3)
        j1.juega()

        print("\n=== Juego Par ===")
        j2 = JuegoAdivinaPar(3)
        j2.juega()

        print("\n=== Juego Impar ===")
        j3 = JuegoAdivinaImpar(3)
        j3.juega()
Aplicacion.main()