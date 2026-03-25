from pypdf import PdfReader

def carregar_pdf(caminho):
    reader = PdfReader(caminho)
    texto = ""

    for pagina in reader.pages:
        texto += pagina.extract_text() or ""

    return texto