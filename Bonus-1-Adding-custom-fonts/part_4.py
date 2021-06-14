from fpdf import FPDF

title = '20,000 Leagues Under the Sea'

class PDF(FPDF):

    def __init__(self, **kwargs):
        super(PDF, self).__init__(**kwargs)
        # Adding custom (google) fonts
        self.add_font('Zapfino', '', '/Library/Fonts/Zapfino.ttf', uni=True)
        self.add_font('Amatic', '', '/Documents/Python_Scripts/pdf/adding_custom_fonts/AmaticSC-Regular.ttf', uni=True)
        self.add_font('Amatic', 'B', '/Documents/Python_Scripts/pdf/adding_custom_fonts/AmaticSC-Bold.ttf', uni=True)

    def header(self):
        # font
        self.set_font('Amatic', 'B', 15)
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
        self.set_font('Amatic', '', 10)
        # page number
        self.cell(0, 10, f'Page {self.page_no()}/nb', align = 'C')

    # Adding chapter title to start of each chapter
    def chapter_title(self, ch_num, ch_title, link):
        # Set link location
        self.set_link(link)
        # set font
        self.set_font('Zapfino', '', 12)
        # background color
        self.set_fill_color(200, 220, 255)
        # Chapter title
        chapter_title = f'Chapter {ch_num} : {ch_title}'
        self.cell(0, 5, chapter_title, ln=1, fill=1)
        # line break
        self.ln()

    # Chapter content
    def chapter_body(self, name):
        # read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # set font
        self.set_font('times', '', 12)
        # insert text
        self.multi_cell(0, 5, txt)
        # line break
        self.ln()
        # end each chapter
        self.set_font('times', 'I', 12)
        self.cell(0, 5, 'END OF CHAPTER')

    def print_chapter(self, ch_num, ch_title, name, link):
        self.add_page()
        self.chapter_title(ch_num, ch_title, link)
        self.chapter_body(name)

# create a PDF object
pdf = PDF(orientation='P', unit='mm', format='Letter')

# metadara
pdf.set_title(title)
pdf.set_author('Jules Verne')

# Create Links
website = 'https://www.youtube.com/channel/UC17QKsysOmZ7oJepmmcUTvA'
ch1_link = pdf.add_link()
ch2_link = pdf.add_link()

# Set auto page break
pdf.set_auto_page_break(auto=True, margin = 15)

# Add Page
pdf.add_page()
pdf.image('background_image.png', x = -0.5, w = pdf.w + 1)

# Attach Links
pdf.cell(0, 10, 'Tutorial Source', ln = 1, link = website)
pdf.cell(0, 10, 'Chapter 1', ln = 1, link = ch1_link)
pdf.cell(0, 10, 'Chapter 2', ln = 1, link = ch2_link)

# get total page numbers
pdf.alias_nb_pages(alias='nb')

pdf.print_chapter(1, 'A RUNAWAY REEF','chp1.txt', ch1_link)
pdf.print_chapter(2, 'THE PROS AND CONS', 'chp2.txt', ch2_link)

pdf.output('pdf_4.pdf')
