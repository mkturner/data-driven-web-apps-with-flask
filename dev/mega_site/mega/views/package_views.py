import flask

import services.package_services as ps

# Instantiate blueprint
blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/package/<package_name>')
def package_details(package_name: str):
    # return "Package details for: {}".format(package_name)
    return flask.render_template('packages/details.html', name=package_name)
