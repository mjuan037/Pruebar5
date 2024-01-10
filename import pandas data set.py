import pandas as pd
import os

# Lista de rutas de archivos CSV
archivos_csv = [
    r'C:\Users\Chanchor\OneDrive - Universidad Piloto de Colombia\Documents\Prueba R5\artistas.csv',
    r'C:\Users\Chanchor\OneDrive - Universidad Piloto de Colombia\Documents\Prueba R5\albums.csv',
    r'C:\Users\Chanchor\OneDrive - Universidad Piloto de Colombia\Documents\Prueba R5\tracks.csv',
    r'C:\Users\Chanchor\OneDrive - Universidad Piloto de Colombia\Documents\Prueba R5\audio_features.csv'
]

# Para cada archivo CSV
for archivo_csv in archivos_csv:
    # Cargar datos desde el archivo CSV
    df = pd.read_csv(archivo_csv)

    # Verificar valores nulos
    null_values = df.isnull().sum()

    # Verificar duplicados
    duplicates = df.duplicated().sum()

    # Verificar estadísticas descriptivas
    statistics = df.describe()

    # Verificar tipos de datos
    data_types = df.dtypes

    # Crear el nombre del archivo de informe
    nombre_archivo = f'informe_calidad_datos_{os.path.basename(archivo_csv)[:-4]}.txt'

    # Guardar resultados en un informe
    with open(nombre_archivo, 'w') as report:
        report.write(f"Resumen de calidad de datos para {archivo_csv}:\n")
        report.write("===========================\n")
        report.write(f"Valores Nulos:\n{null_values}\n\n")
        report.write(f"Valores Duplicados: {duplicates}\n\n")
        report.write(f"Estadísticas Descriptivas:\n{statistics}\n\n")
        report.write(f"Tipos de Datos:\n{data_types}\n")

    print(f"Análisis completado para {archivo_csv}. Se ha generado el informe en '{nombre_archivo}'.")
