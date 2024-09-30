
class ClaseA:
    def __init__(self):
        self.a = 1
    
    def saludar (self):
        print("Hola soy ClaseB")

class ClaseB (ClaseA):
    def __init__(self):
        super().__init__()
        self.b = 2
    


mi_objeto = ClaseB()
print(mi_objeto.a)
print(mi_objeto.b)

mi_objeto.saludar()