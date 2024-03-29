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
            choices = [(f'incorrect_{i}', answer) for i, answer in enumerate(question['incorrect_answers'])] + [('correct', question['correct_answer'])]
            self.fields[f'answer_{i}'] = forms.ChoiceField(
                choices=choices,
                widget=forms.RadioSelect(),
                label=question['question']
            )