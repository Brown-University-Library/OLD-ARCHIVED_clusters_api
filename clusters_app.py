# -*- coding: utf-8 -*-

import datetime, json, os
import flask
from clusters_api.config import settings
from clusters_api.utils import logger_setup, grabber_handler


## setup
app = flask.Flask(__name__)
log = logger_setup.setup_logger()


@app.route( u'/clusters_api', methods=['GET'] )
def return_json():
    """ Returns already-produced json.
        TODO: build out. """
    jstring = get-the-file
    jdict = json.loads( jstring )
    return_dict = {
        u'datetime': datetime.datetime.now(),
        u'info': 'wiki url',
        u'response': jdict
        }
    return flask.jsonify( return_dict )


@app.route( u'/update_data', methods=['POST'] )
def search():
    """ Builds json.
        TODO: build out. """
    client_ip = flask.request.remote_addr
    if not client_ip in settings.LEGIT_IPS.keys():
        log.debug( u'- in clusters_app.search_new_request(); client_ip `%s` not in LEGIT_IPS; returning forbidden' % client_ip )
        return flask.abort( 403 )
    grabber = grabber_handler.Grabber( log )
    grabber.update_data()  # this is the work; nothing really needs to be returned. I could just redirect to a clusters_api() call for the produced data.
    return flask.some-redirect-function-call( ./clusters_api )




if __name__ == '__main__':
    if os.getenv('DEVBOX') == 'true':
        app.run( host='0.0.0.0', debug=True )
    else:
        app.run()
