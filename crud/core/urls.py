from django.urls import path

from .views import PostList, PostCreate, PostUpdate, user_register, user_login, log_out, PostDelete

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('create/', PostCreate.as_view(), name="create"),
    path('update/<pk>', PostUpdate.as_view(), name="update"),
    path('delete/<pk>', PostDelete.as_view(), name="delete"),
    path('register/', user_register, name="register"),
    path('login/', user_login, name='login'),
    path('logout/', log_out, name='logout'),
]