from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Player(models.Model):
    '''
    This model is used to store the score of the player
    '''
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

class Quiz(models.Model):
    '''
    This model is used to store the quiz details
    '''
    quiz_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    total_questions = models.IntegerField()
    time = models.IntegerField(help_text="Duration of the quiz in minutes")
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ManyToManyField('Question', related_name='quizzes')
    def __str__(self):
        return self.title
    

class Question(models.Model):
    '''
    This model is used to store the questions of the quiz
    '''
    question_id = models.AutoField(primary_key=True)
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    def __str__(self):
        return self.question