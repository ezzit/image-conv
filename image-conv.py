import os
from tkinter import Tk, Label, Entry, Button, OptionMenu, StringVar, filedialog
from PIL import Image
from ttkbootstrap import Style

def image_converter():
    try:
        imagem_url = entry_url.get()
        converted = dropdown_format_var.get()
        
        imagem = Image.open(imagem_url)
        
        image_converted = os.path.splitext(imagem_url)[0] + '.' + converted.lower()
        imagem.save(image_converted)
        
        mensage_status.config(text=f'Imagem convertida com sucesso: {image_converted}')
    except Exception as e:
        mensage_status.config(text=f'Falha na conversão da imagem: {str(e)}')

def selecionar_arquivo():
    imagem_url = filedialog.askopenfilename(filetypes=[('Imagens', '*.jpg;*.jpeg;*.png;*.gif;*.tiff;*.bmp;*.svg;*.raw;*.webp;*.hdr;*.ico')])
    entry_url.delete(0, 'end')
    entry_url.insert(0, imagem_url)

root = Tk()
style = Style(theme='yeti')

style.configure('TButton', font=('TkDefaultFont', 10))

root.title('Image-Conv')

root.geometry('430x120'),
root.resizable(False, False)

label_url = Label(root, text='Image URL:')
label_url.grid(row=0, column=0, padx=10, pady=10)

entry_url = Entry(root, width=40)
entry_url.grid(row=0, column=1, padx=10, pady=10)

button_selecionar = Button(root, text='Select File', command=selecionar_arquivo)
button_selecionar.grid(row=0, column=2, padx=10, pady=10)

label_format = Label(root, text='Convert to:')
label_format.grid(row=1, column=0, padx=10, pady=10)

formats = ['JPEG', 'PNG', 'GIF', 'TIFF', 'BMP', 'SVG', 'RAW', 'WebP', 'HDR', 'ICO']
dropdown_format_var = StringVar(root)
dropdown_format_var.set(formats[0])

dropdown_format = OptionMenu(root, dropdown_format_var, *formats)
dropdown_format.grid(row=1, column=1, padx=10, pady=10)

button_converter = Button(root, text='Convert', command=image_converter)
button_converter.grid(row=1, column=2, padx=10, pady=10)

mensage_status = Label(root, text='')
mensage_status.grid(row=2, columnspan=3, pady=10)

root.mainloop()