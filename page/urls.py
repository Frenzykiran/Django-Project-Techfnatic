from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import company_name

urlpatterns = [
    path('', views.index, name='index'),
    #path('company_name', company_name, name='company_name'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



      