VERSION = (0, 8, 3)

__version__ = "%s.%s.%s" % VERSION

def get_version():
    return "{0}.{1}".format(*VERSION)
