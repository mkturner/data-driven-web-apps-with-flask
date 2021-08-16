import flask

import services.package_services as ps

# Instantiate blueprint
blueprint = flask.Blueprint('home', __name__, template_folder='tem')


@blueprint.route('/')
def index():
    test_packages = ps.get_latest_packages()
    return flask.render_template('home/index.html', packages=test_packages)


@blueprint.route('/about')
def about():
    return flask.render_template('home/about.html')