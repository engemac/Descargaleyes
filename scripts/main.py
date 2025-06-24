# scripts/main.py

import sys
from descarga_ley import descargar_archivos
from procesa_ley import procesar_ley
from estructura_json import guardar_json_estructura

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: main.py SIGLAS")
        sys.exit(1)

    siglas = sys.argv[1]
    carpeta = f"output/{siglas}"

    descargar_archivos(siglas, siglas, carpeta)
    procesar_ley(siglas, siglas)

    txt_path = f"{carpeta}/{siglas}.txt"
    if os.path.exists(txt_path):
        with open(txt_path, encoding="utf-8") as f:
            texto = f.read()
            guardar_json_estructura(siglas, texto, carpeta)
