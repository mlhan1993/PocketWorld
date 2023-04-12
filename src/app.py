from flask import Flask, request, redirect
from src.idGenerator import IDGenerator

class APPConfig:
    def __init__(self, server_id):
        self.server_id = server_id


class APP(object):

    def __init__(self, config, db):
        self.app = Flask("urlShortener")
        self.config = config
        self.db = db

        self.add_routes()
        self.server_id = self.config.server_id
        self.url_shortener = IDGenerator(self.server_id)

    def add_routes(self):
        self.app.add_url_rule('/shorten', view_func=self.shorten, methods=['POST'])
        self.app.add_url_rule('/', view_func=self.get, methods=['GET'])

    def shorten(self):
        url = request.form.get('url')
        key = self.url_shortener.get_key()
        print(key)
        return "done"

    def get(self):
        print(self.db.get("xyz"))
        url = "google.ca"
        return redirect(url)

    def run(self):
        self.app.run()
