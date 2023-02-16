import datetime

from fpdf import FPDF  # install fpdf package to allow pdf creation
import os
import io
from dateutil.relativedelta import relativedelta
import math
import config


class PDF(FPDF):
    """
    PDF class corresponding to the format provided by Tactalyse

    @author: Maksym Kadiri
    @author: Pierre Chang
    """

    # Note PDF is 210 x 297 mm
    path = os.getcwd()

    def rectangle(self):
        self.set_line_width(0.1)
        self.set_fill_color(169, 169, 169)  # color for outer rectangle
        self.rect(5, 5, 200, 287, 'DF')
        self.set_fill_color(255, 255, 255)  # color for inner rectangle: white
        self.rect(8, 8, 194, 281, 'FD')

    # Add the selected image of the player
    def addImage(self, name):
        self.image(name=name, link='', type='', x=5, y=60, w=55)

    # Title of the pdf document
    def addTitle(self):
        self.set_xy(0.0, 0.0)
        self.set_font('Arial', 'B', 20)
        self.set_text_color(0, 0, 0)
        self.cell(w=210.0, h=40.0, align='C', txt="Stats report", border=0)

    # Add name of the player selected
    def addName(self, name):
        self.set_xy(65, 45)
        self.set_font('Arial', '', 20)
        self.set_text_color(0, 0, 0)
        self.cell(w=210.0, h=40.0, txt=name, border=0)

    # Fills the pdf with the data from the form
    def addStatistics(self, position, height, dob, agent, age, club, league, country):
        x_image_start = 65.0
        x_image_start2 = 30

        x_column_two = 70

        self.set_text_color(195, 37, 37)
        self.set_font('Helvetica', 'B', 14)

        ###############
        # First column
        ###############

        self.set_xy(x_image_start, 70.0)
        self.cell(0, 20, 'POSITION: ', ln=1)

        self.set_xy(x_image_start, 80.0)
        self.cell(0, 20, 'HEIGHT: ', ln=1)

        self.set_xy(x_image_start, 90.0)
        self.cell(0, 20, 'DOB: ', ln=1)

        self.set_xy(x_image_start, 100.0)
        self.cell(0, 20, 'AGENT: ', ln=1)

        ###############
        # Second column
        ###############

        self.set_xy(x_image_start + x_column_two, 70.0)
        self.cell(0, 20, 'AGE: ', ln=1)

        self.set_xy(x_image_start + x_column_two, 80.0)
        self.cell(0, 20, 'CLUB: ', ln=1)

        self.set_xy(x_image_start + x_column_two, 90.0)
        self.cell(0, 20, 'LEAGUE: ', ln=1)

        self.set_xy(x_image_start + x_column_two, 100.0)
        self.cell(0, 20, 'COUNTRY: ', ln=1)

        ###############
        # First column variables
        ###############
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'B', 12)

        self.set_xy(x_image_start + x_image_start2, 70.0)
        self.cell(0, 20, position, ln=1)

        self.set_xy(x_image_start + x_image_start2, 80.0)
        self.cell(0, 20, height, ln=1)

        self.set_xy(x_image_start + x_image_start2, 90.0)
        self.cell(0, 20, dob.strftime("%x"), ln=1)

        self.set_xy(x_image_start + x_image_start2, 100.0)
        self.cell(0, 20, agent, ln=1)

        ###############
        # Second column variables
        ###############
        self.set_xy(x_image_start + x_column_two + x_image_start2, 70)
        self.cell(0, 20, str(age), ln=1)

        self.set_xy(x_image_start + x_column_two + x_image_start2, 80)
        self.cell(0, 20, club, ln=1)

        self.set_xy(x_image_start + x_column_two + x_image_start2, 90)
        self.cell(0, 20, league, ln=1)

        self.set_xy(x_image_start + x_column_two + x_image_start2, 100)
        self.cell(0, 20, country, ln=1)

    # Adds  break line on the top of the from page of the document
    def line_cover(self, r, g, b):
        self.set_draw_color(r=r, g=g, b=b)
        self.set_line_width(width=1.05)
        self.line(x1=0, y1=47, x2=210, y2=47)
        self.ln(30)

    def header(self):
        self.image(name=self.path + "/app/Images/Background.png", x=0, y=0, w=self.w, h=self.h)

    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-20)
        # Select Arial italic 8
        self.set_font('Arial', '', 14)
        # Print centered page number
        self.cell(0, 20, str(self.page_no()), 0, 0, 'R')

    # Creates a subsection
    def section(self, name):
        self.set_font('Arial', 'B', 20)
        self.set_text_color(197, 37, 37)
        self.cell(w=210, h=40, txt=name, border=0)
        self.set_text_color(0, 0, 0)
        self.ln(25)

    # Function to place 2 pictures next to each other
    def two_images(self, name1, name2):

        x = self.x
        y = self.y
        self.image(name1, w=90, h=70)
        self.image(name2, x=x + 93, y=y, w=90, h=70)

    def single_graph(self, name):
        x = self.x
        y = self.y
        self.image(name, w=90, h=70)


##########################################################################################

def generate(app, portrait, radar_plot, folder_path):
    print("Generating pdf...")
    pdf = PDF(orientation='P', unit='mm', format='A4')

    # Page 1
    pdf.add_page(orientation='P')
    pdf.addImage(portrait)
    pdf.line_cover(197, 37, 37)
    pdf.addTitle()  # print the name of player on the top of the file

    pdf.addName(app.name)

    age = relativedelta(datetime.datetime.now(), app.dob).years

    pdf.addStatistics(app.position, app.height, app.dob, app.agent,
                      age, app.club, app.league, app.country)
    print("Page 1 generated")

    # Page 2
    pdf.add_page(orientation='P')
    pdf.line_cover(255, 255, 255)
    pdf.image(radar_plot, x=15, w=168, h=150)
    print("Page 2 generated")

    graphs_list_len = len(config.POSITIONAL_POINT_UNIX[app.position])
    pages_needed_graphs = math.ceil(graphs_list_len / 6)

    ind = 0
    for i in range(0, pages_needed_graphs):
        # Page 3
        pdf.add_page(orientation='P')
        pdf.line_cover(255, 255, 255)
        pdf.section("Stats Progression")
        #missing = []
        for j in range(0, 3):
            if ind + 1 < graphs_list_len:  # 0 1 2 3
                if os.getcwd()[0] == '/':
                    pdf.two_images(folder_path + "/" + config.POSITIONAL_POINT_UNIX[app.position][ind],
                                   folder_path + "/" + config.POSITIONAL_POINT_UNIX[app.position][ind + 1])
                    print(config.POSITIONAL_POINT_UNIX[app.position][ind]+' pdf '+config.POSITIONAL_POINT_UNIX[app.position][ind+1])

                else:
                    pdf.two_images(folder_path + "\\"+config.POSITIONAL_POINT_WINDOWS[app.position][ind],
                                   folder_path + "\\"+config.POSITIONAL_POINT_WINDOWS[app.position][ind+1])
                    print(config.POSITIONAL_POINT_UNIX[app.position][ind] + ' pdf ' +
                          config.POSITIONAL_POINT_UNIX[app.position][ind + 1])
                ind += 2
            elif ind < graphs_list_len:
                if os.getcwd()[0] == '/':
                    pdf.single_graph(folder_path + "/" + config.POSITIONAL_POINT_UNIX[app.position][ind])
                    print(config.POSITIONAL_POINT_UNIX[app.position][ind] + ' :pdf')
                else:
                    pdf.single_graph(folder_path + "\\"+config.POSITIONAL_POINT_WINDOWS[app.position][ind])
                    print(config.POSITIONAL_POINT_WINDOWS[app.position][ind] + ' :pdf')
                ind += 1

        print("Page " + str(3 + i) + " generated")
    #print(missing)
    print("\nEND")
    content = pdf.output(dest='S')

    return content
