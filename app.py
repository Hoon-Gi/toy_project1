import flask

app = flask.Flast(__name__)

@app.route('/')
def hello_world():
    return 'plz activate'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')