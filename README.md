fullthroattle_labs,
Django-Assignment Test
-----------------------------------------------------------------------------------------------
Admin Superuser Information
User Name : sajid , 
User Password: 9959301556
-----------------------------------------------------------------------------------------------

heroku host of this poject: https://fullthrottlelabsproject.herokuapp.com/
-----------------------------------------------------------------------------------------------

Downloading project:
Clone as zip file and open it your computer or if you have git application
https://github.com/sajid969/fullthroattle_labs.git
------------------------------------------------------------------------------------------------

Before running this project you need intall below list apps and packages

Install Python 3.7 or above -> https://www.python.org/
Install Pip -> python get-pip.py

pip install Django
pip install djangorestframework
pip install django-timezone-field
pip install faker

or

pip install -r requirements.txt

-------------------------------------------------------------------------------------------------
For running:

python manage.py runserver
-------------------------------------------------------------------------------------------------
to custom management command to populate the database with some dummy data:

heroku run python populate.py --app fullthrottlelabsproject
