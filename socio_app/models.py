from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


categories = [('Web Design', 'Web Design'), ('Video Editing', 'Video Editing'), ('Photo Editing', 'Photo Editing'),
                 ('IT Service', 'IT Service'), ('UI/UX Design', 'UI/UX Design'),
                 ('Accountancy & Taxes', 'Accountancy & Taxes')]


class AddService(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=categories, default='Web Design')
    price = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Queries(models.Model):
    question = models.CharField(max_length=50,null=True)
    question_detail = models.TextField(max_length=200,default='No Details')
    category = models.CharField(max_length=50, choices=categories, default='Web Design')
    create_date = models.DateField(default=timezone.now)
    create_time = models.TimeField(default=timezone.now)
    approval = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.question

class Answers(models.Model):
    questions = models.ForeignKey(Queries,on_delete=models.CASCADE)
    detail = models.TextField(max_length=200,default='Write Your Answer Here')
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.detail

