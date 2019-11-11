import os
from django.urls import path
from .views import Login, Logout, AccountCreate, AccountActive, AccountConfirm
from registrations.forms import UserActivationForm

app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [

    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registration/', AccountCreate.as_view(), name='registration'),
    # path('confirm/<uidb64>/<token>/', AccountConfirm.as_view(), name='AccountConfirm'),
    path('confirm/', AccountConfirm.as_view(), name='AccountConfirm'),
    path('active/', AccountActive.as_view(form_class=UserActivationForm), name='active'),
]
