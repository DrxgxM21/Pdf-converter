import sys
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def AbfrageJPG():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Wähle eine JPEG-Datei aus", filetypes=[("JPEG-Dateien", "*.jpg")])

    try:
        with open(file_path, 'rb') as datei:
            Image.open(datei)
            return file_path
    except FileNotFoundError:
        print(f"Die Datei {file_path} wurde nicht gefunden.")
        input("Das Programm muss neugestartet werden ")
        sys.exit()
    except Exception as e:
        print(f"Fehler beim Öffnen des Bildes: {e}")
        input("Das Programm muss neugestartet werden ")
        sys.exit()

    

# def PdfName():
#     def bestaetigen():
#         global eingabe
#         eingabe_wert = eingabe_entry.get()
#         fenster.destroy()
#         eingabe_wert += ".pdf"
#         eingabe = eingabe_wert
    
#     eingabe = None

#     fenster = tk.Tk()
#     fenster.title("Name des Pdf")

#     label = tk.Label(fenster, text="Gib den Namen deiner Pdfs ein, du brauchst nicht .pdf einzugeben:")
#     label.pack(pady=10)

#     eingabe_entry = tk.Entry(fenster, width=30)
#     eingabe_entry.pack(pady=10)

#     bestaetigungs_button = tk.Button(fenster, text="Bestätigen", command=bestaetigen)
#     bestaetigungs_button.pack(pady=10)

#     fenster.mainloop()
    
#     # eingabe_wert = bestaetigen()

#     print(eingabe)

#     retursn eingabe

# class Gui(tk.Tk):
#     def __inti__(self):
#         super().__init__()
#         self.title("Name des Pdf")
#         self.label = tk.Label(self, text="Gib den Namen deiner Pdfs ein, du brauchst nicht .pdf einzugeben:")
#         self.label.pack(pady=10) 
#         self.eingabe_entry = tk.Entry(self, width=30)
#         self.eingabe_entry.pack(pady=10)

#         self.bestaetigungs_button = tk.Button(self, text="Bestätigen", command=self.bestaetigen)
#         self.bestaetigungs_button.pack(pady=10)

#         self.eingabe_wert = None

#     def bestaetigen(self):
#         self.eingabe_wert = self.eingabe_entry.get()
#         self.eingabe_wert  += ".pdf"
#         self.destroy()

# app = Gui()
# app.mainloop()

# eingabe_wert = bestaetigen()

# Global variable to store the entered text
import tkinter as tk

def call_entry_gui(callback):
    global global_variable, entry  # Declare entry as a global variable

    global_variable = ""

    # Function to handle button click
    def on_button_click():
        global global_variable
        global_variable = entry.get()
        global_variable += ".pdf"
        print(global_variable)
        root.destroy()
        callback(global_variable)  # Execute the callback with the entered value

    # Create the main window
    root = tk.Tk()
    root.title("Text Entry GUI")

    label = tk.Label(root, text="Gib den Namen des Pdf ein, du musst kein .pdf anhängen.")
    label.pack (pady=10)
    
    # Create an entry widget
    entry = tk.Entry(root, width=30)
    entry.pack(pady=10)

    
    
    # Create a button
    button = tk.Button(root, text="Submit", command=on_button_click)
    button.pack()

    # Start the main event loop
    root.mainloop()




# Example usage:
if __name__ == "__main__":
    result = call_entry_gui()
    print("Entered text:", result)
