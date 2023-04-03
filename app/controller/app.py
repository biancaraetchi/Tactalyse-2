from flask import Flask, request, Response, make_response

from .data_service import get_league_data, get_player_data
from .graph_service import create_radio_chart, create_line_plot
from .pdf_service import create_pdf

app = Flask(__name__)


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
        return Response("Error: invalid JSON payload.", 400, mimetype='application/json')

    league_file = request.json.get('league-file')
    player_file = request.json.get('player-file')
    player_name = request.json.get('player-name')
    start_date = request.json.get('start-date')
    end_date = request.json.get('end-date')

    if not league_file:
        return Response("Error: league-file was not sent.", 400, mimetype='application/json')
    elif not player_file:
        return Response("Error: player-file was not sent.", 400, mimetype='application/json')
    elif not player_name:
        return Response("Error: player-name was not specified.", 400, mimetype='application/json')

    return pass_data(league_file, player_file, player_name, start_date, end_date)


def key_value_process(files, form):
    """
    Function that handles a request to the PDF generator API endpoint if it is of another format than json.

    :param files: The files included in the API request.
    :param form: The other key-value pairs included in the API request.
    :return: A response either containing an error message, or the generated PDF in byte representation.
    """
    if 'league-file' not in files:
        return Response("Error: league file was not sent.", 400, mimetype='application/json')
    elif 'player-file' not in files:
        return Response("Error: player file was not sent.", 400, mimetype='application/json')
    elif 'player-name' not in form:
        return Response("Error: player name was not specified.", 400, mimetype='application/json')

    league_file = files['league-file']
    player_file = files['player-file']
    player_name = form['player-name']
    start_date = form.get('start-date')
    end_date = form.get('end-date')

    return pass_data(league_file, player_file, player_name, start_date, end_date)


def pass_data(league_file, player_file, player_name, start_date, end_date):
    """
    Function that passes the received data to the appropriate services, and generates a PDF.

    :param league_file: Excel file containing football league data.
    :param player_file: Excel file containing player match data.
    :param player_name: Name of the player to generate a report for.
    :param start_date: Start date of Tactalyse's services for the player.
    :param end_date: End date of Tactalyse's services for the player.
    :return: A response containing the generated PDF in byte representation.
    """
    player_row, columns_radio_chart, main_pos_long, main_pos = get_league_data(league_file, player_name)
    player_data, columns_line_plot = get_player_data(player_file, main_pos)

    radar_chart = create_radio_chart(main_pos_long, player_row, columns_radio_chart)
    line_plot = create_line_plot(None, player_data, columns_line_plot)

    pdf_bytes = create_pdf(player_row, player_name, main_pos_long, radar_chart, line_plot)

    response = make_response(pdf_bytes)
    response.headers.set('Content-Type', 'application/pdf')
    response.headers.set('Content-Disposition', 'attachment', filename=player_name + '.pdf')

    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
