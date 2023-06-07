from flask import Flask, request, Response, make_response
from app.controller.data_service import DataService
from .graph_service import GraphService
from .pdf_service import PDFService

app = Flask(__name__)
mimetype='application/json'


@app.route('/pdf', methods=["POST"])
def generate_pdf():
    """
    API endpoint for generating a football report based on query parameters.
    The following parameters must be included in the request:
    - league-file: an Excel file containing football league data.
    - player-file: an Excel file containing a player's match data.
    - player-name: a string representing the name of the player. Must exist within the league file.
    Optional parameters include:
    - start-date: start date of Tactalyse's services for the player.
    - end-date: end date of Tactalyse's services for the player.

    :return: A response either containing an error message, or the generated PDF in byte representation.
    """
    if request.is_json:
        return json_process(request.get_json())
    else:
        return key_value_process(request.files, request.form)


def json_process(payload):
    """
    Function that handles a json-formatted request to the PDF generator API endpoint.

    :param payload: The json payload of the request.
    :return: A response either containing an error message, or the generated PDF in byte representation.
    """
    if payload is None:
        return Response("Error: invalid JSON payload.", 400, mimetype=mimetype)

    league_file = request.json.get('league-file')
    player_file = request.json.get('player-file')
    compare_file = request.json.get('compare-file')
    player_name = request.json.get('player-name')
    league_name = request.json.get('league-name')
    compare_name = request.json.get('compare-name')
    start_date = request.json.get('start-date')
    end_date = request.json.get('end-date')
    player_image = request.json.get('player-image')
    player_cmp_image = request.json.get('compare-image')

    if not league_file:
        return Response("Error: league-file was not sent.", 400, mimetype=mimetype)
    elif not player_file:
        return Response("Error: player-file was not sent.", 400, mimetype=mimetype)
    elif not player_name:
        return Response("Error: player-name was not specified.", 400, mimetype=mimetype)

    return pass_data(league_file, player_file, player_name, league_name, start_date, end_date, compare_file,
                     compare_name, player_image, player_cmp_image)


def key_value_process(files, form):
    """
    Function that handles a request to the PDF generator API endpoint if it is of another format than json.

    :param files: The files included in the API request.
    :param form: The other key-value pairs included in the API request.
    :return: A response either containing an error message, or the generated PDF in byte representation.
    """
    if 'league-file' not in files:
        return Response("Error: league file was not sent.", 400, mimetype=mimetype)
    elif 'player-file' not in files:
        return Response("Error: player file was not sent.", 400, mimetype=mimetype)
    elif 'player-name' not in form:
        return Response("Error: player name was not specified.", 400, mimetype=mimetype)

    league_file = files['league-file']
    player_file = files['player-file']
    compare_file = files.get('compare-file')
    league_name = files.get('league-name')
    player_name = form['player-name']
    compare_name = form.get('compare-name')
    start_date = form.get('start-date')
    end_date = form.get('end-date')
    player_image = form.get('player-image')
    player_cmp_image = form.get('compare-image')

    return pass_data(league_file, player_file, player_name, league_name, start_date, end_date, compare_file,
                     compare_name, player_image, player_cmp_image)


def pass_data(league_file, player_file, player_name, league_name, start_date, end_date, compare_file, compare_name,
              player_image, player_cmp_image):
    """
    Function that passes the received data to the appropriate services, and generates a PDF.

    :param league_file: Excel file containing football league data.
    :param player_file: Excel file containing the player's match data.
    :param player_name: Name of the player to generate a report for.
    :param start_date: Start date of Tactalyse's services for the player.
    :param end_date: End date of Tactalyse's services for the player.
    :param compare_file: Excel file containing match data for the player to compare with.
    :param compare_name: Name of the player to compare with.
    :return: A response containing the generated PDF in byte representation.
    """
    data_service = DataService()
    if compare_name and not data_service.both_in_league(league_file, player_name, compare_name):
        return Response("Error: The second player name was not found in the league file.", 400,
                        mimetype=mimetype)
    # Get parameter maps with relevant data for generating plots from the data module
    line_map = data_service.get_line_data(league_file, player_file, player_name, compare_file, compare_name, start_date, end_date)
    bar_map = data_service.get_bar_data(league_file, player_name, compare_name)

    # Pass the maps to get lists containing plots in byte form from the graph_generator module
    graph_service = GraphService()
    line_plots = graph_service.create_line_plots(line_map)
    bar_plot_set = graph_service.create_bar_plots(bar_map, 'v')

    # Get a parameter map with relevant data for generating a PDF from the data module, and pass it to the pdf_generator
    # module along with the graphs
    pdf_service = PDFService()
    pdf_map = data_service.get_pdf_data(league_file, player_name, league_name, compare_name, line_plots, bar_plot_set,
                                        player_image, player_cmp_image)
    pdf_bytes = pdf_service.create_pdf(pdf_map)

    response = make_response(bytes(pdf_bytes))
    response.headers.set('Content-Type', 'application/pdf')
    response.headers.set('Content-Disposition', 'attachment', filename=player_name + '.pdf')
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
