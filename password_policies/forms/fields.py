from django import forms

from password_policies.forms import validators


class PasswordPoliciesField(forms.CharField):
    """
    A form field that validates a password using :ref:`api-validators`."""

    default_validators = [
        validators.validate_common_sequences,
        validators.validate_consecutive_count,
        validators.validate_cracklib,
        validators.validate_dictionary_words,
        validators.validate_letter_count,
        validators.validate_lowercase_letter_count,
        validators.validate_uppercase_letter_count,
        validators.validate_number_count,
        validators.validate_symbol_count,
        validators.validate_entropy,
        validators.validate_not_email,
    ]

    def __init__(self, *args, **kwargs):
        if "widget" not in kwargs:
            kwargs["widget"] = forms.PasswordInput(render_value=False)
        super().__init__(*args, **kwargs)
