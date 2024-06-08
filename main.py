import os
import numpy as np

# Especifica la ruta a tu carpeta
folder_path = '/home/andrewkc/Projects/ml-p3/features10/r21d/r2plus1d_18_16_kinetics/'

# Lista para almacenar los datos cargados
data_list = []

# Itera sobre los archivos en la carpeta
for filename in os.listdir(folder_path):
    if filename.endswith('.npy'):
        file_path = os.path.join(folder_path, filename)
        # Carga el archivo .npy
        data = np.load(file_path)
        # Añade los datos a la lista
        data_list.append(data)

# Opcional: Imprimir los datos para verificar
for i, data in enumerate(data_list):
    print(f'Datos del archivo {i+1}:')
    print(data)
    print(data.shape)
