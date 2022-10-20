# content-curation-web-application
SolarSPELL Content Curation service (CC). The Content Curation service provides functionality for library curators to submit new content and its associated metadata for approval in multiple languages. A Content Curation Admin has all the abilities of a library curator, and can also approve, modify, or reject outright content submitted for approval. A Content Curation Admin can also add new language categories, create/remove users, and modify their roles to create other admins or content curators.

# Installation Instructions
Install the latest versions of Git, npm, Python, and Postgresql. If you would like to set up your local environment using Docker, navigate to the docker section.

Using git, clone the project into a new directory git clone https://github.com/SolarSPELL-Main/content-curation.git.

In the frontend directory, run npm install. This installs all the packages npm needs to build the frontend. Then, build the frontend using npm run-script build.

Back in the main directory, run pip3 install -r requirements.txt. Depending on your system, you may need to use pip instead of pip3. This installs all the python dependencies.

As well as with pip, python3 may be replaced with python depending on your system. When using bash or similar terminal you may be able to use ./manage.py instead of python3 manage.py to save time.

Create a PostgreSQL database. If you are using linux, you should do this on another user account created specifically for postgres. You will need to find a postgres tutorial for this on google as it varies differently depending on your OS

Copy the file content_curation/env.example and rename it to content_curation/.env. If your system file browser doesn't let you do this try with VSCode or other IDE file browser.

Edit the newly created content_curation/.env file, setting SECRET_KEY to a new random string, DATABASE_URL to the connection string of the database you created in step 4. If in a production environment, change DEBUG to False

Run python3 manage.py migrate. This updates the django database to initialize it with the right schema.

Open a django shell using python3 manage.py shell. Enter the following commands. If you aren't running this on localhost, replace 127.0.0.1 with your domain name (ex. example.com)

>>> from django.contrib.sites.models import Site
>>> site = Site.objects.create(domain='127.0.0.1', name='127.0.0.1')
>>> site.save()
(credit https://stackoverflow.com/questions/16068518/django-site-matching-query-does-not-exist)

Enter exit() to exit the django shell.

Create a superuser by using python3 manage.py createsuperuser Enter a username, email, and password. This will be your login and password to the admin panel

Run the server by using python3 manage.py runsslserver 127.0.0.1:8000. This is only suitable for a developer server and should be setup differently on production according to your server.

Login to the admin console under https://127.0.0.1:8000/admin/. Make sure that you are using https. Click accept the risk on your browser. Under Social Applications, click add social application on the top right. Select Google for Provider, enter google for name, the client id and secret key can be generated with the Google Cloud Console. If you haven't done this before you will likely need an external tutorial for this. If you are working with others it is possible that others will already have one. You can have multiple people with the same client id and secret. One thing of note is that the Key field on the entry form can be left blank. For Sites make sure that the 127.0.0.1 site or other created during step 8 is selected.

You can now view the content curation site at https://127.0.0.1:8000/static/index.html/

Hot Reloading:

cd frontend && npm run watch
Open up another terminal and run cd .. && python manage.py runserver 0.0.0.0:8000
