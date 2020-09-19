import wronaworks
import flask

@wronaworks.app.route('/', methods=['GET'])
def show_index_page():
    context = {}
    return flask.render_template("index.html", **context)
# show_index_page
