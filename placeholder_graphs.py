from app.controller.graph_service import create_radar_chart
from app.data.excel_reader import ExcelReader
from app.data.preprocessors.preprocessor import Preprocessor
from app.data.preprocessors.radar_processor import RadarProcessor

processor = Preprocessor()


def create_graph(leaguefile, playername):
    reader = ExcelReader()
    league = reader.league_data(leaguefile, playername)
    radar_map = {}

    radar_chart = create_radar_chart(radar_map)
    f = open('placeholders/bot_'+playername+'.png', 'wb')
    f.write(radar_chart)
    f.close()


def generate_placeholders():
    filepath = 'app/pdf_generator/resources/test_data/ENG2.xlsx'
    # create_graph(filepath, 'A. Masina')
    # create_graph(filepath, 'B. Foster')
    # create_graph(filepath, 'C. Cathcart')
    # create_graph(filepath, 'I. Sarr')
    # create_graph(filepath, 'João Pedro')
    # create_graph(filepath, 'K. Sema')
    # create_graph(filepath, 'Kiko Femenía')
    # create_graph(filepath, 'N. Chalobah')
    # create_graph(filepath, 'T. Cleverley')
    create_graph(filepath, 'W. Troost-Ekong')

