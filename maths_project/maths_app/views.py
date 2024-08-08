from django.shortcuts import render
from django.core.serializers import serialize
from .models import Questions  

def question_list(request):
    questions = Questions.objects.all()
    context = {
        'questions': questions,
        'questions_json': serialize('json', questions, fields=('question', 'answer')),
    }
    return render(request, 'maths_app/question_list.html', context)

# def put_results(request):
#     results = GetResult.objects.all().order_by('-created_at')  
#     return render(request, 'maths_app/results_list.html', {'results': results})

# def question_create(request):
#     if request.method == 'POST':
#         form = QuestionForms(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('question_list')  
#     else:
#         form = QuestionForms()
#     return render(request, 'maths_app/question_create.html', {'form': form})
