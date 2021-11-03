Simple quiz app; consists of two templates - one generates a question and provides a form for the answer, the other checks the posted answer.
Generated questions asks for the capital of a random country. This data is fetched from https://countriesnow.space/api/v0.1/countries/capital.
Answer template checks the posted answer and provides correct answer if posted answer is incorrect.

This app is very simple and does not require a full-fledged backend (db.sqlite3 is used to save session data in this case). If we were to add more functionality, like allowing several users to do the quiz and keep track of their scores, it would make sense to add this with User and Answer models, for example. 

To run this locally, do pip install with requirements.txt file and run manage.py migrate to recreate a local db.sqlite3 file.
settings.py is provided here, but would not be normally committed and DEBUG flag would need to be changed to False in production.
