import os

from django.urls import include, path

from .views import Home, Profile
from .admin_views import UploadCSV

urlpatterns = [
    # Add a path with /api for Woocommerce and shopify plugin endpoints
    path('', Home.as_view(), name='home_view'),
    path('profile/<id>', Profile.as_view(), name='profile_view'),
    path('admin/upload/', UploadCSV.as_view(), name='admin_upload_view'),
]
