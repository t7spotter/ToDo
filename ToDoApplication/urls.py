from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoView.as_view()),
    path('<int:pk>', views.TodoDetailView.as_view()),
]
