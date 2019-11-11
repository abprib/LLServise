import os
from django.urls import path
from .views import IntervalUpdate, StatusUpdate, RepeatUpdate

app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [

    path('update_interval/<int:pk>/', IntervalUpdate.as_view(), name='update_interval'),
    path('update_status/<int:pk>/', StatusUpdate.as_view(), name='update_status'),
    path('update_repeat/<int:pk>/', RepeatUpdate.as_view(), name='update_repeat'),

]