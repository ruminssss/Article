from django.urls import path

from .views import index, UserLogin, UserLogout, ArtCreateView, comments

urlpatterns = [
    path('', index, name='index'),
    path('login/', UserLogin.as_view()),
    path('logout/', UserLogout.as_view()),
    path('add/', ArtCreateView.as_view()),
    path('<int:pk>/', comments, name='comments'),
]