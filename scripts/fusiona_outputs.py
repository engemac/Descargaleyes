# scripts/fusiona_outputs.py

import os
import shutil

def fusionar_todo(carpeta_origen="output", carpeta_final="output_global"):
    os.makedirs(carpeta_final, exist_ok=True)

    for subcarpeta in os.listdir(carpeta_origen):
        origen = os.path.join(carpeta_origen, subcarpeta)
        if not os.path.isdir(origen):
            continue
        for archivo in os.listdir(origen):
            shutil.copy2(os.path.join(origen, archivo), carpeta_final)

    print(f"[✓] Todos los archivos fusionados en {carpeta_final}")
