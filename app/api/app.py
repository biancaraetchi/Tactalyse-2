from flask import Flask, request, Response
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

    # pass everything to graphs
    # pass everything to pdfs

    response = Response(response_text, status=code, mimetype='application/json')

    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
