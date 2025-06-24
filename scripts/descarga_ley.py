# scripts/descarga_ley.py

import os
import requests
from pathlib import Path

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def descargar_archivos(nombre, siglas, carpeta_destino):
    base_url = "https://www.diputados.gob.mx/LeyesBiblio"
    formatos = ["pdf", "doc"]
    nombre_archivo = siglas.upper()

    os.makedirs(carpeta_destino, exist_ok=True)

    for ext in formatos:
        url = f"{base_url}/{ext}/{nombre_archivo}.{ext}"
        try:
            respuesta = requests.get(url, headers=HEADERS, verify=False, timeout=30)
            if respuesta.status_code == 200 and len(respuesta.content) > 10_000:
                ruta_archivo = os.path.join(carpeta_destino, f"{nombre_archivo}.{ext}")
                with open(ruta_archivo, "wb") as f:
                    f.write(respuesta.content)
                print(f"[✓] Descargado: {url}")
            else:
                print(f"[x] Vacío o no encontrado: {url}")
        except Exception as e:
            print(f"[!] Error al descargar {url} — {e}")
