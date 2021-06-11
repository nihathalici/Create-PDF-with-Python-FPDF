# Create PDF with Python FPDF | Part-1

How to create a pdf with python using the simple library FPDF2. This is part 1 of a 4 part series where we go over how to create a pdf with Python and eventually automate the creation of reports and invoices. 

* Setup
* Library Installation
* Imports
* Create PDF Object
* Add PDF Page
* Specify Font
* Add Text
* Create PDF
* Adding Additional Text
* Permission Error
* Text Placement

part_1.py
========================================================
```Python3
from fpdf import FPDF

# create FPDF object
# Layout ('P', 'L')
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
pdf = FPDF('P', 'mm', 'Letter')

# Add a page
pdf.add_page()

# specify font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
pdf.set_font('helvetica', '', 16)

# Add text
# w = width
# h = height
# txt = your text
# ln (0 False; 1 True - move cursor down to next line)
# border(0 False; 1 True - add border around cell)
pdf.cell(120, 100, 'Hello World!', ln=True, border=True)
pdf.cell(80, 10, 'Good Bye World!')

pdf.output('pdf_1.pdf')
```

* Watch on YouTube:
https://www.youtube.com/watch?v=q70xzDG6nls&t=2s

* GitHub Repo:
https://github.com/bvalgard/create-pdf-with-python-fpdf2

Sample Output
========================================================
![Sample output Create PDF with Python FPDF | Part-1](https://github.com/nihathalici/Create-PDF-with-Python-FPDF/blob/main/Part-1/pdf_1.png)

