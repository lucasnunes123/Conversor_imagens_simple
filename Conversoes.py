from PIL import Image
import os

lista_webp = os.listdir('webp')
lista_jpg = os.listdir('jpg')
lista_png = os.listdir('png')

# Conversor WEBP to GIF(ok)
def WebpToGif():
    lista_webp = os.listdir('webp')

    for i in lista_webp:
        imagem = Image.open(f"webp/{i}")
        imagem.info.pop("background", None)
        imagem.save(f'imagens_convertidas/{i.replace("webp", "gif")}', "gif", save_all=True)

#Conversor de WEBP to JPG(OK)
def WebpToJpg():
    lista_webp = os.listdir('webp')

    for i in lista_webp:
        imagem = Image.open(f'webp/{i}').convert("RGB")
        imagem.save(f'imagens_convertidas/{i.replace("webp", "jpg")}')

# Conversor JPG to PNG(ok)
def JpgToPng():
    lista_jpg = os.listdir('jpg')

    for i in lista_jpg:
        imagem = Image.open(f'jpg/{i}')
        imagem.save(f'imagens_convertidas/{i.replace("jpg", "png")}')

# Conversor JPG to Pdf(ok)
def JpgToPdf():
    lista_jpg = os.listdir('jpg')

    for i in lista_jpg:
        imagem = Image.open(f'jpg/{i}')
        imagem.save(f'imagens_convertidas/{i.replace("jpg", "pdf")}')

# Convesor de PNG to PDF(Ok)
def PngToPdf():
    lista_png = os.listdir('png')

    for i in lista_png:
        imagem = Image.open(f"png/{i}").convert("RGB")
        imagem.save(f'imagens_convertidas/{i.replace("png", "pdf")}')

# Convesor de PNG to JPG(Ok)
def PngTojpg():
    lista_png = os.listdir('png')
    
    for i in lista_png:
        imagem = Image.open(f"png/{i}").convert("RGB")
        imagem.save(f'imagens_convertidas/{i.replace("png", "jpg")}')

# Conversor de PDF to Jpg(X)
def PdfToJpg():
    for i in lista_png:
        imagem = Image.open(f"png/{i}")
        imagem.save(f'imagens_convertidas/{i.replace("pdf", "jpg")}')
