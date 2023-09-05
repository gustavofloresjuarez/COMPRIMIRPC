import os
import zipfile
import shutil
import time
from tqdm import tqdm

# Ruta de la carpeta principal que contiene las subcarpetas a comprimir en tu PC
ruta_carpeta_principal = os.getcwd()

# Función para comprimir una carpeta en un archivo ZIP
def comprimir_carpeta(carpeta):
    # Ruta completa de la carpeta a comprimir
    ruta_carpeta = os.path.join(ruta_carpeta_principal, carpeta)
    # Ruta completa del archivo ZIP resultante
    ruta_zip = os.path.join(ruta_carpeta_principal, carpeta + '.zip')

    # Lista de archivos en la carpeta
    archivos = [os.path.join(root, file) for root, _, files in os.walk(ruta_carpeta) for file in files]

    # Crea una barra de progreso personalizada
    with tqdm(total=len(archivos), unit='archivo', unit_scale=True, desc=f'Comprimiendo {carpeta}') as pbar:
        # Crear archivo ZIP
        with zipfile.ZipFile(ruta_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for ruta_archivo in archivos:
                # Agregar cada archivo individual al ZIP
                zipf.write(ruta_archivo, os.path.relpath(ruta_archivo, ruta_carpeta))
                # Actualiza la barra de progreso con el nombre del archivo actual
                pbar.set_postfix(nombre=os.path.basename(ruta_archivo), refresh=True)
                pbar.update(1)  # Actualiza la barra de progreso

    # Mensaje de finalización de compresión
    print(f"{carpeta} comprimida correctamente.")

# Comprimir cada subcarpeta por separado y luego eliminarlas
for nombre_carpeta in os.listdir(ruta_carpeta_principal):
    ruta_subcarpeta = os.path.join(ruta_carpeta_principal, nombre_carpeta)
    if os.path.isdir(ruta_subcarpeta):
        comprimir_carpeta(nombre_carpeta)
        # Eliminar la subcarpeta después de comprimir
        shutil.rmtree(ruta_subcarpeta)
