from flask import Flask, request, Response, make_response

from controller.data_service import read_files_standard, get_main_position, get_column_names
from controller.graph_service import create_polar_plot
from controller.pdf_service import create_pdf
app = Flask(__name__)


@app.route('/pdf', methods=["POST"])
def generate_pdf():
    if request.is_json:
        return json_process(request.get_json())
    else:
        return key_value_process(request.files, request.form)


def json_process(payload):
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
    league_df, player_df = read_files_standard(league_file, player_file)
    columns = get_column_names(player_df)
    main_pos = get_main_position(league_df, player_name)

    plot = create_polar_plot(main_pos, player_df, columns)

    pdf_bytes = create_pdf(league_df, player_name, main_pos, plot)

    response = make_response(pdf_bytes)
    response.headers.set('Content-Type', 'application/pdf')
    response.headers.set('Content-Disposition', 'attachment', filename=player_name + '.pdf')

    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
