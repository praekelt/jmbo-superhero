from django.contrib import admin

from jmbo.admin import ModelBaseAdmin
from superhero.models import Superhero


admin.site.register(Superhero, ModelBaseAdmin)
