from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('detect_blood_pressure/',views.detect_blood_pressure,name='detect_blood_pressure'),
    path('detect_thyroid/',views.detect_thyroid,name='detect_thyroid'),
    path('predict_diabetes/',views.predict_diabetes,name='predict_diabetes'),
    path('read_sensor_data/',views.read_sensor_data,name='read_sensor_data'),
    path('predict_diabetesRN/',views.predict_diabetesRN,name='predict_diabetesRN'),
    
    


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
