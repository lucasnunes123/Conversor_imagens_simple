import os
import shutil
from tkinter import filedialog


#LOCAL PARA CONVERSOR
pasta_raiz = os.getcwd()
pasta_convert = f"{pasta_raiz}/Files_convert"

def abrirJanela():
    #ABRINDO JANELA NO PC DO USER PARA SELEÇÃO DE ARQUIVOS
    Win_open_files = filedialog.askopenfilenames()

    
    for arquivo in Win_open_files:
        shutil.copy2(arquivo, pasta_convert)

