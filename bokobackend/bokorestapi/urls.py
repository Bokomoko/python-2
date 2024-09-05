from django.urls import path
from .views import PersonViewset

urlpatterns = [
    path('persons/', views.PersonList.as_view()),
    path('persons/<int:id>', views.PersonDetail.as_view()),
]
