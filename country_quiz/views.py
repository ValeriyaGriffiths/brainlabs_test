from django.shortcuts import render
from .forms import QuizForm
from .services import get_country_data_from_external_api


def quiz(request):
    """Generates quiz question and provides form to submit answer."""

    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            return render(request, 'country_quiz/check_answer.html', {'answer': form.data['answer'],
                                                                      'capital': request.session['capital'],
                                                                      'country': request.session['country']
                                                                      })
        else:
            form = QuizForm()
            return render(request, 'country_quiz/quiz_question.html', {'country': request.session['country'],
                                                                       'form': form,
                                                                       'error': True})
    else:
        data = get_country_data_from_external_api() #TODO calls api every time and only takes first.
        country = data[0]['name']
        capital = data[0]['capital']

        request.session['country'] = country
        request.session['capital'] = capital
        form = QuizForm()

    return render(request, 'country_quiz/quiz_question.html', {'country': country,
                                                               'form': form,
                                                                       'error': False})
