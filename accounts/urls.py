from . import views
from django.urls import path


urlpatterns = [
    path("registrations/", views.UserRegisterAPIView.as_view()),
]