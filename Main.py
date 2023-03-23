from tkinter import *
from tkinter import ttk

from Check_extension import*
from Conversoes import *
from Get_files import abrirJanela

#função irá verificar resposta do ComboBox
def verificar():
    ve = Cb_ConvertTypes.get()
    if ve == 'Webp para Gif':
        return WebpToGif()
    elif ve == 'Webp para Jpg':
        return WebpToJpg
    elif ve == 'Jpg para Png':
        return JpgToPng()
    elif ve == 'Jpg para Pdf':
        return JpgToPdf()
    elif ve == 'Png para Jpg':
        return PngTojpg()
    elif ve == 'Png para Pdf':
        return PngToPdf()
    

window = Tk()
window.geometry("400x250")
window.config(bg='#141111')
window.title("Convert")


#Label Conversão
texto_selectfiles = Label(window, text="Selecione os Arquivos Para Converter", font=('Arial 8 bold'), bg="#141111", fg="white")
texto_selectfiles.grid(column=0, row=0, padx=90, pady=10)

#Botão Selecionar arquivos
btn_searchfiles = Button(window, text="Selecionar Arquivos", relief='raised', command=abrirJanela)
btn_searchfiles.grid(column=0, row=2, padx=0, pady=10)

#Label Tipo de conversão
texto_selectfiles = Label(window, text="Escolha o Tipo de Conversão", font=('Arial 8 bold'), bg="#141111", fg="white")
texto_selectfiles.grid(column=0, row=5, padx=0, pady=0)

#Selecionar tipo de conversão
List_ConvertTypes = ["Webp para Gif", "Webp para jpg", "Jpg para Png", "Jpg para Pdf", "Png para Jpg", "Png para Pdf"]
Cb_ConvertTypes = ttk.Combobox(window, values=List_ConvertTypes)
Cb_ConvertTypes.set("Webp para Gif")
Cb_ConvertTypes.grid(column=0, row=7, padx=60, pady=0)


#Botão conversão
btn_vel = Button(window, text="Converter", command=lambda: [filtrarExtensão(), verificar()])
btn_vel.grid(column=0, row=9,  pady=10)


window.mainloop()