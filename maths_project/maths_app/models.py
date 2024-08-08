from django.db import models

class Questions(models.Model):
    questions = models.CharField(max_length=255,primary_key=True)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.questions

# class GetResult(models.Model):
#     questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
#     user_answer = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.questions} - {self.user_answer}"