from DataSet import DataSet
from SLR import SLR
from MateDiscreta import MateDiscreta
from QR import QR
from CR import CR
#Arreglo de datos para el Data Set
x = [108,115,106,97,95,91,97,83,83,78,54,67,56,53,61,115,81,78,30,45,99,32,25,28,90,89]
y  = [95,96,95,97,93,94,95,93,92,86,73,80,65,69,77,96,87,89,60,63,95,61,55,56,94,93]
#Ejemplo cuadratica
#x = [0,1,2,3]
#y = [1,3,2,0]
#Ejemplo de cubica
#x = [-2,-1,0,1,2]
#y = [3,0,2,4,4]
#Se crea el objeto de DataSet con los datos del arreglo
datos = DataSet(x,y)
#Creamos nuestra clase de SLR
lineal = SLR(datos.get_x(),datos.get_y())
nuevo = MateDiscreta(x,y)
cuadratica = QR(x,y)
cubica = CR(x,y)
cuadratica.imprimir_ecuacion()
cubica.imprimir_ecuacion()
print("Regresion Lineal")
lineal.imprimir_ecuacion()
print("3 datos conocidos: ")
print("#1 x = 95 y = ", lineal.predecir(95))
print("#2 x = 89 y = ", lineal.predecir(89))
print("#3 x = 78 y = ", lineal.predecir(78))
print("Predicciones de 3 datos:")
print("#1 X = 110, Y  = ", lineal.predecir(110))
print("#2 X = 50, Y  = ", lineal.predecir(50))
print("#3 X = 45, Y  = ", lineal.predecir(26))
print("Coeficiente de Correlacion: ", lineal.get_coeficiente_corelacion())
print("Coeficiente de Determinacion: ", lineal.get_coeficiente_determinacion())
print("-----------------------------------------------------------")
print("Regresion Cuadratica")
cuadratica.imprimir_ecuacion()
print("3 datos conocidos: ")
print("#1 x = 95 y = ", cuadratica.predecir(95))
print("#2 x = 89 y = ", cuadratica.predecir(89))
print("#3 x = 78 y = ", cuadratica.predecir(78))
print("Predicciones de 3 datos:")
print("#1 X = 110, Y  = ", cuadratica.predecir(110))
print("#2 X = 50, Y  = ", cuadratica.predecir(50))
print("#3 X = 45, Y  = ", cuadratica.predecir(26))
print("Coeficiente de Correlacion: ", cuadratica.get_coeficiente_corelacion())
print("Coeficiente de Determinacion: ", cuadratica.get_coeficiente_determinacion())
print("----------------------------------------------------------")
print("Regresion  Cubica")
cubica.imprimir_ecuacion()
print("3 datos conocidos: ")
print("#1 x = 95 y = ", cubica.predecir(95))
print("#2 x = 89 y = ", cubica.predecir(89))
print("#3 x = 78 y = ", cubica.predecir(78))
print("Predicciones de 3 datos:")
print("#1 X = 110, Y  = ", cubica.predecir(110))
print("#2 X = 50, Y  = ", cubica.predecir(50))
print("#3 X = 45, Y  = ", cubica.predecir(26))
print("Coeficiente de Correlacion: ", cubica.get_coeficiente_corelacion())
print("Coeficiente de Determinacion: ", cubica.get_coeficiente_determinacion())