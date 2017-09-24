# This is a README.
## Hi!

This is a cookiecutter.
It has:
* IPython (and django_extensions to use `python manage.py shell plus`)
* Tests moved to a separate directory
* Config has DRF, django_extensions and existing apps added
* AppConfig moved to init in both apps (no need to clutter the directories)
* Accounts app using the django.contrib.auth model
* Empty Template app with models, serializers and views that only contain
  imports
* This **README!**

Please remember to:
* pip freeze > requirements.txt if you're going to collaborate
* use scripts for things that you're going to do repetitively

"Features" to add (`#TODO`, mainly because I want to do something with this
in the future and having a TODO helps me do that):
* url confs moved to each app
