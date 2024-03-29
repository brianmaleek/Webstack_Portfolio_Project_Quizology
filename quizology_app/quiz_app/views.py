# Create your views here.
from  django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from  .models import *
from django.contrib.auth.decorators import login_required, user_passes_test
import requests

from .forms import QuizCategoryForm, QuizAnswerForm


@login_required
def home(request):
    '''
        This view is used to display the home page
    '''
    return render(request, 'quiz_app/home.html')

def about(request):
    return render(request, 'quiz_app/about.html')



def quiz_catergory_list(request):
    '''
        This view is used to display the list of quiz categories
    '''
    if request.method == 'POST':
        form = QuizCategoryForm(request.POST)
      
        if form.is_valid():
            category_id = form.cleaned_data['category_id']  
            # Fetch quiz questions based on the selected category
            return redirect('display_quiz', category_id=category_id)
    else:
        form = QuizCategoryForm()
    return render(request, 'quiz_app/quiz_category_list.html', {'form': form})


def display_quiz(request, category_id):
    '''
        This view is used to display the quiz questions
    '''
       
    if request.method == 'POST':
        form = QuizAnswerForm(request.POST)
        print(form)
        if form.is_valid():
            score = 0
            for i, question in enumerate(form.questions):
                answer = form.cleaned_data[f'answer_{i}']
                print(answer)
                if answer == 'correct':
                    score += 1
            return render(request, 'quiz_app/score.html', {'score': score})
        
    # Fetch quiz questions from the API
    else:
        response = requests.get(f'https://opentdb.com/api.php?amount=5&category={category_id}&type=multiple')
        data = response.json()
        questions = []
        for question in data['results']:
            questions.append({
                'question': question['question'],
                'correct_answer': question['correct_answer'],
                'incorrect_answers': question['incorrect_answers']
            })
        questions.append(question)
        print(questions)
        
        form = QuizAnswerForm(questions=questions)
    return render(request, 'quiz_app/quiz_questions.html', {'form': form})