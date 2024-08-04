from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import QuestionForm

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'maths_app/question_list.html')

def get_results(request):
    pass

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_list') 
    else:
        form = QuestionForm()
    return render(request, 'maths_app/question_create.html', {'form': form})



@csrf_exempt
def verify_answer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        answer = data.get('answer')

        # Perform the answer verification logic here
        correct_answer = Question.objects.filter(answer=answer).exists()

        if correct_answer:
            # Save the result to the database if needed
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    return JsonResponse({'error': 'Invalid request'}, status=400)
