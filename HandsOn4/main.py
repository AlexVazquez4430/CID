from Datos import Datos
from Clasificador import Clasificador

def main() -> None:
    ds = Datos()
    knn = Clasificador(metrica = 'euclileana')

    knn.fit(ds.get_x(), ds.get_y())

    prueba = [[190, 75], [180, 78], [160, 60], [195, 88], [200, 80]] 
    predicciones = knn.predict(prueba) 

    print('predicciones')
    for i in range(len(prueba)):
        print(f'{'-' * 20} Prediccion {i + 1} {'-' * 20}')
        print(f'Altura: {prueba[i][0]} cms')
        print(f'Peso: {prueba[i][1]} kgs')
        print(f'Prediccion Talla Camisa: {predicciones[i]} -> {['Mediana', 'Grande'][predicciones[i]]}')
        print(f'{'-' * 54}')

# Entry point
if __name__ == '__main__':
    main()