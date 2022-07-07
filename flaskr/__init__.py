import os

from flask import Flask
from flask import render_template
from flask import render_template_string
from .getLaunches import *


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template('index.html',
    last_launch=GetLaunches.getLastLaunch(),
    next_launch=GetLaunches.getNextLaunch(),
    upcoming_launches=GetLaunches.getUpcomingLaunch(),
    past_launches=GetLaunches.getPastLaunch()
    )

    @app.route('/past-launches')
    def pastLaunches():
        return render_template('past-launches.html')

    @app.route('/upcoming-launches')
    def upcomingLaunches():
        return render_template('upcoming-launches.html')

    return app
