import json
import click
import flask

from pprint import pprint


app = flask.Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def api():
    r = {
        "method": flask.request.method,
        "headers": dict(flask.request.headers),
        "args": dict(flask.request.args),
        "form": dict(flask.request.form),
        "json": flask.request.json,
        "get_json()": flask.request.get_json(),
    }

    pprint(r)
    return flask.Response(
        response=json.dumps(flask.request.get_json()),
        status=200,
        mimetype="application/json",
    )


@click.command()
@click.option("--host", "-h", default="127.0.0.1")
@click.option("--port", "-p", default=8000, type=int)
def echo_server(host, port):
    app.run(host=host, port=port)
