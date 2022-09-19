from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import AddService, Queries, Answers



class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __str__(self):
        poster = self.username

class NewServiceForm(forms.ModelForm):
    class Meta:
        model = AddService
        fields = ('name','category','price')


class QueriesForm(forms.ModelForm):
    class Meta:
        model = Queries
        fields = ('question','question_detail','category')


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ('detail',)


