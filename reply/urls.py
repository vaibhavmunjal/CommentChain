from django.urls import path, include
from .views import home, delete_comment


urlpatterns = [
	path('', home, name='home'),
	path('delete', delete_comment, name='delete'),
]
