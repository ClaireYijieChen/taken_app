#Installation

1. Create a python 2.7 virtualenv by your preferred method. 
2. Install django 1.6 in the virtualenv ("pip install django")
3. Pull or clone this repo (git clone) into the virtualenv directory
4. Sync the database ("python manage.py syncdb")
5. Run the server ("python manage.py runserver")
6. Make your way to 127.0.0.1:8000 (normally) and start taking notes

##Style Guide
 - camelCase for backend functions such as models, database relations, searching, etc.
 - snake_case for frontend functions such as template engines and actual views
