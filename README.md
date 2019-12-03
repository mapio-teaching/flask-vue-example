# Flask Vue Example

## The dispatcher

In order to serve **both** a Flask *backend* and a Vue *frontend* with the same `gunicorn` server it's enough to run the app in `backend/dispatcher.py`; such app is a WSGI *dispatcher* (based on Werkzeug [SharedDataMiddleware](https://werkzeug.palletsprojects.com/en/0.15.x/middleware/shared_data/) and [DispatcherMiddleware](https://werkzeug.palletsprojects.com/en/0.15.x/middleware/dispatcher/)) that routes requests to `/` (and to URLs with paths starting with `/{js,css,img}/` ) to the Vue app and the requests to URLs with paths starting with `/api/` to the Flask app. Thanks to such middleware, no modification is required to the standard Flask and Vue apps.

### Herokup

This example can be deployed on Heroku using the [command line client](https://devcenter.heroku.com/categories/command-line) as follows:

    heroku create <app_name>
    heroku buildpacks:add heroku/nodejs
    heroku buildpacks:add heroku/python
    git push heroku master

It is crucial that the `package.json` file sets

    "postinstall": "cd frontend && yarn install && yarn build"

to compile the Vue file during the Node buildpack execution and that in `Procfile` the creation of the database is run *before* the execution of `gunicorn` as

    web: cd backend && export FLASK_APP=api && flask init-db && gunicorn dispatcher:app --log-file -

### Endpoints

Once in execution, the endpoints of the app are:

* `/` leading to the Vue app (and `/about` leading to the routed about component);

* `/api/hello` as defined by the simple `/hello` route in the Flask app

* `/api/admin` as defined by the Flask-Admin usual integration endpoint.

Examples of such endpoint should be available on Heroku, for the **fontend** at

* https://mapio-flask-vue-example.herokuapp.com/

* https://mapio-flask-vue-example.herokuapp.com/about

and for the **backend** at

* https://mapio-flask-vue-example.herokuapp.com/api/hello

* https://mapio-flask-vue-example.herokuapp.com/api/admin/user/


## Developing the backend

The backend is just a Flask app with a trivial Flask-Admin integration that can be developed and tested as an usual Flak app.

To **setup** the backend run

    pip install -r requirements.txt
    cd backend
    rm -rf instance
    export FLASK_APP=api
    flask init-db

to **run** in *development* mode run

    export FLASK_ENV=development
    flask run

## Developing the frontend

The frontend is the basic Vue app as created by vue-cli with the router plugin that can be developed and tested as an usual Vue app.

To **setup** the frontend run

    yarn install

to **run** in *development* mode run

    yarn serve

### From scratch

How to recreate the frontend from scratch

    rm -rf frontend
    yarn add @vue/cli
    yarn run vue create frontend
    rm -rf node_modules package.json yarn.lock
    cd frontend
    yarn add @vue/cli
    yarn add @vue/cli-service-global
    yarn run vue add @vue/cli-plugin-router
