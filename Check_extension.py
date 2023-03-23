import os


def filtrarExtensão():

    Files_list = os.listdir('Files_convert')

    for i in Files_list:
        extensão_check = os.path.splitext(f"{i}")[1]

        if extensão_check == ".jpg":
            os.rename(f"Files_convert/{i}", f"jpg/{i}")

        elif extensão_check == ".png":
            os.rename(f"Files_convert/{i}", f"png/{i}")

        elif extensão_check == ".webp":
            os.rename(f"Files_convert/{i}", f"webp/{i}")
