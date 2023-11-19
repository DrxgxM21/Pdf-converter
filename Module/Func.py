from PIL import Image
from reportlab.pdfgen import canvas
import sys

def screenshot_to_pdf(input_image_path, output_pdf_path):
    # Öffne das Bild
    img = Image.open(input_image_path)

    # Erstelle ein PDF-Dokument
    pdf = canvas.Canvas(output_pdf_path, pagesize=img.size )

    # Füge das Bild zur PDF-Seite hinzu
    pdf.drawInlineImage(input_image_path, 0, 0, width=img.width, height=img.height)

    # Speichere das PDF-Dokument
    pdf.save()
    sys.exit()



# def suche_datei(verzeichnis, dateiname):
#     for root, dirs, files in os.walk(verzeichnis):
#         if dateiname in files:
#             return os.path.join(root, dateiname)

#     return None


