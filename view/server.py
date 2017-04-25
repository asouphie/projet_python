from bottle import route, template, run, static_file


@route('/view/<filename>', name='view')
def server_view(filename) :
    return static_file(filename, root='view')

@route('/')
def index():
    return template('template')

run(host='localhost', port=8080)