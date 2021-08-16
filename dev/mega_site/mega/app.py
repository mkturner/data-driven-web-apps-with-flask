import flask

import services.package_services as ps

app = flask.Flask(__name__)


@app.route('/')
def index():
    test_packages = ps.get_latest_packages()
    return flask.render_template('home/index.html', packages=test_packages)


@app.route('/about')
def about():
    return flask.render_template('home/about.html')


if __name__ == '__main__':
    app.run(debug=True)
