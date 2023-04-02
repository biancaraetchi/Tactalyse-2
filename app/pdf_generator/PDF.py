from fpdf import FPDF
from PIL import Image
from .Player import Player
import io


class PDF(FPDF):

    player = Player()

    def set_info(self, player_name, league_df, main_pos):
        self.player.set_personal_info(player_name, league_df)
        self.player.set_football_info(player_name, league_df, main_pos)

    def header(self):
        # Banner
        self.rect(-1, -1, 250, 30, 'DF')
        # Logo 1
        self.image('app/pdf_generator/resources/images/Logo_Tactalyse.png', 4, 2, 25)
        # Logo 2
        self.image('app/pdf_generator/resources/images/Logo_Tactalyse_Stats.png', 50, 7, 115)
        # Background
        self.image("app/pdf_generator/resources/images/BackgroundClean.png", x=0, y=30, w=self.w, h=self.h)
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
        self.cell(0, 14, "Stats Report for " + self.player.get_player_name(), 0, 1, 'C', False)
        self.ln(4)

    def print_player_info_label(self, start_x_pos, start_y_pos, end_pos, label, y_offset):
        self.set_text_color(255, 77, 77)
        self.set_xy(start_x_pos, start_y_pos + y_offset)
        self.cell(0, 20, label, ln = 1)
        self.set_text_color(0, 0, 0)
        self.set_xy(start_x_pos + end_pos, start_y_pos + y_offset)


    def print_player_info_col1(self):

        start_x_pos = 45.0
        start_y_pos = 150.0
        end_pos = 30

        self.print_player_info_label(start_x_pos, start_y_pos, end_pos, 'POSITION: ', 0)
        self.cell(0, 20, self.player.get_player_position(), ln = 1)

        self.print_player_info_label(start_x_pos, start_y_pos, end_pos, 'CLUB: ', 10)
        self.cell(0, 20, self.player.get_player_club(), ln = 1)

        self.print_player_info_label(start_x_pos, start_y_pos, end_pos, 'ON LOAN: ', 20)
        self.cell(0, 20, self.player.get_player_on_loan(), ln = 1)

        self.print_player_info_label(start_x_pos, start_y_pos, end_pos, 'CONTRACT EXPIRES ON: ', 30)
        self.set_xy(start_x_pos + end_pos + 35, start_y_pos + 30)
        self.cell(0, 20, self.player.get_player_contract_date(), ln =1)

        self.print_player_info_label(start_x_pos, start_y_pos, end_pos, 'COUNTRY: ', 60)
        self.cell(0, 20, self.player.get_player_country(), ln =1)

        self.print_player_info_label(start_x_pos, start_y_pos, end_pos, 'HEIGHT: ', 70)
        self.cell(0, 20, self.player.get_player_height() + "cm", ln =1)

        self.print_player_info_label(start_x_pos, start_y_pos, end_pos, 'FOOT: ', 80)
        self.cell(0, 20, self.player.get_player_foot(), ln =1)

    def print_player_info_col2(self):

        start_x2_pos = 125.0
        start_y2_pos = 150.0
        end_pos = 30

        self.print_player_info_label(start_x2_pos, start_y2_pos, end_pos, 'LEAGUE: ', 0)
        self.cell(0, 20, self.player.get_player_league(), ln =1)

        self.print_player_info_label(start_x2_pos, start_y2_pos, end_pos, '#MATCHES: ', 10)
        self.cell(0, 20, self.player.get_player_num_matches(), ln =1)

        # There's no information about the agent in the excel files
        # (might be necessary to have that passed from the frontend?)

        #self.print_player_info_label(start_x2_pos, start_y2_pos, end_pos, 'AGENT: ', 20)
        #self.cell(0, 20, self.__player_agent, ln =1)

        self.print_player_info_label(start_x2_pos, start_y2_pos, end_pos, 'AGE: ', 60)
        self.cell(0, 20, self.player.get_player_age(), ln =1)

        self.print_player_info_label(start_x2_pos, start_y2_pos, end_pos, 'WEIGHT: ', 70)
        self.cell(0, 20, self.player.get_player_weight() + "kg", ln =1)

    # print player's image and basic information in the first page
    def print_basic_player_info(self):
        self.image('app/pdf_generator/resources/images/placeholder_player_photo.jpg', 50, 60, 115)
        self.set_font('Arial', 'B', 14)

        # First column
        self.print_player_info_col1()
        self.print_player_info_col2()

    def print_plot(self, plot):
        img = Image.open(io.BytesIO(plot))
        self.image(img, 50, 70, 115)
