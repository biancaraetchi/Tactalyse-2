from flask import Flask, request, Response
from controller.data_service import *
from controller.graph_service import *
from controller.pdf_service import *
import matplotlib.pyplot as plt
app = Flask(__name__)


@app.route('/pdf', methods=["POST"])
def generate_pdf():
    payload = request.get_json()

    if payload is None:
        return Response("Error: invalid JSON payload.", 400, mimetype='application/json')

    league_file = request.json.get('league-file')
    player_file = request.json.get('player-file')
    player_name = request.json.get('player-name')
    start_date = request.json.get('start-date')
    end_date = request.json.get('end-date')

    code = 400
    if not league_file:
        response_text = "Error: league-file was not included in the request."
    elif not player_file:
        response_text = "Error: player-file was not included in the request."
    elif not player_name:
        response_text = "Error: player-name was not included in the request."
    else:
        response_text = "Successfully called endpoint."
        code = 200

    league_df, player_df = read_files_standard(league_file, player_file)
    columns = get_column_names(player_df)
    main_pos = get_main_position(league_df, player_name)

    plot = create_polar_plot(main_pos, player_df, columns)

    response = Response(plot, status=code, mimetype='application/json')

    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
