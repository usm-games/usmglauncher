import json

from flask import Flask, abort, redirect, request, render_template
import subprocess

app = Flask(__name__)

with open("games.json") as fp:
    GAMES = json.load(fp)


class ProgramAlreadyRunningError(Exception):
    pass


current_program = None


def launch_from_path(path: str):
    global current_program
    if current_program is not None and current_program.poll() is None:
        raise ProgramAlreadyRunningError("A program is already running")
    current_program = subprocess.Popen([path])


@app.errorhandler(404)
def page_not_found(error):
    return r"<h1>Bad route: 404</h1>", 404


@app.route('/')
def main():
    has_error = request.args.get("error", False)

    return render_template("index.html")


@app.route('/launch/<launchid>')
def launch(launchid):
    launch_path = GAMES["paths"].get(launchid)
    if launch_path is None:
        abort(404)

    try:
        launch_from_path(launch_path)
    except ProgramAlreadyRunningError:
        return redirect('/?error=True')
    return redirect('/')

