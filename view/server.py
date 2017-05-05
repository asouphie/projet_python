import json

from bottle import route, template, run, static_file, app, request, response, post

from view.functions import list_activite, list_ville, list_cp


@route('/view/<filename>', name='view')
def server_view(filename) :
    return static_file(filename, root='view')

@route('/')
def index():
    return template('template', list_activite = list_activite(), list_villes_cp = list_ville()+","+list_cp())

run(host='localhost', port=8080)