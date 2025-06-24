# scripts/descarga_ley.py

import os
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def descargar_archivo_pdf(siglas, carpeta_destino):
    base_url = "https://www.diputados.gob.mx/LeyesBiblio/pdf"
    archivo = f"{siglas.upper()}.pdf"
    url = f"{base_url}/{archivo}"

    os.makedirs(carpeta_destino, exist_ok=True)
    ruta_archivo = os.path.join(carpeta_destino, archivo)

    try:
        respuesta = requests.get(url, headers=HEADERS, verify=False, timeout=30)
        if respuesta.status_code == 200 and len(respuesta.content) > 10000:
            with open(ruta_archivo, "wb") as f:
                f.write(respuesta.content)
            print(f"[✓] PDF descargado correctamente: {url}")
        else:
            print(f"[x] No disponible o vacío: {url}")
    except Exception as e:
        print(f"[!] Error al descargar {url} — {e}")
