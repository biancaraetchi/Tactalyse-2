from fpdf import FPDF

class PDF(FPDF):

    player_name = "K. Kvaratskhelia"

    def header(self):
        # Banner
        self.rect(-1, -1, 250, 30, 'DF')
        # Logo 1
        self.image('images/Logo_Tactalyse.png', 4, 2, 25)
        # Logo 2
        self.image('images/Logo_Tactalyse_Stats.png', 87, 7, 115)
        # Background
        self.image("images/BackgroundClean.png", x=0, y=30, w=self.w, h=self.h)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def chapter_title(self, label):
        # Arial 12
        self.set_font('Arial', '', 27)
        # Line break
        self.ln(8)
        # Title
        self.cell(0, 14, label, 'B', 1, 'C', False)
        # Line break
        self.ln(4)

    def chapter_body(self, text):
        # Read text file
        txt = text
        # Times 12
        self.set_font('Arial', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()

    def print_chapter(self, title, text):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(text)
        self.set_font('Arial', '', 12)

    def print_title(self):
        self.set_font('Arial', '', 30)
        self.ln(8)
        self.cell(0, 14, "Stats Report for " + self.player_name, 0, 1, 'C', False)
        self.ln(4)

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.set_font('Arial', '', 12)
pdf.set_draw_color(250, 51, 10)
pdf.set_fill_color(255, 230, 230)
pdf.set_title(pdf.player_name)
pdf.add_page()
pdf.print_title()

pdf.print_chapter('Stats Progression', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
pdf.output(pdf.title + '.pdf', 'F')