from django.contrib import admin
from django.urls import path
from .views import (
    create_post_view,
    detail_post_view,
    list_post_view,
    update_post_view,
    delete_post_view
)

app_name = 'posts'

urlpatterns = [
    path('create/', create_post_view, name='create'),
    path('detail/', detail_post_view, name='detail'),
    path('list/', list_post_view, name='list'),
    path('update/', update_post_view, name='update'),
    path('delete/', delete_post_view, name='delete'),
]
