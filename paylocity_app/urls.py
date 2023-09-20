from paylocity_app import views
from django.urls import path

urlpatterns = [
    path('', views.security_features_list)
]
