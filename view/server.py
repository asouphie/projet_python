import json

from bottle import route, template, run, static_file, get, request

from view.functions import list_adress, list_activity, list_for_map


@route('/view/<filename>', name='view')
def server_view(filename) :
    return static_file(filename, root='view')

@route('/index')
def index():
    return template('template')

@get('/search')
def search():
    return template('template2')

@get('/list_town_zip')
def list_town_zip():
    town = None
    zip = None
    maxRows = None
    #On vérifie que la requête existe, si c'est le cas, alors la ville/le code postal prendra la valeur de la requete.
    if request.query.town:
        town = request.query.town
    if request.query.zip:
        zip = request.query.zip
    if request.query.max_rows:
        maxRows = request.query.max_rows

    list_town_zip = list_adress(town, zip, maxRows)

    return json.dumps(list_town_zip)

@get('/list_activities')
def list_activities():
    activity = None
    maxRows = None
    # On vérifie que la requête existe, si c'est le cas, alors l'activite prendra la valeur de la requete.
    if request.query.activity:
        activity = request.query.activity
    if request.query.max_rows:
        maxRows = request.query.max_rows

    activities = list_activity(activity, maxRows)
    return json.dumps(activities)

@get('/search_activity')
def search_activity():
    activity = None
    zip = None
    town = None

    if request.query.activity:
        activity = request.query.activity
    if request.query.zip:
        zip = request.query.zip
    if request.query.town:
        town = request.query.town

        listMap = list_for_map(activity, zip, town)

    return json.dumps(listMap)


run(host='localhost', port=8080)