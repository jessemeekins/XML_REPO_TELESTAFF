# flask-api

This [template repository](https://github.com/jessemeekins/XML_REPO_TELESTAFF.git)
 provides a minimal configuration for a 'production-ready' Flask API 
project. It includes a basic project structure and 'seed' files for functional and 
non-function testing, a basic application structure (including error-handling 
blueprint), and a few assorted 'getting started' files too.

The template has been set up for use with Python >= 3.10.8 and [Docker](https://www.docker.com/). 

## Running locally

To run the basic server, you'll need to install a few requirements. To do this, run:

```bash
pip install -r requirements/common.txt
```

This will install only the dependencies required to run the server. To boot up the 
default server, you can run:

```bash
bash bin/run.sh
```

This will start a [Gunicorn](https://gunicorn.org/) server that wraps the Flask app 
defined in `src/app.py`. Note that [this is one of the recommended ways of deploying a
Flask app 'in production'](https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/). 
The server shipped with Flask is [intended for development
purposes only](https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment).  

You should now be able to send:

```bash
curl localhost:5000/health
```

And receive the response `OK` and status code `200`. 

## Running with `docker`

Unsurprisingly, you'll need [Docker](https://www.docker.com/products/docker-desktop) 
installed to run this project with Docker. To build a containerised version of the API, 
run:

```bash
docker build . -t flask-app
```

To launch the containerised app, run:

```bash
docker run -p 5000:5000 flask-app
```

You should see your server boot up, and should be accessible as before.

## Developing with the template

```bash
pip install -r requirements/develop.txt
```

This'll install some style formatting and testing tools (including `pytest` and 
`locust`).
