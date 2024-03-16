class Passaro:
    def voar(self):
        print("Voando...")

    def emitir_som(self):
        print("Emitindo som...")


class Pato(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print("Quack quack")


class Pardal(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print("Piu piu")


pato = Pato()
print("Pato")
pato.voar()
print ("Pato emitindo som...")
pato.emitir_som()


pardal = Pardal()
print("Pardal")
pardal.voar()
print ("Pardal emitindo som...")
pardal.emitir_som()
