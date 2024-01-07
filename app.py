#!/usr/bin/env python3

import connexion
from modules.encoder import JSONEncoder
import os
import sys
import logging
from distutils.util import strtobool

from modules.settings import Settings

def app_specific(connexion_app):
    """ Add additional or initialize specifc app functionality
        Args:
            connexion_app (connexion.App): The app
        Returns:
            App (connexion.App): The app
    """
    # if 'nose' not in sys.modules.keys():
    #     settings = Settings('settings.yml')
    # else:
    #     settings = Settings('test_settings.yml')
    settings = Settings('settings.yml')
    connexion_app.app.settings = settings

    return connexion_app


def create_app():
    # Setup the swagger ui console
    # https://github.com/zalando/connexion#the-swagger-ui-console
    dir_path = os.path.dirname(os.path.realpath(__file__))
    #options = {'swagger_path': f"{dir_path}/swagger-ui-3.25.5/dist/"}
    # create the app
    app = connexion.App(__name__,
                        specification_dir='./swagger_server/swagger/')
    # add the api yaml
    app.add_api('swagger.yaml',
                arguments={'title': 'Games Library API'})

    # setup custom json_encoder
    app.app.json_encoder = JSONEncoder

    # add our settings
    app = app_specific(app)
    app.app.logger.setLevel(logging.INFO)

    return app


if __name__ == '__main__':
    app = create_app()
    debug_val = app.app.settings.app_debug
    if not isinstance(debug_val, bool):
        debug_val = bool(strtobool(str(debug_val)))
    app.run(host='0.0.0.0', port=8080)