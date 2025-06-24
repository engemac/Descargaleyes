# scripts/main.py

import sys
import os
from descarga_ley import descargar_archivo_pdf
from procesa_ley import procesar_ley
from estructura_json import guardar_json_estructura

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: main.py SIGLAS")
        sys.exit(1)

    siglas = sys.argv[1]
    carpeta = f"output/{siglas}"

    descargar_archivo_pdf(siglas, carpeta)
    procesar_ley(siglas, siglas)

    txt_path = os.path.join(carpeta, f"{siglas}.txt")
    if os.path.exists(txt_path):
        with open(txt_path, encoding="utf-8") as f:
            texto = f.read()
            guardar_json_estructura(siglas, texto, carpeta)
    else:
        print(f"[x] No se generó TXT para {siglas}")
