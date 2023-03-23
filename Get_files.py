import os
from tkinter import filedialog


#LOCAL PARA CONVERSOR
convert_local = os.getcwd()

def abrirJanela():
    #ABRINDO JANELA NO PC DO USER PARA SELEÇÃO DE ARQUIVOS
    Win_open_files = filedialog.askopenfilenames()

    
    for caminho in Win_open_files:
        caminho_final = caminho

        #REMOÇÃO DE CARACTERS(":", "/" e "[espaço]") QUE PODEM INTERFERIR NO DIRECIONAMENTO DAS PASTAS
        troque = ":/ "
        for x in range(0, len(troque)):
            caminho_final = caminho_final.replace(troque[x], "")

        os.rename(f'{caminho}', f'{convert_local}'+ f"\Files_convert\\{caminho_final}")

