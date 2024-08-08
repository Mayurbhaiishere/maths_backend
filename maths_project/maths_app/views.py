from django.shortcuts import render, redirect
from .models import Questions,GetResult
from .forms import QuestionForms,ResultForms

def question_list(request):
    questions = list(Questions.objects.values())
    # if request.method == 'POST':
    #     questions = QuestionForms(request.POST)
    #     if answer.is_valid():
    #         answer.save()
    #     return redirect('question_list')
    # else:
    #     answer = QuestionForms()
    #     return render(request, self.template_name, {'questions': questions})
    return render(request,'maths_app/question_list.html',{'questions': questions})


def put_results(request):
    answer = list(GetResult.objects.values().order_by('-created_at'))
    return render(request, 'maths_app/question_list.html', {'answer': answer})

def question_create(request):
    if request.method == 'POST':
        form = QuestionForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_create') 
    else:
        form = QuestionForms()
    return render(request, 'maths_app/question_create.html', {'form': form})

