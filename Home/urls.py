from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('sending',views.updatedata),
    #path('',views.Teams_asJson,name='my_ajax_url'),
]