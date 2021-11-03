from django import forms


class QuizForm(forms.Form):
    """Form takes answer to quiz question."""
    answer = forms.CharField(label='Answer', max_length=200)
