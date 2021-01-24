import datetime
import logging
import mimetypes
import os
from wsgiref.util import FileWrapper

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import FileResponse, StreamingHttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView

from .models import TeachersModel
import csv, io


class UploadCSV(LoginRequiredMixin, TemplateView):
    template = "upload_categories.html"

    def get(self, request, *args, **kwargs):
        context = {}
        teachers = TeachersModel.objects.all()
        context['teachers'] = teachers
        return TemplateResponse(request, self.template, context=context)

    def post(self, request):
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')

        data_set = csv_file.read().decode('UTF-8')

        # setup a stream which is when we loop through each line we are able to handle a data in a stream
        io_string = io.StringIO(data_set)
        next(io_string)
        next(io_string)
        # for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        #     if not column[2]:
