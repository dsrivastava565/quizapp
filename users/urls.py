from django.urls import include, path
from knox import views as knox_views

from . import views
from users.views import *

urlpatterns = [
    path('show', views.UserListView.as_view()),
    path('add_question',views.QuestionAPIView.as_view()),
    path('register', views.RegisterAPI.as_view()),
    path('login', LoginAPI.as_view(), name='login'),
    path('logout', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('userdata', views.UserAPI.as_view(),name='userdata'),
    path('getquestions', views.GETQuestions.as_view()),
    path('createquiz', views.CreateQuiz.as_view()),
    path('createquizquestions', views.CreateQuizQuestions.as_view()),
    path('getquizs', views.GETQuizs.as_view()),
    path('getquizquestions',views.GETQuizQuestions.as_view()),
    path('submitquiz',views.SubmitQuiz.as_view())
]