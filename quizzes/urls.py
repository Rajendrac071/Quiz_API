from django.urls import path
from .views import Quiz_GenericAPIView, Question_GenericAPIView, Answer_GenericAPIView, QuizTaker_GenericAPIView, UsersAnswer_GenericAPIView


urlpatterns = [
    path('quiz/', Quiz_GenericAPIView.as_view()),
    path('quiz/detail/<int:id>/', Quiz_GenericAPIView.as_view()),

    path('question/', Question_GenericAPIView.as_view()),
    path('question/detail/<int:id>/', Question_GenericAPIView.as_view()),
    
    path('answer/', Answer_GenericAPIView.as_view()),
    path('answer/detail/<int:id>/', Answer_GenericAPIView.as_view()),

    path('quiztaker/', QuizTaker_GenericAPIView.as_view()),
    path('quiztaker/detail/<int:id>/', QuizTaker_GenericAPIView.as_view()),

    path('usersanswer/', UsersAnswer_GenericAPIView.as_view()),
    path('usersanswer/detail/<int:id>/', UsersAnswer_GenericAPIView.as_view()),

]