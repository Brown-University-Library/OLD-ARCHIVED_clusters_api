# -*- coding: utf-8 -*-

""" Grabs html, parses, and saves json to disk. """

import datetime, json, pprint
import requests
from bs4 import BeautifulSoup
from clusters_api.config import settings


class Grabber(object):

    def __init__( self, log ):
        """ Sets up basics. """
        self.log = log
        self.parser = None
        self.parser = Parser( self.log )

    def update_data( self ):
        """ Accesses source html, parses it, and saves json to disk. """
        html = self._grab_html()
        clusters_dict = self.parser.parse_cluster_html( html )
        return

    def _grab_html( self ):
        """ Helper function.
            Grabs html and returns it. """
        r = requests.get( settings.SOURCE_URL )
        html = r.content.decode( u'utf-8' )
        return html


class Parser(object):

    def __init__( self, log ):
       """ Sets up basics. """
       self.log = log
       self.cluster_name_mapper = {  # source-html-name: api-name
            u'Rock 1st Floor': u'rock-level-1',
            u'Rock 2nd Floor': u'rock-level-2-main',
            u'Rock Grad': u'rock-level-2-grad',
            u'Friedman': u'scili-friedman',
            u'SciLi Mezz': u'scili-mezzanine'
            }

    def parse_cluster_html( self, html ):
        """ Takes source html.
            Parses out cluster data.
            Returns dict. """
        soup = BeautifulSoup( html, from_encoding=u'utf-8' )
        ul_element = soup.find( id=u'pubStats' )
        a_elements = ul_element.find_all( u'a' )
        data_dict = {}
        for a_element in a_elements:
            all_text = a_element.text
            count_text = a_element.find( u'span' ).text
            source_cluster_name = all_text[ 0:all_text.find(count_text) ]
            self.log.debug( u'- in grabber_handler.Parser.parse_cluster_html(); source_cluster_name, `%s`' % source_cluster_name )
            if source_cluster_name in self.cluster_name_mapper.keys():
                data_dict_key = self.cluster_name_mapper[ source_cluster_name ]
                parts = count_text.split( u'/' )
                ( calculated_available, total ) = ( parts[0], parts[1] )
                data_dict[ data_dict_key ] = { u'available': calculated_available, u'total': total }
        self.log.debug( u'- in grabber_handler.Parser.parse_cluster_html(); data_dict, `%s`' % pprint.pformat(data_dict) )
