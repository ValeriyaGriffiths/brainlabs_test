from django.test import TestCase


class QuizViewTest(TestCase):
    def set_session_variables(self):
        session = self.client.session
        session['country'] = 'Belarus'
        session['capital'] = 'Minsk'
        session.save()

    def test_home_url_uses_quiz_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'country_quiz/quiz_question.html')

    def test_invalid_answer_uses_quiz_template(self):
        self.set_session_variables()
        response = self.client.post('/', data={'answer': '   '})
        self.assertTemplateUsed(response, 'country_quiz/quiz_question.html')

    def test_valid_answer_uses_answer_template(self):
        self.set_session_variables()
        response = self.client.post('/', data={'answer': 'Minsk'})
        self.assertTemplateUsed(response, 'country_quiz/check_answer.html')

