from django.shortcuts import render
from .forms import QuizForm
from .services import get_country_data_from_external_api


def quiz(request):
    """Generates quiz question and provides form to submit answer on GET.
    Checks form and provided answer on POST."""

    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            return render(request, 'country_quiz/check_answer.html', {'answer': form.data['answer'],
                                                                      'capital': request.session['capital'],
                                                                      'country': request.session['country']
                                                                      })
        else:
            form_error = True
    else:
        country_data = get_country_data_from_external_api()
        request.session['country'] = country_data['name']
        request.session['capital'] = country_data['capital']
        form_error = False

    return render(request, 'country_quiz/quiz_question.html', {'country': request.session['country'],
                                                               'form': QuizForm(),
                                                               'form_error': form_error})
