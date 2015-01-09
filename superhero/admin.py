from django.contrib import admin
from django import forms

from jmbo.admin import ModelBaseAdmin

from superhero.models import Superhero


class SuperheroForm(forms.ModelForm):

    class Meta:
        model = Superhero


class SuperheroAdmin(ModelBaseAdmin):
    form = SuperheroForm

    def get_fieldsets(self, request, obj=None):
        result = super(SuperheroAdmin, self).get_fieldsets(request, obj=obj)
        result = list(result)
        return tuple([result[0], result[2], result[3]])


admin.site.register(Superhero, SuperheroAdmin)
