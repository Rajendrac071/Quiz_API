from django.db import models
from django.conf import settings

class Quiz(models.Model):
    no_of_questions  = models.IntegerField()
    quiz_name        = models.CharField(max_length = 100)

    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    quiz            = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text   = models.CharField(max_length = 500)          #Label
    image           = models.ImageField(null = True, blank = True)
    question_type   = models.CharField(max_length = 100)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question    = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length = 500)          #Label
    is_correct  = models.BooleanField(default = False)

    def __str__(self):
        return self.answer_text

class QuizTaker(models.Model):
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz    = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score   = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
class UsersAnswer(models.Model):
    quiz_taker      = models.ForeignKey(QuizTaker, on_delete=models.CASCADE)
    question        = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer          = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.question.question_text
