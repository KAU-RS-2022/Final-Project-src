from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('test/', views.test, name='test'),
    path('get-recommend', views.recommend, name='recommend')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)