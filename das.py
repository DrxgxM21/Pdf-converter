import tkinter as tk
from tkinter import simpledialog

def Pdfname():
    def read_button():
        window.destroy()
    
    
    window = tk.Tk()
    window.title("Pdf Name")

    ausgabe_label = tk.Label(window, text="Gib ein wie das Pdf heißen soll, du brauchst nicht am ende .pdf hinzufügen.")
    ausgabe_label.pack(pady=10)

    input_var = tk.StringVar()
    input_field = tk.Entry(window, textvariable=input_var)
    ok_button = tk.Button(window, text="Ok", command=read_button)
    input_field.pack(pady = 20)
    ok_button.pack(pady=10)

    window.mainloop()


pdf_name= Pdfname()
print(pdf_name)