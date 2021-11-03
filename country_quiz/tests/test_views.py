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

    def test_invalid_answer_gives_error_message(self):
        self.set_session_variables()
        response = self.client.post('/', data={'answer': '   '})
        content = str(response.content)
        self.assertTrue('Bad input. Try again.' in content)

    def test_correct_answer_is_accepted(self):
        self.set_session_variables()
        response = self.client.post('/', data={'answer': 'Minsk'})
        content = str(response.content)
        self.assertTrue('You answered Minsk, which is correct!' in content)

    def test_lower_case_answer_is_capitalised(self):
        self.set_session_variables()
        response1 = self.client.post('/', data={'answer': 'Minsk'})
        response2 = self.client.post('/', data={'answer': 'minsk'})
        content1 = response1.content
        content2 = response2.content

        self.assertTrue(content1 == content2)

    def test_correct_answer_is_given_when_user_incorrect(self):
        self.set_session_variables()
        response = self.client.post('/', data={'answer': 'Msk'})
        content = str(response.content)
        self.assertTrue('Correct answer was Minsk' in content)


