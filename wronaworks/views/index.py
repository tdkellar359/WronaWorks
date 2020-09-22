import wronaworks
import flask

@wronaworks.app.route('/', methods=['GET'])
def show_index_page():
    context = { 'page': 'home' }
    return flask.render_template("index.html", **context)
# show_index_page


@wronaworks.app.route('/experiences', methods=['GET'])
def show_experiences_page():
    context = { 'page': 'experiences' }

    return flask.render_template("experiences.html", **context)

@wronaworks.app.route('/passions', methods=['GET'])
def show_passions_page():
    context = { 'page': 'passions' }

    return flask.render_template("passions.html", **context)

@wronaworks.app.route('/thoughts', methods=['GET'])
def show_thoughts_page():
    context = { 'page': 'thoughts' }

    return flask.render_template("thoughts.html", **context)

@wronaworks.app.route('/connect', methods=['GET'])
def show_connect_page():
    context = { 'page': 'connect' }

    return flask.render_template("connect.html", **context)
