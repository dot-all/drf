from django.urls import path
from .views import CustomLoginView, protected_view

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='custom_login'),
    path('protected/', protected_view, name='protected_view'),
]
