from django.db import models
from django.db.models.fields import NOT_PROVIDED

_core_model_field_attr = {
    "blank": False,
    "choices": [],
    "db_column": None,
    "db_index": False,
    "db_tablespace": None,
    "default": NOT_PROVIDED,
    "editable": True,
    "error_messages": None,
    "help_text": None,
    "null": False,
    "primary_key": False,
    "unique": False,
    "validators": None,
    "verbose_name": None,
}

_model_fields = {
    "AutoField": _core_model_field_attr,
    "BigIntegerField": _core_model_field_attr,
    "BooleanField": _core_model_field_attr,
    "CharField": _core_model_field_attr,
    "CommaSeparatedIntegerField": _core_model_field_attr,
    "DateField": _core_model_field_attr,
    "DateTimeField": _core_model_field_attr,
    "DecimalField": _core_model_field_attr,
    "EmailField": _core_model_field_attr,
    "FileField": _core_model_field_attr,
    "FilePathField": _core_model_field_attr,
    "FloatField": _core_model_field_attr,
    "ForeignKey": _core_model_field_attr,
    "GenericIPAddressField": _core_model_field_attr,
    "IPAddressField": _core_model_field_attr,
    "ImageField": _core_model_field_attr,
    "IntegerField": _core_model_field_attr,
    "ManyToManyField": _core_model_field_attr,
    "NullBooleanField": _core_model_field_attr,
    "OneToOneField": _core_model_field_attr,
    "PositiveIntegerField": _core_model_field_attr,
    "PositiveSmallIntegerField": _core_model_field_attr,
    "SlugField": _core_model_field_attr,
    "SmallIntegerField": _core_model_field_attr,
    "TextField": _core_model_field_attr,
    "TimeField": _core_model_field_attr,
    "URLField": _core_model_field_attr,
}

_add_model_attr = {
    "CharField": {"max_length": None},
    "CommaSeparatedIntegerField": {"max_length": None},
    "DateField": {
        "auto_now": False,
        "auto_now_add": False,
        "unique_for_date": None,
        "unique_for_month": None,
        "unique_for_year": None,
    },
    "DateTimeField": {
        "auto_now": False,
        "auto_now_add": False,
        "unique_for_date": None,
        "unique_for_month": None,
        "unique_for_year": None,
    },
    "DecimalField": {"max_digits": None, "decimal_places": None},
    "EmailField": {"max_length": 75},
    "FileField": {"max_length": 100, "upload_to": None, "storage": None},
    "FilePathField": {
        "allow_files": True,
        "allow_folders": False,
        "match": None,
        "path": None,
        "recursive": False,
    },
    "ForeignKey": {
        "limit_choices_to": None,
        "on_delete": models.CASCADE,
        "related_name": None,
        "to_field": None,
    },
    "GenericIPAddressField": {"protocol": "both", "unpack_ipv4": False},
    "ImageField": {
        "max_length": 100,
        "upload_to": None,
        "height_field": None,
        "width_field": None,
    },
    "OneToOneField": {},
    "SlugField": {"max_length": 50},
    "TimeField": {
        "auto_now": False,
        "auto_now_add": False,
        "unique_for_date": None,
        "unique_for_month": None,
        "unique_for_year": None,
    },
    "URLField": {"max_length": 200},
}

for k, v in _add_model_attr.items():
    _model_fields[k] = dict(_model_fields[k], **v)

model_fields = _model_fields


model_meta_fields = {
    "abstract": False,
    "db_tablespace": "",
    "get_latest_by": None,
    "managed": True,
    "order_with_respect_to": None,
    "ordering": None,
    "permissions": [],
    "proxy": False,
    "unique_together": [],
    "verbose_name": None,
    "verbose_name_plural": None,
}

_core_form_field_attr = {
    "required": True,
    "label": None,
    "initial": None,
    "widget": None,
    "help_text": None,
    "error_messages": None,
    "localize": False,
    "validators": None,
}

_form_fields = {
    "BooleanField": _core_form_field_attr,
    "CharField": _core_form_field_attr,
    "ChoiceField": _core_form_field_attr,
    "DateField": _core_form_field_attr,
    "DateTimeField": _core_form_field_attr,
    "DecimalField": _core_form_field_attr,
    "EmailField": _core_form_field_attr,
    "FileField": _core_form_field_attr,
    "FilePathField": _core_form_field_attr,
    "FloatField": _core_form_field_attr,
    "GenericIPAddressField": _core_form_field_attr,
    "IPAddressField": _core_form_field_attr,
    "ImageField": _core_form_field_attr,
    "IntegerField": _core_form_field_attr,
    "MultipleChoiceField": _core_form_field_attr,
    "NullBooleanField": _core_form_field_attr,
    "RegexField": _core_form_field_attr,
    "SlugField": _core_form_field_attr,
    "TimeField": _core_form_field_attr,
    "TypedChoiceField": _core_form_field_attr,
    "TypedMultipleChoiceField": _core_form_field_attr,
    "URLField": _core_form_field_attr,
}

_add_form_attr = {
    "CharField": {"max_length": None, "min_length": None},
    "ChoiceField": {"choices": None},
    "DateField": {"input_formats": None},
    "DateTimeField": {"input_formats": None},
    "DecimalField": {
        "max_value": None,
        "min_value": None,
        "max_digits": None,
        "decimal_places": None,
    },
    "EmailField": {"max_length": None, "min_length": None},
    "FileField": {"max_length": None, "allow_empty_file": False},
    "FilePathField": {
        "allow_files": True,
        "allow_folders": False,
        "match": None,
        "path": None,
        "recursive": False,
    },
    "FloatField": {"max_value": None, "min_value": None},
    "GenericIPAddressField": {"protocol": "both", "unpack_ipv4": False},
    "IntegerField": {"max_value": None, "min_value": None},
    "MultipleChoiceField": {"choices": None},
    "RegexField": {"regex": None},
    "TimeField": _core_form_field_attr,
    "TypedChoiceField": {"choices": None, "empty_value": None, "coerce": None},
    "TypedMultipleChoiceField": {"choices": None, "empty_value": None, "coerce": None},
    "URLField": {"max_length": None, "min_length": None},
}


for k, v in _add_form_attr.items():
    _form_fields[k] = dict(_form_fields[k], **v)

form_fields = _form_fields
