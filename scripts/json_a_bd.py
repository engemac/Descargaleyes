# scripts/json_a_bd.py

import os
import json

def crear_bd_sql_y_datos(carpeta_output, carpeta_bd):
    os.makedirs(carpeta_bd + "/datos", exist_ok=True)

    estructura_sql = """
CREATE TABLE leyes (
    id SERIAL PRIMARY KEY,
    siglas TEXT,
    capitulo TEXT,
    articulo TEXT,
    fraccion TEXT,
    contenido TEXT
);
"""

    with open(os.path.join(carpeta_bd, "estructura.sql"), "w", encoding="utf-8") as f:
        f.write(estructura_sql)

    for nombre_ley in os.listdir(carpeta_output):
        ruta_json = os.path.join(carpeta_output, nombre_ley, f"{nombre_ley}.json")
        if not os.path.exists(ruta_json):
            continue

        registros = []
        with open(ruta_json, encoding="utf-8") as f:
            data = json.load(f)
            for cap in data:
                capitulo = cap["capitulo"]
                for art in cap["articulos"]:
                    articulo = art["titulo"]
                    if art["fracciones"]:
                        for frac in art["fracciones"]:
                            fraccion = frac["titulo"]
                            contenido = " ".join(frac["contenido"]).strip()
                            registros.append((nombre_ley, capitulo, articulo, fraccion, contenido))
                    else:
                        contenido = " ".join(art["contenido"]).strip()
                        registros.append((nombre_ley, capitulo, articulo, None, contenido))

        archivo_csv = os.path.join(carpeta_bd, "datos", f"{nombre_ley}.tsv")
        with open(archivo_csv, "w", encoding="utf-8") as f:
            for r in registros:
                fila = "\t".join([x if x else "" for x in r])
                f.write(fila + "\n")

        print(f"[✓] TSV generado para BD: {nombre_ley}")

