import os
import zipfile
from StringIO import StringIO
from tempfile import mkdtemp
import shutil

from django import forms
from django.utils.translation import ugettext as _
from django.contrib.sites.models import Site
from django.conf import settings

from superhero.fields import FileMultiField
from superhero.models import Superhero


class ImportForm(forms.Form):
    files = FileMultiField(
        required=True,
        label=_("Zip file(s)"),
        help_text=_("""One or more zip files containing HTML, CSS, Javascript \
and images. The top level of the zip file must contain an index.html else it is omitted.""")
    )

    def __init__(self, model, *args, **kwargs):
        super(ImportForm, self).__init__(*args, **kwargs)
        self.fieldsets = (
            (_("Import"), {"fields": ("files", )}),
        )

    def save(self, commit=True):
        result = []

        if self.cleaned_data["files"]:
            for item in self.cleaned_data["files"]:
                item.seek(0)
                to_add = []

                # Zip file?
                itemfp = StringIO(item.read())
                item.seek(0)
                try:
                    zfp = zipfile.ZipFile(itemfp, "r")
                except:
                    # zipfile does not raise a specific exception
                    continue
                else:
                    if not zfp.testzip():
                        # Skip if index.html not in top level of archive
                        if "index.html" not in zfp.namelist():
                            continue

                        # Ensure superhero directory exists
                        dir = os.path.join(settings.MEDIA_ROOT, "superhero")
                        if not os.path.exists(dir):
                            os.mkdir(dir)

                        name = ".".join(item.name.split(".")[:-1])
                        target = os.path.join(dir, name)

                        # Remove target if it exists because it may contain
                        # stale files
                        if os.path.exists(target):
                            shutil.rmtree(target)

                        zfp.extractall(path=target)

                        # Create or update object
                        try:
                            obj = Superhero.objects.get(name=name)
                        except Superhero.DoesNotExist:
                            obj = Superhero.objects.create(
                                title=name.capitalize(), name=name
                            )
                            obj.sites = Site.objects.all()
                            obj.save()

                        result.append(obj)

        return result
