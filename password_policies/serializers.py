import json
from django.core.serializers.json import DjangoJSONEncoder

class JSONSerializer:
    """
    Simple wrapper around json to be used in signing.dumps and
    signing.loads.
    """
    def dumps(self, obj):

        return json.dumps(
            obj,
            separators=(',', ':'),
            sort_keys=True,
            indent=1,
            cls=DjangoJSONEncoder
        ).encode('latin-1')

    def loads(self, data):
        return json.loads(data.decode('latin-1'))
