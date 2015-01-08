from django import template
from django.contrib import messages
from django.contrib.admin import helpers
from django.shortcuts import render_to_response
from django.utils.translation import ugettext as _
from django.conf import settings

import object_tools

from superhero.forms import ImportForm
from superhero.models import Superhero


class SuperheroImport(object_tools.ObjectTool):
    name = "import"
    label = _("Import")
    help_text = _("Import a superhero bundle.")
    form_class = ImportForm

    #def save_data(self, data):
    #    pass

    def handle_import(self, form):
        #csv_file = form.files['csv_file']
        #self.save_data(data_dict)
        pass

    def view(self, request, extra_context=None, process_form=True):
        form = extra_context["form"]

        if form.is_valid() and process_form:
            self.handle_import(form)
            message = _("The superhero bundle has been successfully imported.")
            messages.add_message(request, messages.SUCCESS, message)

        adminform = helpers.AdminForm(form, form.fieldsets, {})

        context = {"adminform": adminform}
        context.update(extra_context or {})
        context_instance = template.RequestContext(request)

        return render_to_response(
            "admin/superhero/import_form.html",
            context,
            context_instance=context_instance
        )

object_tools.tools.register(SuperheroImport, Superhero)
