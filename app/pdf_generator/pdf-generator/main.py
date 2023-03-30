from fpdf import FPDF


class PDF(FPDF):

    player_name = "K. Kvaratskhelia"
    player_position = "Winger"
    player_height = "temp1"
    player_DOB = "13/03/1997"   
    player_agent = "temp2"
    player_age = "temp3"
    player_country = "temp4"
    player_agent = "temp5"
    player_club = "temp6"
    player_league = "temp7"
    player_weight = "temp8"
    player_foot = "temp9"
    player_on_loan = "yes"
    player_contract_date = "temp10"
    player_num_matches = "10"

    def header(self):
        # Banner
        self.rect(-1, -1, 250, 30, 'DF')
        # Logo 1
        self.image('app/pdf_generator/pdf-generator/images/Logo_Tactalyse.png', 4, 2, 25)
        # Logo 2
        self.image('app/pdf_generator/pdf-generator/images/Logo_Tactalyse_Stats.png', 50, 7, 115)
        # Background
        self.image("app/pdf_generator/pdf-generator/images/BackgroundClean.png", x=0, y=30, w=self.w, h=self.h)
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

    #print player's image and basic information in the first page
    def print_player_basic_info(self):
        self.image('app/pdf_generator/pdf-generator/images/placeholder_player_photo.jpg', 50, 60, 115)
        self.set_font('Arial', 'B', 14)
        end_pos = 30

        # First column 
        start_x_pos = 50.0
        start_y_pos = 150.0
        self.set_xy(start_x_pos, start_y_pos)
        self.cell(0, 20, 'POSITION: ', ln = 1)
        self.set_xy(start_x_pos + end_pos, start_y_pos)
        self.cell(0, 20, pdf.player_position, ln = 1)

        self.set_xy(start_x_pos, start_y_pos + 10)
        self.cell(0, 20, 'CLUB: ', ln = 1)
        self.set_xy(start_x_pos + end_pos, start_y_pos + 10)
        self.cell(0, 20, pdf.player_club, ln = 1)

        self.set_xy(start_x_pos, start_y_pos + 20)
        self.cell(0, 20, 'ON LOAN: ', ln = 1)
        self.set_xy(start_x_pos + end_pos, start_y_pos + 20)
        self.cell(0, 20, pdf.player_on_loan, ln = 1)

        self.set_xy(start_x_pos, start_y_pos + 30)
        self.cell(0, 20, 'CONTRACT EXPIRES ON: ', ln = 1)
        self.set_xy(start_x_pos + end_pos + 35, start_y_pos + 30)
        self.cell(0, 20, pdf.player_contract_date, ln =1)

        self.set_xy(start_x_pos, start_y_pos + 60)
        self.cell(0, 20, 'COUNTRY: ', ln = 1)
        self.set_xy(start_x_pos + end_pos, start_y_pos + 60)
        self.cell(0, 20, pdf.player_country, ln =1)

        self.set_xy(start_x_pos, start_y_pos + 70)
        self.cell(0, 20, 'HEIGHT: ', ln = 1)
        self.set_xy(start_x_pos + end_pos, start_y_pos + 70)
        self.cell(0, 20, pdf.player_height + "cm", ln =1)

        self.set_xy(start_x_pos, start_y_pos +80)
        self.cell(0, 20, 'DOB: ', ln = 1)
        self.set_xy(start_x_pos + end_pos, start_y_pos + 80)
        self.cell(0, 20, pdf.player_DOB, ln =1)


        # Second column
        start_x2_pos = 120.0
        start_y2_pos = 150.0
        self.set_xy(start_x2_pos, start_y2_pos)
        self.cell(0, 20, 'LEAGUE: ', ln = 1)
        self.set_xy(start_x2_pos + end_pos, start_y2_pos)
        self.cell(0, 20, pdf.player_league, ln =1)

        self.set_xy(start_x2_pos, start_y2_pos + 10)
        self.cell(0, 20, 'AGENT: ', ln = 1)
        self.set_xy(start_x2_pos + end_pos, start_y2_pos + 10)
        self.cell(0, 20, pdf.player_agent, ln =1)

        self.set_xy(start_x2_pos, start_y2_pos + 20)
        self.cell(0, 20, '#MATCHES: ', ln = 1)
        self.set_xy(start_x2_pos + end_pos, start_y2_pos + 20)
        self.cell(0, 20, pdf.player_num_matches, ln =1)

        self.set_xy(start_x2_pos, start_y2_pos + 60)
        self.cell(0, 20, 'AGE: ', ln = 1)
        self.set_xy(start_x2_pos + end_pos, start_y2_pos + 60)
        self.cell(0, 20, pdf.player_age, ln =1)

        self.set_xy(start_x2_pos, start_y2_pos + 70)
        self.cell(0, 20, 'WEIGHT: ', ln = 1)
        self.set_xy(start_x2_pos + end_pos, start_y2_pos + 70)
        self.cell(0, 20, pdf.player_weight + "kg", ln =1)

        self.set_xy(start_x2_pos, start_y2_pos + 80)
        self.cell(0, 20, 'FOOT: ', ln = 1)
        self.set_xy(start_x2_pos + end_pos, start_y2_pos + 80)
        self.cell(0, 20, pdf.player_foot, ln =1)




# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.set_font('Arial', '', 12)
pdf.set_draw_color(250, 51, 10)
pdf.set_fill_color(255, 230, 230)
pdf.set_title(pdf.player_name)
pdf.add_page()
pdf.print_title()
pdf.print_player_basic_info()


pdf.print_chapter('Stats Progression', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
pdf.output(pdf.title + '.pdf', 'F')