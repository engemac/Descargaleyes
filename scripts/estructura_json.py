# scripts/estructura_json.py

import os
import json
import re

def extraer_estructura_legal(texto):
    estructura = []
    capitulo_actual = None
    articulo_actual = None

    lineas = texto.splitlines()

    for linea in lineas:
        linea = linea.strip()

        if re.match(r"^Cap[ií]tulo\s+[IVXLCDM]+", linea, re.IGNORECASE):
            capitulo_actual = {
                "capitulo": linea,
                "articulos": []
            }
            estructura.append(capitulo_actual)

        elif re.match(r"^Art[ií]culo\s+\d+[.-]?", linea, re.IGNORECASE):
            if capitulo_actual is None:
                capitulo_actual = {
                    "capitulo": "Sin Capítulo",
                    "articulos": []
                }
                estructura.append(capitulo_actual)

            articulo_actual = {
                "titulo": linea,
                "contenido": [],
                "fracciones": []
            }
            capitulo_actual["articulos"].append(articulo_actual)

        elif re.match(r"^Fracci[oó]n\s+[IVXLCDM\d]+", linea, re.IGNORECASE):
            if articulo_actual:
                articulo_actual["fracciones"].append({
                    "titulo": linea,
                    "contenido": []
                })

        elif linea:
            if articulo_actual:
                if articulo_actual["fracciones"]:
                    articulo_actual["fracciones"][-1]["contenido"].append(linea)
                else:
                    articulo_actual["contenido"].append(linea)

    return estructura

def guardar_json_estructura(nombre_archivo, texto_limpio, carpeta):
    estructura = extraer_estructura_legal(texto_limpio)
    ruta_json = os.path.join(carpeta, f"{nombre_archivo}.json")
    with open(ruta_json, "w", encoding="utf-8") as f:
        json.dump(estructura, f, ensure_ascii=False, indent=2)
    print(f"[✓] JSON estructurado guardado: {ruta_json}")
