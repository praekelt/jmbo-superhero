from django import forms
from django.utils.translation import ugettext as _


class ImportForm(forms.Form):
    zip_file = forms.FileField(
        required=True,
        label=_("Zip file"),
        help_text=_("A zip file containing HTML, CSS, Javascript and images.")
    )

    def __init__(self, model, *args, **kwargs):
        super(ImportForm, self).__init__(*args, **kwargs)
        self.fieldsets = (
            (_("Import"), {"fields": ("zip_file", )}),
        )
