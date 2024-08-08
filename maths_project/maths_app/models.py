from django.db import models

class Questions(models.Model):
    questions = models.CharField(max_length=200,primary_key=True)  
    answer = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.questions 


class GetResult(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=200)

    def __str__(self):
        return f"Result for: {self.question}"