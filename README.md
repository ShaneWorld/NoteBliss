# Notes

#### Video Demo: https://youtu.be/N3_xGNiZtA4

#### Description:

This web app uses flask as the back-end framework, and mainly uses bootstrap to render html pages.

In the config.py file, the initial information of the program is centrally configured.

In the app folder, \_\_init\_\_.py is used to initialize the app, create and link the database, register the blueprint, and import the configuration information in config.py. The extension.py file defines the database db and the function login_required for subsequent file references.

In the app folder, it is mainly divided into 6 folders. Among them, templates and static are folders for storing template files and css styles respectively. The database tables are defined in the models folder. The main, edit, and auth folders are three blueprint modules, which are responsible for the home page, editing area, and account management respectively. The \_\_init\_\_.py file in each module creates the blueprint and imports the module's routing functions. forms.py is used to create forms to use flask_WTF. The routes.py file defines routes.

The main purpose of this web program is to write notes, but with the blessing of markdown syntax and flask blueprint, the scalability has been greatly improved. In the future, the functions can be continuously enriched, and the simple and beautiful appearance can all become the advantages of this app.
