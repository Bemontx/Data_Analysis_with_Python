import numpy as np

def calculate(lst):
    matrix = np.array(lst).reshape(3, 3)
    media = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix).tolist()]
    varianza = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).tolist()]
    std_dev = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix).tolist()]
    max_valor = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix).tolist()]
    min_valor = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix).tolist()]
    sum_total = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).tolist()]
    
    return {
        'la media es:': media,
        'la varianza es:': varianza,
        'la desviacion estandar es:': std_dev,
        'valor maximo:': max_valor,
        'valor minimo:': min_valor,
        'suma total:': sum_total
    }

lista_prueba = [45,12,65,98,78,48,15,55,28]

print(calculate(lista_prueba))