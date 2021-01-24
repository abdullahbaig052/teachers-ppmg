from django.urls import path

from .admin_views import UploadCSV

urlpatterns = [
    path('upload-teacher-details/', UploadCSV.as_view(), name="admin_upload_teachers"),
]
