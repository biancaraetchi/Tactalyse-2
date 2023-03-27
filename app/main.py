from flask import Flask

# initiating app
app = Flask(__name__)

# for now, I'll add a basic route just to test it out
@app.route("/")
def initiate_app():
    return "here"