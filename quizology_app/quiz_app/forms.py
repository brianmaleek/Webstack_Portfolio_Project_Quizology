from django.forms import ModelForm
from .models import *
from django import forms
from .models import *
import requests

class QuizCategoryForm(forms.Form):
    category_id = forms.ChoiceField(label='Quiz Category', choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Fetch quiz categories from the API and populate the choices
        response = requests.get('https://opentdb.com/api_category.php')
        data = response.json()
        categories = [(category['id'], category['name']) for category in data['trivia_categories']]
        self.fields['category_id'].choices = categories



class QuizAnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.questions = kwargs.pop('questions', [])
        
        super(QuizAnswerForm, self).__init__(*args, **kwargs)
        for i, question in enumerate(self.questions):
            self.fields[f'answer_{i}'] = forms.ChoiceField(
                widget=forms.RadioSelect,
                label=question['question'], 
                choices=[('correct', question['correct_answer'])] + [(f'incorrect_{i}', incorrect_answer) 
                                                                     for i, incorrect_answer in enumerate(question['incorrect_answers'])])
              
    def get_score(self):
        score = 0
        for i, question in enumerate(self.questions):
            correct_answer = question['correct_answer']
            user_answer = self.cleaned_data[f'answer_{i}']
            print(user_answer)
            if user_answer == 'correct':
                score += 1
        return score