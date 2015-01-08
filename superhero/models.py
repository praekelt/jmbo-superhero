from django.utils.translation import ugettext as _

from jmbo.models import ModelBase


class Superhero(ModelBase):

    class Meta:
        verbose_name_plural = _("Superheroes")
