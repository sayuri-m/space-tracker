import os
import json
from flask import Flask
from flask import render_template
from flask import render_template_string
from .getLaunches import *
from flask import request
from .apiCaller import *

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def index():
        return render_template(
    'index.html',
    last_launch=apiCaller.request('latest'),
    next_launch=apiCaller.request('next'),
    upcoming_launches=apiCaller.request('upcoming'),
    past_launches=apiCaller.request('past')
    )

    @app.route('/latest', methods=['GET'])
    def latestRequest():
        return json.dumps([GetLaunches.getLastLaunch().__dict__]) , 200

    @app.route('/next', methods=['GET'])
    def nextRequest():
        return json.dumps([GetLaunches.getNextLaunch().__dict__]) , 200

    @app.route('/upcoming', methods=['GET'])
    def upcomingRequest():
        return json.dumps([launch.__dict__ for launch in GetLaunches.getUpcomingLaunch()]) , 200

    @app.route('/past', methods=['GET'])
    def pastRequests():
        return json.dumps([launch.__dict__ for launch in GetLaunches.getPastLaunch()]) , 200

    return app
