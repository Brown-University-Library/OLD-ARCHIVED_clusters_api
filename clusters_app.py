# -*- coding: utf-8 -*-

import datetime, json, os, pprint
import flask
from clusters_api.config import settings
from clusters_api.utils import logger_setup, grabber_handler


## setup
app = flask.Flask(__name__)
log = logger_setup.setup_logger()


@app.route( u'/summary_availability_api_v2/lib-all/', methods=['GET'] )
@app.route( u'/data/', methods=['GET'] )
def return_json():
    """ Returns already-produced json. """
    log.debug( u'- in clusters_app.return_json(); starting' )
    with open( settings.JSON_FILE_PATH ) as f:
        data_dict = json.loads( f.read() )
    return_dict = {
        u'info': { u'documentation': settings.DOCUMENTATION_URL },
        u'request': {
            u'requested_cluster_identifier': u'no longer used',
            u'time_of_request': unicode( datetime.datetime.now() ) },
        u'response': data_dict[u'counts'] }
    return_dict[u'response'][u'time_counts_last_updated'] = data_dict[u'datetime_updated']
    return flask.jsonify( return_dict )


@app.route( u'/update_data', methods=['POST'] )
def search():
    """ Builds json. """
    client_ip = flask.request.remote_addr
    if not client_ip in settings.LEGIT_IPS.keys():
        log.debug( u'- in clusters_app.search_new_request(); client_ip `%s` not in LEGIT_IPS; returning forbidden' % client_ip )
        return flask.abort( 403 )
    grabber = grabber_handler.Grabber( log )
    grabber.update_data()  # nothing really needs to be returned, but i'll redirect to the get-api for easy debugging
    redirect_url = flask.url_for( u'return_json' )
    return flask.redirect( redirect_url, code=303 )




if __name__ == u'__main__':
    if os.getenv( u'DEVBOX' ) == u'true':
        app.run( host=u'0.0.0.0', debug=True )
    else:
        app.run()
