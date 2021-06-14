from fpdf import FPDF

# create FPDF object
# Layout ('P', 'L')
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
pdf = FPDF('P', 'mm', 'Letter')

# uni = TrueType font subset embedding
pdf.add_font('Zapfino', '', '/Library/Fonts/Zapfino.ttf', uni=True)
pdf.add_font('Amatic', '', '/Documents/Python_Scripts/pdf/adding_custom_fonts/AmaticSC-Regular.ttf', uni=True)
pdf.add_font('Amatic', 'B', '/Documents/Python_Scripts/pdf/adding_custom_fonts/AmaticSC-Bold.ttf', uni=True)

# Add a page
pdf.add_page()

# specify font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
pdf.set_font('Amatic', '', 16)
pdf.set_text_color(220, 50, 50)
# Add text
# w = width
# h = height
# txt = your text
# ln (0 False; 1 True - move cursor down to next line)
# border(0 False; 1 True - add border around cell)
pdf.cell(120, 100, 'Hello World!', ln=True, border=True)

pdf.set_font('Amatic', 'B', 12)
pdf.cell(80, 10, 'Good Bye World!')

pdf.output('pdf_1.pdf')
