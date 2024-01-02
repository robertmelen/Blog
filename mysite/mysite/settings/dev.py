from .base import *
print("dev settings")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure---w*5k%q(t0_l%wg-nws!l1+x^6#$w*@s51&)tu%n-#s@zunj3"

# SECURITY WARNING: define the correct hosts in production!


ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
        "https://blog-production-bbba.up.railway.app"
    ]
    

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
