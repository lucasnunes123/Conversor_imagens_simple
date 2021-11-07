from PIL import Image
import os

lista_imagens = os.listdir('imagens')

# Conversor WEBP to GIF
for i in lista_imagens:
    imagem = Image.open(f"imagens/{i}")
    imagem.info.pop("background", None)
    imagem.save(f'imagens_convertidas/{i.replace("webp", "gif")}', "gif", save_all=True)