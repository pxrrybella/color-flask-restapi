
# Colors REST API



Hello! I hope you are having a great day, might today be filled with opportunities for growth and learning <3

This project is a fairly simple REST API built with Flask.
It has the basic CRUD routes which you can test using Postman ( you can test some of these routes using only your browser, but for the "add_color" and "update_color routes you'll need a GUI like Postman so you can input form values. )

You can:
- See all colors ( ``/colors`` )
- Add colors ( ``/add_color`` )
- Update colors ( ``/update_color`` )
- Delete colors ( ``/drop_color/<color_id>`` )

All of this was possible thanks to the LinkedIn Learning course "Building RESTful APIs with Flask" by Bruce Van Horn.


## How to run it locally:
You'll need:
- Python ( free at python.org )
- pip installed ( pip is a package manager, it usually comes with Python, but just check if you have it by running the command ``pip --version`` on your system's command line interpreter application (cmd, for example) )
- IDE ( i used PyCharm by JetBrains, free at jetbrains.com )

Having those, once you clone the folder with GIT, you need to set up you virtual enviroment so the dependencies get installed there.

For that, open a terminal within the cloned folder and type ``pipenv shell``.

Then, for the dependencies to install, use the command ``pipenv install``. To check if every package had installed correctly, you can use the command ``pip list`` to get all the packages.
It should match the piplist.txt file within the project.

That done, your pipenv virtual enviroment is ready.

Within the virtual enviroment, type the command ``flask db_create``, this will create the SQLite database.

Then, type the command ``flask db_seed`` so we can add some data to the database.

Having that ready, now you can run de app.py file either using a IDE or the terminal.

With the app.py running, the API is ready for HTTP requests.

Hope this is useful, if you have questions feel free to ask.


## Packages installed:

- Flask
- SQL-Alchemy
- flask-marshmallow
- Flask-SQLAlchemy
- marshmallow
- marshmallow-sqlalchemy
- SQLAlchemy