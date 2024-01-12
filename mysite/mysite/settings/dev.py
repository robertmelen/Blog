from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: define the correct hosts in production!


ALLOWED_HOSTS = ['blog-production-bbba.up.railway.app', 'www.robs-blog.co.uk', 'robs-blog.co.uk', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = [
        "https://blog-production-bbba.up.railway.app", "https://*.robs-blog.co.uk"
    ]
    

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
 