import django

def is_authenticated(user):
    if user:
        if django.VERSION < (1, 10):
            return user.is_authenticated()
        return user.is_authenticated
    return False
