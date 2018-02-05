import sys
reload(sys)
sys.setdefaultencoding('utf8')

from markan.cli import markan
sys.exit(markan())
