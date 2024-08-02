from django.shortcuts import render, get_object_or_404
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'qa/question_list.html', {'questions': questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all()
    return render(request, 'qa/question_detail.html', {'question': question, 'answers': answers})

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'qa/question_form.html', {'form': form})

def answer_create(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('question_detail', pk=pk)
    else:
        form = AnswerForm()
    return render(request, 'qa/answer_form.html', {'form': form})
