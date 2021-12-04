from django.urls import path

from .views import PostList, PostCreate

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('create/', PostCreate.as_view(), name="create"),
]