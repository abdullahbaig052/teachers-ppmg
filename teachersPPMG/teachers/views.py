from django.template.response import TemplateResponse
from django.views import View

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