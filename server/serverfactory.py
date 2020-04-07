from flask import Flask, redirect
from flask_restful import Api
from werkzeug.exceptions import NotFound
from server.errors import NotFoundError
from server.routes import init_routes


class ServerFactory:
    def __init__(self):
        """
        Init server-factory
        """
        self.name = 'aiven-server'
        self.static_folder = './static'

        self.app = None
        self.api = None

    def up(self):
        """
        Initializes flask.
        :return: The flask-app
        """
        self.app = Flask(self.name, static_folder=self.static_folder)
        self.set_up_api()
        return self.app

    def set_up_api(self):
        """
        Sets up the flask-restful api
        :return: None
        """
        self.api = Api(self.app)
        self.set_up_routes()

    def set_up_routes(self):
        init_routes(self.api)
        self.set_up_static_file_serving()

    def set_up_static_file_serving(self):
        @self.app.route('/<path:path>')
        def static_file(path):
            try:
                return self.app.send_static_file(path)
            except NotFound:
                raise NotFoundError()

        @self.app.route('/')
        def static_index():
            return redirect('/index.html')
