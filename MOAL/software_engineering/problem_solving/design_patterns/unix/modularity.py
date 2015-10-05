# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())


DEBUG = True if __name__ == '__main__' else False


# NOT Modular ------------------------------------------------------------------

class BigBloatedAppClass:

    def respond(self, *args, **kwargs):
        pass

    def request(self, *args, **kwargs):
        pass

    def render(self, *args, **kwargs):
        pass

    def render_to_json(self, *args, **kwargs):
        pass

    def route(self, *args, **kwargs):
        pass

    def parse_route(self, *args, **kwargs):
        pass

    def get_params(self, *args, **kwargs):
        pass

    def read_model(self, *args, **kwargs):
        pass

    def create_model(self, *args, **kwargs):
        pass

    def update_model(self, *args, **kwargs):
        pass

    def delete_model(self, *args, **kwargs):
        pass

    def upload(self, *args, **kwargs):
        pass

    def parse_template(self, *args, **kwargs):
        pass

    def get_static(self, *args, **kwargs):
        pass

    def authenticate(self, *args, **kwargs):
        pass

    def new_user(self, *args, **kwargs):
        pass


# Modular ----------------------------------------------------------------------

class AppView:
    """Handles the application request/response cycle"""

    def respond(self, *args, **kwargs):
        pass

    def request(self, *args, **kwargs):
        pass

    def stream(self, *args, **kwargs):
        pass


class FtpView(AppView):
    pass


class JsonView(AppView):
    pass


class HttpView(AppView):
    pass


class AppRenderer:

    def render(self, *args, **kwargs):
        pass

    def render_to_json(self, *args, **kwargs):
        pass

    def parse_template(self, *args, **kwargs):
        pass

    def get_static(self, *args, **kwargs):
        pass


class TemplateRenderer(AppRenderer):
    pass


class AppRouter:

    def route(self, *args, **kwargs):
        pass

    def parse_route(self, *args, **kwargs):
        pass

    def get_params(self, *args, **kwargs):
        pass

    def get_post(self, *args, **kwargs):
        pass


class AppModel:

    def read(self, *args, **kwargs):
        pass

    def create(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass


class AppAuthentication:

    def send_auth_link(self, *args, **kwargs):
        pass

    def authenticate(self, *args, **kwargs):
        pass

    def reset(self, *args, **kwargs):
        pass

    def update_password(self, *args, **kwargs):
        pass

    def new_user(self, *args, **kwargs):
        pass
