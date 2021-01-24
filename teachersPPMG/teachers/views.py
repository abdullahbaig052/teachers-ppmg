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


class Profile(View):
    template_name = 'profile.html'

    def get(self, request, id):
        context = {}
        teacher = TeachersModel.objects.get(id=id)
        context['teacher'] = teacher
        return TemplateResponse(request, self.template_name, context)