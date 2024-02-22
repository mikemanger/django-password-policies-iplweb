def is_authenticated(user):
    if user:
        return user.is_authenticated
    return False
