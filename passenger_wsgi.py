import os, sys
sys.path.insert(0, '/home/m/megbytfi/megbytfi.beget.tech/coolsite')
sys.path.insert(1, '/home/m/megbytfi/megbytfi.beget.tech/djangoenv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'coolsite.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()