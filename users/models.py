from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    address = models.CharField(blank=True,max_length=255)
    usertype = models.CharField(max_length=600,blank=True)
    
    def __str__(self):
        return self.email

class Questions(models.Model):
    AddedBy = models.ForeignKey(CustomUser, blank = True,null = True,on_delete=models.CASCADE)
    question =models.TextField(max_length=600)
    option1 = models.CharField(max_length=600)
    option2 = models.CharField(max_length=600)
    option3 = models.CharField(max_length=600)
    option4 = models.CharField(max_length=600)
    answer = models.CharField(max_length=600,blank=False)
    def __str__(self):
        return self.question

class Quiz(models.Model):
    AddedBy = models.ForeignKey(CustomUser, blank = True,null = True,on_delete=models.CASCADE)
    Name =models.TextField(max_length=600)
    TimeDuration = models.IntegerField(default=0)
    max_marks = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    def __str__(self):
        return self.Name

class QuizQuestions(models.Model):
    quiz = models.ForeignKey(Quiz, blank = True,null = True,on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, blank = True,null = True,on_delete=models.CASCADE)

    def __str__(self):
        return self.quiz


class QuizSubmission(models.Model):
    quiz = models.ForeignKey(Quiz, blank = True,null = True,on_delete=models.CASCADE)
    SubmittedBy = models.ForeignKey(CustomUser, blank = True,null = True,on_delete=models.CASCADE)
    total_correct =  models.IntegerField(default=0)
    total_marks_obtained = models.IntegerField(default=0)
    def __str__(self):
        return self.quiz
		