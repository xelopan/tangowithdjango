from django.db import models

class TagField(models.TextField):
    description = "Stores tags in a single database column"

    __metaclass__ = models.SubfieldBase

    def __init__(self, delimiter="|", *args, **kwargs):
        self.delimiter = delimiter
        super(TagField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, list):
            return value

        return value.split(self.delimiter)

    def get_prep_value(self, value):
        return self.delimiter.join(value)

from south.modelsinspector import add_introspection_rules
add_introspection_rules([
    (
        [TagField],
        [],
        {
            'delimiter': ['delimiter', {'default': "|"}],
        },
    ),
], [
    "^southtut\.fields\.TagField"])

class UpperCaseField(models.TextField):
    "Makes sure its content is always upper-case"

    def to_python(self, value):
        return value.upper()

    def get_prep_value(self, value):
        return value.upper()

add_introspection_rules([], ["^southtut\.fields\.UpperCaseField"])
