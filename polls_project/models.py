from django.db import models

class Admin(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Survey(models.Model):
    name = models.CharField(max_length=30)

class Survey(models.Model):
    name = models.CharField(max_length=30)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.CharField(max_length=1000)

class Questions(models.Model):
    survey_id = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

class Answers(models.Model):
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=1000).null
    answer2 = models.CharField(max_length=1000).null
    answer3 = models.CharField(max_length=1000).null
    answer4 = models.CharField(max_length=1000).null
    answer5 = models.CharField(max_length=1000).null
    id_survey = models.IntegerField
    id_qustestion = models.IntegerField()

class Id(models.Model):
    id_user = models.IntegerField()

class Answers_Users(models.Model):
    answer = models.CharField(max_length=1000)
    name_survey = models.CharField(max_length=100)
    id_question = models.IntegerField()

