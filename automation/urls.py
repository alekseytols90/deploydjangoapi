from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #url(r'^$', views.analysis, name='analysis'),
    url(r'^add_patient', views.add_patient, name='add_patient'),

]
