from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view, template_bootstrap


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/',cars_view, name='cars_list'),
    path('template/', template_bootstrap)

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
