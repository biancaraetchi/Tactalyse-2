from fpdf import FPDF
from PIL import Image
import io


class PDF(FPDF):

    __player_name = "A. Masina"
    __player_position = "Winger"
    __player_height = "temp1"
    __player_agent = "temp2"
    __player_age = "temp3"
    __player_country = "temp4"
    __player_agent = "temp5"
    __player_club = "temp6"
    __player_league = "temp7"
    __player_weight = "temp8"
    __player_foot = "temp9"
    __player_on_loan = "yes"
    __player_contract_date = "temp10"
    __player_num_matches = "10"

    def set_personal_info(self, player_name, league_df):
        self.__player_name = player_name
        self.__player_height = str(league_df.loc[league_df['Player'] == player_name, 'Height'].values[0])
        self.__player_age = str(league_df.loc[league_df['Player'] == player_name, 'Age'].values[0])
        self.__player_country = league_df.loc[league_df['Player'] == player_name, 'Birth country'].values[0]
        self.__player_weight = str(league_df.loc[league_df['Player'] == player_name, 'Weight'].values[0])

    def set_football_info(self, player_name, league_df, position):
        self.__player_position = position
        self.__player_club = league_df.loc[league_df['Player'] == player_name, 'Team'].values[0]
        self.__player_league = "ENG2"
        self.__player_foot = league_df.loc[league_df['Player'] == player_name, 'Foot'].values[0]
        self.__player_on_loan = league_df.loc[league_df['Player'] == player_name, 'On loan'].values[0]
        self.__player_contract_date = league_df.loc[league_df['Player'] == player_name, 'Contract expires'].values[0]
        self.__player_num_matches = str(league_df.loc[league_df['Player'] == player_name, 'Matches played'].values[0])

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
        self.cell(0, 14, "Stats Report for " + self.__player_name, 0, 1, 'C', False)
        self.ln(4)

    def print_player_info_col1(self):
        end_pos = 30
        start_x_pos = 50.0
        start_y_pos = 150.0
        self.set_xy(start_x_pos, start_y_pos)
        self.cell(0, 20, 'POSITION: ', ln = 1)
        self.set_xy(start_x_pos + end_pos, start_y_pos)
        self.cell(0, 20, self.__player_position, ln = 1)

        self.set_xy(start_x_pos, start_y_pos + 10)
        self.cell(0, 20, 'CLUB: ', ln = 1)
        self.set_xy(start_x_pos + end_pos, start_y_pos + 10)
        self.cell(0, 20, self.__player_club, ln = 1)

        self.set_xy(start_x_pos, start_y_pos + 20)
        self.cell(0, 20, 'ON LOAN: ', ln = 1)
        self.set_xy(start_x_pos + end_pos, start_y_pos + 20)
        self.cell(0, 20, self.__player_on_loan, ln = 1)

        self.set_xy(start_x_pos, start_y_pos + 30)
        self.cell(0, 20, 'CONTRACT EXPIRES ON: ', ln = 1)
        self.set_xy(start_x_pos + end_pos + 35, start_y_pos + 30)
        self.cell(0, 20, self.__player_contract_date, ln =1)

        self.set_xy(start_x_pos, start_y_pos + 60)
        self.cell(0, 20, 'COUNTRY: ', ln = 1)
        self.set_xy(start_x_pos + end_pos, start_y_pos + 60)
        self.cell(0, 20, self.__player_country, ln =1)

        self.set_xy(start_x_pos, start_y_pos + 70)
        self.cell(0, 20, 'HEIGHT: ', ln = 1)
        self.set_xy(start_x_pos + end_pos, start_y_pos + 70)
        print(self.__player_height)
        self.cell(0, 20, self.__player_height + "cm", ln =1)

        self.set_xy(start_x_pos, start_y_pos + 80)
        self.cell(0, 20, 'FOOT: ', ln = 1)
        self.set_xy(start_x_pos + end_pos, start_y_pos + 80)
        self.cell(0, 20, self.__player_foot, ln =1)

    def print_player_info_col2(self):
        end_pos = 30
        start_x2_pos = 120.0
        start_y2_pos = 150.0

        self.set_xy(start_x2_pos, start_y2_pos)
        self.cell(0, 20, 'LEAGUE: ', ln = 1)
        self.set_xy(start_x2_pos + end_pos, start_y2_pos)
        self.cell(0, 20, self.__player_league, ln =1)

        self.set_xy(start_x2_pos, start_y2_pos + 10)
        self.cell(0, 20, 'AGENT: ', ln = 1)
        self.set_xy(start_x2_pos + end_pos, start_y2_pos + 10)
        self.cell(0, 20, self.__player_agent, ln =1)

        self.set_xy(start_x2_pos, start_y2_pos + 20)
        self.cell(0, 20, '#MATCHES: ', ln = 1)
        self.set_xy(start_x2_pos + end_pos, start_y2_pos + 20)
        self.cell(0, 20, self.__player_num_matches, ln =1)

        self.set_xy(start_x2_pos, start_y2_pos + 60)
        self.cell(0, 20, 'AGE: ', ln = 1)
        self.set_xy(start_x2_pos + end_pos, start_y2_pos + 60)
        self.cell(0, 20, self.__player_age, ln =1)

        self.set_xy(start_x2_pos, start_y2_pos + 70)
        self.cell(0, 20, 'WEIGHT: ', ln = 1)
        self.set_xy(start_x2_pos + end_pos, start_y2_pos + 70)
        self.cell(0, 20, self.__player_weight + "kg", ln =1)

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
