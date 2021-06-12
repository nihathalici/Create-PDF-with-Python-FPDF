# Create PDF with Python FPDF | Part-3

How to create a pdf with python using the simple library FPDF2. This is part 3 of a 4 part series where we go over how to create a pdf with Python and eventually automate the creation of reports and invoices. 



part_3.py
========================================================
```Python3
from fpdf import FPDF

title = '20,000 Leagues Under the Sea'

class PDF(FPDF):
    def header(self):
        # font
        self.set_font('helvetica', 'B', 15)
        # Calculate width of title and position
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        # colors of frame, background, and text
        self.set_draw_color(0, 80, 180) # border = blue
        self.set_fill_color(230, 230, 0) # background = yellow
        self.set_text_color(220, 50, 50) # text = red
        # Thickness of frame (border)
        self.set_line_width(1)
        # Title
        self.cell(title_w, 10, title, border=1, ln=1, align='C', fill=1)
        # line break
        self.ln(10)

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

pdf.output('pdf_3.pdf')

```

* Watch on YouTube:
https://www.youtube.com/watch?v=FcrW-ESdY-A

* GitHub Repo:
https://github.com/bvalgard/create-pdf-with-python-fpdf2

Sample Output
========================================================
![Sample output Create PDF with Python FPDF | Part-2](https://github.com/nihathalici/Create-PDF-with-Python-FPDF/blob/main/Part-2/part_2-png.png)


