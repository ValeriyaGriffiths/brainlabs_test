from django.shortcuts import render
from .services import get_country_data_from_external_api


def quiz(request):
    """Generates quiz question and provides form to submit answer."""

    data = get_country_data_from_external_api()

    return render(request, 'country_quiz/quiz_question.html')
