import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FormHandling.settings')

# Run migrations automatically on startup
try:
    call_command('migrate', interactive=False)
except:
    pass

app = get_wsgi_application()
