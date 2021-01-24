import datetime
import logging
import mimetypes
import os
import csv, io

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


class Home(View):
    template_name = 'home.html'

    def get(self, request):
        context = {}
        teachers = TeachersModel.objects.all()
        context['teachers'] = teachers
        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')

        data_set = csv_file.read().decode('UTF-8')

        # setup a stream which is when we loop through each line we are able to handle a data in a stream
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            teacher_inst = TeachersModel.objects.filter(email=column[3]).last()
            # if teacher_inst:
                # messages.error(request, f'Skipped: Teacher with this email: {teacher_inst.email} already exists')
                # continue

            # teacher_inst = TeachersModel()
            teacher_inst.first_name = column[0]
            teacher_inst.last_name = column[1]
            teacher_inst.profile_picture = column[2]
            teacher_inst.email = column[3]
            teacher_inst.phone_number = column[4]
            teacher_inst.room_number = column[5]
            teacher_inst.subjects_taught = ", ".join(column[6:])
            teacher_inst.save()
        return redirect('home_view')


class Profile(View):
    template_name = 'profile.html'

    def get(self, request, id):
        context = {}
        teacher = TeachersModel.objects.get(id=id)
        context['teacher'] = teacher
        return TemplateResponse(request, self.template_name, context)