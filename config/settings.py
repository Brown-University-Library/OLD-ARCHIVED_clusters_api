# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json, os


# file-logger
LOG_DIR = unicode( os.environ.get(u'clusters__LOG_DIR') )
LOG_LEVEL = unicode( os.environ.get(u'clusters__LOG_LEVEL') )

# web
DOCUMENTATION_URL = unicode(os.environ.get(u'clusters__DOCUMENTATION_URL'))
LEGIT_IPS = json.loads( unicode(os.environ.get(u'clusters__LEGIT_IPS')) )

# grabber
SOURCE_URL = unicode( os.environ.get(u'clusters__SOURCE_URL') )
JSON_FILE_PATH = unicode( os.environ.get(u'clusters__JSON_FILE_PATH') )

# end
