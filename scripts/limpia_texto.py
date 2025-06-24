# scripts/limpia_texto.py

import re
import unicodedata

def limpiar_texto(texto):
    texto = texto.replace("\r", " ").replace("\n", " ")
    texto = re.sub(r"[ ]{2,}", " ", texto)
    texto = re.sub(r"[^\x00-\x7F\u00A1-\u017F]+", "", texto)  # elimina basura
    texto = unicodedata.normalize("NFC", texto)  # normaliza acentos
    return texto.strip()
