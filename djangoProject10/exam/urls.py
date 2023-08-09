from django.urls import path
from .views import test, Just, incorrect

urlpatterns = [
    path('test/', test, name='test'),
    path('Just/', Just, name='Just'),
    path('incorrect/', incorrect, name='incorrect')
]

