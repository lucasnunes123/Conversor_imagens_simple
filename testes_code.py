import os
import PyPDF2

arquivos = 'Files_convert'
list = os.listdir(arquivos)


for i in arquivos():
    pdf_file = open(f'{i}')
    pdf_ler = PyPDF2.PdfFileReader(pdf_file)

    for page_num in range(pdf_ler.numPages):
        page = pdf_ler.getPage(page_num)
        imagem = page.toImage()
        imagem.save('pagina_{}.jpg'.format(page_num+1))
        
pdf_file.close