# scripts/procesa_ley.py

import os
from docx import Document
from PyPDF2 import PdfReader
from limpia_texto import limpiar_texto

def extraer_txt_desde_doc(path):
    try:
        doc = Document(path)
        return "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        print(f"[!] Error procesando DOC: {e}")
        return ""

def extraer_txt_desde_pdf(path):
    try:
        pdf = PdfReader(path)
        return "\n".join([page.extract_text() or "" for page in pdf.pages])
    except Exception as e:
        print(f"[!] Error procesando PDF: {e}")
        return ""

def guardar_txt_limpio(nombre_archivo, texto, carpeta):
    texto_limpio = limpiar_texto(texto)
    with open(os.path.join(carpeta, f"{nombre_archivo}.txt"), "w", encoding="utf-8") as f:
        f.write(texto_limpio)
    print(f"[✓] Texto limpio guardado: {nombre_archivo}.txt")

def procesar_ley(nombre, siglas):
    carpeta = f"output/{siglas}"
    os.makedirs(carpeta, exist_ok=True)

    doc_path = os.path.join(carpeta, f"{siglas}.doc")
    pdf_path = os.path.join(carpeta, f"{siglas}.pdf")

    texto = ""
    if os.path.exists(doc_path):
        texto = extraer_txt_desde_doc(doc_path)
    elif os.path.exists(pdf_path):
        texto = extraer_txt_desde_pdf(pdf_path)
    
    if texto:
        guardar_txt_limpio(siglas, texto, carpeta)
    else:
        print(f"[x] No se pudo extraer texto de {siglas}")
