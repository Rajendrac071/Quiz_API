from django.shortcuts import render
from rest_framework import generics, mixins

from .models import Quiz, Question, Answer, QuizTaker, UsersAnswer
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer, QuizTakerSerializer, UsersAnswerSerializer


class Quiz_GenericAPIView(generics.GenericAPIView,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.RetrieveModelMixin):
    
    serializer_class    = QuizSerializer
    queryset            = Quiz.objects.all()
    lookup_field        = 'id'


    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id = None):
        return self.update(request, id)
    
    def delete(self, request, id):
        return self.destroy(request, id)

class Question_GenericAPIView(generics.GenericAPIView,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.RetrieveModelMixin):
    
    serializer_class    = QuestionSerializer
    queryset            = Question.objects.all()
    lookup_field        = 'id'


    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id = None):
        return self.update(request, id)
    
    def delete(self, request, id):
        return self.destroy(request, id)

class Answer_GenericAPIView(generics.GenericAPIView,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.RetrieveModelMixin):
    
    serializer_class    = AnswerSerializer
    queryset            = Answer.objects.all()
    lookup_field        = 'id'


    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id = None):
        return self.update(request, id)
    
    def delete(self, request, id):
        return self.destroy(request, id)

        
class QuizTaker_GenericAPIView(generics.GenericAPIView,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.RetrieveModelMixin):
    
    serializer_class    = QuizTakerSerializer
    queryset            = QuizTaker.objects.all()
    lookup_field        = 'id'


    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id = None):
        return self.update(request, id)
    
    def delete(self, request, id):
        return self.destroy(request, id)

class UsersAnswer_GenericAPIView(generics.GenericAPIView,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.RetrieveModelMixin):
    
    serializer_class    = UsersAnswerSerializer
    queryset            = UsersAnswer.objects.all()
    lookup_field        = 'id'


    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id = None):
        return self.update(request, id)
    
    def delete(self, request, id):
        return self.destroy(request, id)

