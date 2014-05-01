# -*- coding: utf-8 -*-

import json, os


# auth
LEGIT_IPS = json.loads( unicode(os.environ.get(u'clusters__LEGIT_IPS')) )

# file-logger
LOG_DIR = unicode( os.environ.get(u'clusters__LOG_DIR') )
LOG_LEVEL = unicode( os.environ.get(u'clusters__LOG_LEVEL') )

# grabber
SOURCE_URL = unicode( os.environ.get(u'clusters__SOURCE_URL') )
JSON_FILE_PATH = unicode( os.environ.get(u'clusters__JSON_FILE_PATH') )

# end
