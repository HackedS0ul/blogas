from django.urls import path

from .views import PostList, PostCreate, PostUpdate, user_register

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('create/', PostCreate.as_view(), name="create"),
    path('update/<pk>', PostUpdate.as_view(), name="update"),
    path('register/', user_register, name="register"),
]