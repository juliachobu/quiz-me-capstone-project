from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from .models import Question, Choice, Result


class GetQuestions(ListView):
    model = Question
    context_object_name = 'questions'
    # template_name = 'questions.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = context['questions'].all()
        return context



class QuestionDetail(DetailView):
    model = Choice
    context_object_name = 'choices'
    template_name = 'quiz_me_app/details.html'

    # def result(request):
    #     result = request.GET['correct_answer']
    #     return render(request, 'details.html', {'correct_answer':result})



class ResultDetail(ListView):
    model = Result
    context_object_name = 'results'
    template_name = 'quiz_me_app/results.html'



    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['results'] = context['results'].all()
    #     context['count'] = context['results'].filter(correct_answer = True).count()    
    #     return context    


def get_results(request):
    choices = Choice.objects.all()
    questions = Question.objects.all()
    
    if request.method == 'POST':
        incorrect=[]
        correct=[]
        for question in questions:
            choice_id = request.POST[question.text]
            choice = Choice.objects.get(id = choice_id)
            if choice.is_correct:
                correct.append({'question': question.text, 'choice' : choice.text})

            else:
                correct_choice = question.choices.filter(is_correct = True)[0]
                incorrect.append({'question':question.text, 'choice':correct_choice.text})
                
    

        return render(request, 'quiz_me_app/results.html', {'correct' : correct, 'incorrect' : incorrect})

    return render(request, 'quiz_me_app/results.html')


