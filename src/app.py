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
        self.app.add_url_rule('/<short_url>', view_func=self.get, methods=['GET'])

    def shorten(self):
        data = request.get_json()
        url = data.get('url')
        # TODO proper response with empty url
        if not url:
            return "empty url"
        key = self.url_shortener.get_key()
        # TODO handle case where the put failed (internal server error)
        # TODO handle repeated key
        self.db.put(key, url)
        return "done"

    def get(self, short_url):
        # TODO handle case when db.get raise exception
        # TODO handle case when db.get return nothing
        url = self.db.get(short_url)
        return redirect(url)

    def run(self):
        self.app.run()
