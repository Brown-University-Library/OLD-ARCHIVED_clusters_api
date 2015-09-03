# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import datetime, json, os, pprint
import flask
from clusters_api.config import settings
from clusters_api.utils import logger_setup, grabber_handler


## setup
app = flask.Flask(__name__)
log = logger_setup.setup_logger()


# @app.route( '/summary_availability_api_v2/lib-all/', methods=['GET'] )  # /services/clusters/summary_availability_api_v2/lib-all/
@app.route( '/lib-all/', methods=['GET'] )  # /services/clusters/summary_availability_api_v2/lib-all/
@app.route( '/data/', methods=['GET'] )  # /clusters_api/data/
def return_json():
    """ Returns already-produced json. """
    log.debug( '- in clusters_app.return_json(); starting' )
    with open( settings.JSON_FILE_PATH ) as f:
        data_dict = json.loads( f.read() )
    return_dict = {
        'info': { 'documentation': settings.DOCUMENTATION_URL },
        'request': {
            'requested_cluster_identifier': 'no longer used',
            'time_of_request': unicode( datetime.datetime.now() ) },
        'response': data_dict['counts'] }
    return_dict['response']['time_counts_last_updated'] = data_dict['datetime_updated']
    return flask.jsonify( return_dict )


@app.route( '/update_data', methods=['POST'] )  # /clusters_api/update_data/
def search():
    """ Builds json.
        Note: normally grabber.update_data() is run from cron-script; this is just for testing.
        TODO: once server acls are set up, re-enable logging. """
    client_ip = flask.request.remote_addr
    if not client_ip in settings.LEGIT_IPS.keys():
        log.debug( '- in clusters_app.search_new_request(); client_ip `%s` not in LEGIT_IPS; returning forbidden' % client_ip )
        return flask.abort( 403 )
    grabber = grabber_handler.Grabber()
    # grabber = grabber_handler.Grabber( log )
    grabber.update_data()  # nothing really needs to be returned, but i'll redirect to the get-api for easy debugging
    redirect_url = flask.url_for( 'return_json' )
    return flask.redirect( redirect_url, code=303 )




if __name__ == '__main__':
    if os.getenv( 'DEVBOX' ) == 'true':
        app.run( host='0.0.0.0', debug=True )
    else:
        app.run()
