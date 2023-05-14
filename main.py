from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

images = convert_from_path('House Registration-signed.pdf',dpi=500,poppler_path=r'C:\poppler-23.05.0\Library\bin')

for i in range(len(images)):
    images[i].save('page'+str(i)+'.jpg','PNG')

