from django.contrib import admin
from django.urls import path, include  # <- include is needed to add app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),   # <- include tasks app URLs
]
