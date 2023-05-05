import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from Get_files import abrirJanela
from Check_extension import *
from Conversoes import *

#função irá verificar resposta do ComboBox
def verificar():
    ve = Cb_types.get()
    if ve == 'Webp para Gif':
        return WebpToGif()
    elif ve == 'Webp para Jpg':
        return WebpToJpg()
    elif ve == 'Jpg para Png':
        return JpgToPng()
    elif ve == 'Jpg para Pdf':
        return JpgToPdf()
    elif ve == 'Png para Jpg':
        return PngTojpg()
    elif ve == 'Png para Pdf':
        return PngToPdf()


janela = tk.Tk()
janela.title("Conversor")
style =  ttk.Style("solar")
janela.geometry("400x250")

janela.iconbitmap("icon.ico")

#Label Conversão
Label_tipo_conversão = ttk.Label(janela, text="Selecionar Arquivos",font=('Arial 10 bold'))
Label_tipo_conversão.pack(padx=5, pady=10)

#Botão Selecionar arquivos
btn_select_files = ttk.Button(janela, text="Selecionar Arquivos", bootstyle="success-outline", command=abrirJanela)
btn_select_files.pack(padx=5, pady=10)

#Label Tipo de conversão
Label_tipo_conversão = ttk.Label(janela, text="Escolha o Tipo de Conversão",font=('Arial 10 bold'))
Label_tipo_conversão.pack(padx=5, pady=10)

#Selecionar tipo de conversão
List_ConvertTypes = ["Webp para Gif", "Webp para Jpg", "Jpg para Png", "Jpg para Pdf", "Png para Jpg", "Png para Pdf"]
Cb_types = ttk.Combobox(janela, values=List_ConvertTypes, bootstyle="info")
Cb_types.pack(padx=5, pady=10)

#Botão conversão
btn_convert = ttk.Button(janela, text="Converter", bootstyle="light", command=lambda: [filtrarExtensão(), verificar()])
btn_convert.pack(padx=5, pady=10)

janela.mainloop()