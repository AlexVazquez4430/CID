from DataSet import DataSet
from SLR import SLR

#Arreglo de datos para el Data Set
x = [1,2,3,4,5,6,7,8,9]
y  = [5,10,15,20,25,30,35,40,45]
#Se crea el objeto de DataSet con los datos del arreglo
datos = DataSet(x,y)
#Creamos nuestra clase de SLR
mate = SLR(datos.get_x(),datos.get_y())
mate.imprimir_ecuacion()
print("Dado X = 10, la prediccion de Y es = ", mate.predecir(10))
print("Coeficiente de Correlacion: ", mate.get_coeficiente_corelacion())
print("Coeficiente de Determinacion: ", mate.get_coeficiente_determinacion())
print("Predicciones de 5 datos:")
print("#1 X = 20, Y  = ", mate.predecir(20))
print("#2 X = 24, Y  = ", mate.predecir(24))
print("#3 X = 45, Y  = ", mate.predecir(45))
print("#4 X = 50, Y  = ", mate.predecir(50))
print("#5 X = 59, Y  = ", mate.predecir(59))