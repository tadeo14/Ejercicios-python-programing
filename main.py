
import mimodulo


print("Bienvenidos al programa")


mimodulo.saludar()

r = mimodulo.sumar(10,20)
print("El resultado es:",r)

obj = mimodulo.Fabrica()

print(obj.tipo)

obj.picar()