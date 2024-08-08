from django import forms
from .models import Questions

class QuestionForms(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['questions', 'answer']  

# class ResultForms(forms.ModelForm):
#     class Meta:
#         model = GetResult
#         fields = ['questions', 'user_answer']