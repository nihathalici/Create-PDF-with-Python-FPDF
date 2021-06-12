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
pdf.set_font('times', '', 12)

for i in range(1,41):
    pdf.cell(0, 10, f'This is line {i} :D', ln=True)

pdf.cell(80, 10, 'Good Bye World!')

pdf.output('pdf_2.pdf')
