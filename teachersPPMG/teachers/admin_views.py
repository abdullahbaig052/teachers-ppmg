import csv
import io

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views.generic import TemplateView

from .models import TeachersModel


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
        for i, column in enumerate(csv.reader(io_string, delimiter=',', quotechar="|")):
            if column[0]:
                teacher_inst = TeachersModel.objects.filter(email=column[3]).last()
                if teacher_inst:
                    messages.error(request, f'Skipped: Teacher with this email: {teacher_inst.email} already exists')
                    continue

                teacher_inst = TeachersModel()
                teacher_inst.first_name = column[0]
                teacher_inst.last_name = column[1]
                teacher_inst.profile_picture = column[2]
                teacher_inst.email = column[3]
                teacher_inst.phone_number = column[4]
                teacher_inst.room_number = column[5]
                teacher_inst.subjects_taught = ",".join(column[6:]).replace("\"", '')
                teacher_inst.save()
            else:
                messages.error(request, f'RowID: {i} - {column}: not in correct format!')

        return redirect('home_view')

