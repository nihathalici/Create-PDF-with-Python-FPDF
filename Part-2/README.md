# Create PDF with Python FPDF | Part-2

How to create a pdf with python using the simple library FPDF2. This is part 2 of a 4 part series where we go over how to create a pdf with Python and eventually automate the creation of reports and invoices. 

* Many lines
* Page Break
* Break Margin
* Header Footer Overview
* Add Header
* Add Footer
* Add Page Number

part_2.py
========================================================
```Python3
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # logo
        self.image('fox_face.png', 10, 8, 25)
        # font
        self.set_font('helvetica', 'B', 20)
        # Padding
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title', border=True, ln=1, align='C')
        # line break
        self.ln(20)

    # page footer
    def footer(self):
        # Set position of the footer
        self.set_y(-15)
        # set font
        self.set_font('helvetica', 'I', 10)
        # page number
        self.cell(0, 10, f'Page {self.page_no()}/nb', align = 'C')

# create a PDF object
pdf = PDF('P', 'mm', 'Letter')

# get total page numbers
pdf.alias_nb_pages(alias='nb')

# Set auto page break
pdf.set_auto_page_break(auto=True, margin = 15)

# Add a page
pdf.add_page()

# specify font
pdf.set_font('helvetica', 'BIU', 16)

pdf.set_font('times', '', 12)

for i in range(1,41):
    pdf.cell(0, 10, f'This is line {i} :D', ln=True)

pdf.cell(80, 10, 'Good Bye World!')

pdf.output('pdf_2.pdf')

```

* Watch on YouTube:
https://www.youtube.com/watch?v=JhQVD7Y1bsA

* GitHub Repo:
https://github.com/bvalgard/create-pdf-with-python-fpdf2

Sample Output
========================================================
![Sample output Create PDF with Python FPDF | Part-2](https://github.com/nihathalici/Create-PDF-with-Python-FPDF/blob/main/Part-2/part_2-png.png)


