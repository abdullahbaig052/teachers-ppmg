from django.urls import path

from .admin_views import UploadCSV
from .views import Home, Profile

urlpatterns = [
    # Add a path with /api for Woocommerce and shopify plugin endpoints
    path('', Home.as_view(), name='home_view'),
    path('profile/<id>', Profile.as_view(), name='profile_view'),
    path('admin/upload/', UploadCSV.as_view(), name='admin_upload_view'),
]
