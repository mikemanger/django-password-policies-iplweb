from password_policies.conf import settings
from password_policies.models import PasswordHistory


def password_status(request):
    """
Adds a variable determining the state of a user's password
to the context if the user has authenticated:

* ``password_change_required``
    Determines if the user needs to change his/her password.

    Set to ``True`` if the user has to change his/her password,
    ``False`` otherwise.

To use it add it to the list of ``TEMPLATE_CONTEXT_PROCESSORS``
in a project's settings file::

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.contrib.messages.context_processors.messages',
        'password_policies.context_processors.password_status',
    )
"""
    d = {}
    auth = request.user.is_authenticated
    if callable(auth):  # Before Django 1.10
        auth = auth()

    if auth:
        if settings.PASSWORD_POLICIES_CHANGE_REQUIRED_SESSION_KEY not in request.session:
            r = PasswordHistory.objects.change_required(request.user)
        else:
            r = request.session[settings.PASSWORD_POLICIES_CHANGE_REQUIRED_SESSION_KEY]
        d['password_change_required'] = r
    return d
