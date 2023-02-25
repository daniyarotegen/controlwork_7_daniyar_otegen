from django.urls import path
from guestbook.views import index_view, add_view

urlpatterns = [
    path('', index_view, name='index'),
    path('add/', add_view, name='record_add'),

]