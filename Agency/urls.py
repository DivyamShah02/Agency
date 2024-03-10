from django.contrib import admin
from django.urls import path,include
from .views import home
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
