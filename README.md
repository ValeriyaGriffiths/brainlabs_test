Requirements:

1. Have a quiz page with an input box/button to submit an answer.
2. Question should ask 'Name the capital for country XXX'.
3. Pick a country at random from provided API url and pass this to the question.
4. Pressing submit button checks if answer is correct (and gives confirmation).
5. If answer is incorrect provide correct answer.
6. (Inferred requirement - have a button to generate a new question). 

Solution:

Simple quiz app; consists of two templates - one generates a question and provides a form for the answer, the other checks the posted answer. Generated questions asks for the capital of a random country. This data is fetched from https://countriesnow.space/api/v0.1/countries/capital. Answer template checks the posted answer and provides correct answer if posted answer is incorrect.

This app is very simple and does not require a full-fledged backend (db.sqlite3 is used to save session data in this case). If we were to add more functionality, like allowing several users to do the quiz and keep track of their scores, it would make sense to add this with User and Answer models, for example.

To run this locally, do pip install with requirements.txt file and run manage.py migrate to recreate a local db.sqlite3 file. settings.py is provided here, but would not be normally committed and DEBUG flag would need to be changed to False in production.
