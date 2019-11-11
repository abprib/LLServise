import os
from django.urls import path
from .views import WordCreate, WordUpdate, WordDetail, WordDelete, WordList, WordView
from .forms import WordCreateForm

app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path('list/<int:pk>/', WordList.as_view(), name='WordList'),
    path('create/', WordCreate.as_view(form_class=WordCreateForm), name='WordCreate'),
    path('<int:pk>/update/', WordUpdate.as_view(), name='WordUpdate'),
    path('<int:pk>/delete/', WordDelete.as_view(), name='WordDelete'),
    path('<int:pk>/detail/', WordDetail.as_view(), name='WordDetail'),
    path('', WordView.as_view(), name='WordView'),
]