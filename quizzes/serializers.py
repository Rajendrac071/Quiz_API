from rest_framework import serializers
from .models import Quiz, Question, Answer, QuizTaker, UsersAnswer


class QuizSerializer(serializers.ModelSerializer):
    questions_count  = serializers.SerializerMethodField()

    def get_questions_count(self,object):
        return object.question_set.all().count()

    class Meta:
        model   = Quiz
        fields  = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Question
        fields  = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Answer
        fields  = '__all__'

class QuizTakerSerializer(serializers.ModelSerializer):
    class Meta:
        model   = QuizTaker
        fields  = '__all__'

class UsersAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model   = UsersAnswer
        fields  = '__all__'

