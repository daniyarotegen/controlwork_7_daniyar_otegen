from django.urls import path
from guestbook.views import index_view, add_view, update_view, delete_view


urlpatterns = [
    path('', index_view, name='index'),
    path('record/add/', add_view, name='record_add'),
    path('record/<int:pk>/edit/', update_view, name='record_update'),
    path('record/<int:pk>/delete/', delete_view, name='record_delete'),
]