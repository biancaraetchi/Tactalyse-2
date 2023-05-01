import io

from PIL import Image
from fpdf import FPDF

from .player import Player


class PDF(FPDF):
    """
    Class representing the pdf for the player who the client has asked a report of.
    Its layout is defined by the class attributes and their values.
    It is a subclass of the already existing FPDF class within the FDPF library.
    Some methods therefore already existed within FPDF and have been overwritten. 
    :attribute __player: is an instance of the Player class and represents the current player
    for whom the pdf displays info
    :attribute __font: defines the main font used throughout the pdf
    """

    def __init__(self):
        super().__init__()
        self.__player = Player()
        self.__compare = Player()
        self.__font = 'Arial'
        self.__current_y = 70
        self.__img_w = 145
        self.__img_h = 100

    def set_info(self, player_name, league_df, main_pos):
        """
        Function that sets the information within the player object attribute by calling the Player
        class set methods.
        :param player_name: the player's name
        :param league_df: dataframe obtained from the league excel file through Pandas 
        :param main_pos: the player's main position within the team
        """
        self.__player.set_personal_info(player_name, league_df)
        self.__player.set_football_info(player_name, league_df, main_pos)

    def set_compare_info(self, player_name, league_df, main_pos):
        """
        Function that sets the information within the compare object attribute by calling the Player
        class set methods.
        :param player_name: the name of the player that is being compared to
        :param league_df: dataframe obtained from the league excel file through Pandas
        :param main_pos: the compared player's main position within the team
        """
        self.__compare.set_personal_info(player_name, league_df)
        self.__compare.set_football_info(player_name, league_df, main_pos)

    def header(self):
        """
        (Override)
        Function that defines the layout of the pdf's header section
        """
        # Banner
        self.rect(-1, -1, 250, 30, 'DF')
        # Logo 1
        self.image('app/pdf_generator/resources/images/Logo_Tactalyse.png', 4, 2, 25)
        # Logo 2
        self.image('app/pdf_generator/resources/images/Logo_Tactalyse_Stats.png', 50, 7, 115)
        # Background
        self.image("app/pdf_generator/resources/images/BackgroundClean.png", x=0, y=30, w=self.w, h=self.h)
        # Set font bold 15
        self.set_font(self.__font, 'B', 15)
        # Move to the right
        self.cell(80)
        # Line break
        self.ln(20)

    def footer(self):
        """
        (Override)
        Function that defines the layout of the pdf's footer section
        """
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Set font italic 8
        self.set_font(self.__font, 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def chapter_title(self, title):
        """
        Function that sets a new chapter's title
        :param title: The chapter's title
        """
        # Set font 12
        self.set_font(self.__font, '', 27)
        # Line break
        self.ln(8)
        # Title
        self.cell(0, 14, title, 'B', 1, 'C', False)
        # Line break
        self.ln(4)

    def chapter_body(self, text):
        """
        Function that sets a new chapter's text body
        :param text: The chapter's text body
        """
        # Read text file
        txt = text
        # Set font
        self.set_font(self.__font, '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()

    def print_chapter(self, title, text):
        """
        Function that creates a new chapter in a new page within the pdf.
        :param title: the new chapter's given title
        :param text: the new chapter's given text contents
        """
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(text)
        self.set_font(self.__font, '', 12)

    def print_title(self):
        """
        Function that sets the main title of the pdf using the player's name 
        """
        self.set_font(self.__font, '', 30)
        self.ln(8)
        self.cell(0, 14, "Stats Report for " + self.__player.get_player_name(), 0, 1, 'C', False)
        self.ln(4)

    def print_player_info_label(self, start_x_pos, start_y_pos, end_pos, label, y_offset, value):
        """
        Function that displays a given player's information onto the current page
        :param start_x_pos: the starting position of the player's information label on the x axis
        :param start_y_pos: the starting position of the player's information label on the y axis
        :param end_pos: the offset of the player's information label on the x axis
        :param label: the name of the specific information about the player
        :param end_pos: the offset of the player's information label on the y axis
        :param value: the content of such information about the player
        """
        self.set_text_color(255, 77, 77)
        self.set_xy(start_x_pos, start_y_pos + y_offset)
        self.cell(0, 20, label, ln=1)
        self.set_text_color(0, 0, 0)
        self.set_xy(start_x_pos + end_pos, start_y_pos + y_offset)
        self.cell(0, 20, value, ln=1)

    def print_player_info_col1(self, player):
        """
        Function that defines the layout of the first column of the player's information.
        The absolute position and the offset values for the labels within the A4 sheet of the pdf 
        are defined respectively by start_x_pos, start_y_pos and end_pos.
        """
        start_x_pos = 45.0
        start_y_pos = 150.0
        end_pos = 30

        self.print_player_info_label(start_x_pos, start_y_pos, end_pos, 'POSITION: ', 0, player.get_player_position())

        self.print_player_info_label(start_x_pos, start_y_pos, end_pos, 'CLUB: ', 10, player.get_player_club())

        self.print_player_info_label(start_x_pos, start_y_pos, end_pos, 'ON LOAN: ', 20, player.get_player_on_loan())

        self.print_player_info_label(start_x_pos, start_y_pos, end_pos + 35, 'CONTRACT EXPIRES ON: ', 30,
                                     player.get_player_contract_date())

        self.print_player_info_label(start_x_pos, start_y_pos, end_pos, 'COUNTRY: ', 60, player.get_player_country())

        self.print_player_info_label(start_x_pos, start_y_pos, end_pos, 'HEIGHT: ', 70, player.get_player_height())

        self.print_player_info_label(start_x_pos, start_y_pos, end_pos, 'FOOT: ', 80, player.get_player_foot())

    def print_player_info_col2(self, player):
        """
        Function that defines the layout of the second column of the player's information.
        The absolute position and the offset values for the labels within the A4 sheet of the pdf 
        are defined respectively by start_x2_pos, start_y2_pos and end_pos.
        """
        start_x2_pos = 125.0
        start_y2_pos = 150.0
        end_pos = 30

        self.print_player_info_label(start_x2_pos, start_y2_pos, end_pos, 'LEAGUE: ', 0, player.get_player_league())

        self.print_player_info_label(start_x2_pos, start_y2_pos, end_pos, '#MATCHES: ', 10,
                                     player.get_player_num_matches())

        self.print_player_info_label(start_x2_pos, start_y2_pos, end_pos, 'AGE: ', 60, player.get_player_age())

        self.print_player_info_label(start_x2_pos, start_y2_pos, end_pos, 'WEIGHT: ', 70, player.get_player_weight())

    def print_plot(self, plot):
        """
        Function that prints a given plot onto the pdf
        """
        img = Image.open(io.BytesIO(plot))

        if self.__current_y + self.__img_h > self.h:
            self.add_page()
            self.__current_y = 40

        # Print the image at the current y position
        x = (self.w - self.__img_w) / 2.0
        self.image(img, x, self.__current_y, self.__img_w, self.__img_h)

        # Update the current y position to be below the current image
        self.__current_y += self.__img_h + 10

    def set_plot_properties(self, width, height):
        """
        Function that sets the standard width and height of plots in the report
        """
        self.__img_w = width
        self.__img_h = height

    @property
    def font(self):
        return self.__font

    @property
    def player(self):
        return self.__player

    @property
    def compare(self):
        return self.__compare

    @property
    def current_y(self):
        return self.__current_y

    @property
    def img_w(self):
        return self.__img_w

    @property
    def img_h(self):
        return self.__img_w

    @current_y.setter
    def current_y(self, value):
        self.__current_y = value
