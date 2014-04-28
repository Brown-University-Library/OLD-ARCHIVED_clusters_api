# -*- coding: utf-8 -*-

import json, os


# coming
SOME_SETTING = unicode( os.environ.get(u'clusters__SOME_SETTING') )

# file-logger
LOG_DIR = unicode( os.environ.get(u'clusters__LOG_DIR') )
LOG_LEVEL = unicode( os.environ.get(u'clusters__LOG_LEVEL') )

# end
