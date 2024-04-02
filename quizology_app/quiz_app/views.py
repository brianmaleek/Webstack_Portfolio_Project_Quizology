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

    response = requests.get(f'https://opentdb.com/api.php?amount=10&category={category_id}&type=multiple')
    data = response.json()
    questions = data['results']
    
    # form = QuizAnswerForm(questions=questions)
    context = {
        'questions': questions
    }
    return render(request, 'quiz_app/quiz_questions.html', context)



def getUserScore(request):
    '''
        This view is used to display the user's score
    '''
    if request.method == 'POST':

        print(request.POST)
        score = 0
       
        category = "General Knowledge"
        for key, value in request.POST.items():
            if key.startswith('question_'):
               question_id = key.split('_')[1]
               if request.POST.get(f'question_{question_id}') == request.POST.get(f'question_{question_id}_correct_answer'):
                  score += 1
        length = len(request.POST) - 1
        # store the user's score for the api generated quiz
        user = User.objects.get(username=request.user)
        user_score = UserQuizResult(user=user, quiz_category=category, score=score)
        user_score.save()
        half_length = length / 2

        return render(request, 'quiz_app/score.html', {'score': score, 'length': length, 'half_length': half_length})
    

def leaderboard(request):
    '''
        This view is used to display the highest score
    '''
    scores = UserQuizResult.objects.all().order_by('-score')[:10]
    context = {
        'scores': scores
    }
    
    

    return render(request, 'quiz_app/leader_board.html', context)