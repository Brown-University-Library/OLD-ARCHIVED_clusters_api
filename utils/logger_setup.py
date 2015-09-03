# -*- coding: utf-8 -*-

""" Handles log setup. """

from __future__ import unicode_literals
import logging, os, pprint
import logging.handlers
from clusters_api.config import settings


# <http://stackoverflow.com/questions/1407474/does-python-logging-handlers-rotatingfilehandler-allow-creation-of-a-group-writa>
class GroupWriteRotatingFileHandler( logging.handlers.RotatingFileHandler ):
    def _open(self):
        prevumask=os.umask(0o002)
        #os.fdopen(os.open('/path/to/file', os.O_WRONLY, 0600))
        rtv=logging.handlers.RotatingFileHandler._open(self)
        os.umask(prevumask)
        return rtv


def setup_logger():
    """ Returns a logger to write to a file. """
    filename = u'%s/clusters_api.log' % settings.LOG_DIR
    formatter = logging.Formatter( u'[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s' )
    logger = logging.getLogger( u'clusters_api' )
    level_dict = { u'debug': logging.DEBUG, u'info':logging.INFO }
    logger.setLevel( level_dict[settings.LOG_LEVEL] )
    file_handler = GroupWriteRotatingFileHandler( filename, maxBytes=(5*1024*1024), backupCount=1 )
    # file_handler = logging.handlers.RotatingFileHandler( filename, maxBytes=(5*1024*1024), backupCount=1 )
    file_handler.setFormatter( formatter )
    logger.addHandler( file_handler )
    return logger
