import json

from bottle import route, template, run, static_file, get, request

from view.functions import list_adress, list_activity


@route('/view/<filename>', name='view')
def server_view(filename) :
    return static_file(filename, root='view')

@route('/index')
def index():
    return template('template')

@get('/list_town_zip')
def list_town_zip():
    town = None
    zip = None
    max_rows = None
    #On vérifie que la requête existe, si c'est le cas, alors la ville/le code postal prendra la valeur de la requete.
    if(request.query.town) :
        town = request.query.town
    if(request.query.zip):
        zip = request.query.zip
    if(request.query.max_rows) :
        max_rows = request.query.max_rows

    list_town_zip = list_adress(town, zip, max_rows)

    return json.dumps(list_town_zip)

@get('/list_activities')
def list_activities():
    activity = None
    max_rows = None
    # On vérifie que la requête existe, si c'est le cas, alors l'activite prendra la valeur de la requete.
    if(request.query.activity) :
        activity = request.query.activity
    if (request.query.max_rows):
        max_rows = request.query.max_rows

    activities = list_activity(activity, max_rows)
    return json.dumps(activities)

run(host='localhost', port=8080)