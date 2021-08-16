import flask

app = flask.Flask(__name__)


# Make app aware of blueprints
def main():
    register_blueprints()
    app.run(debug=True)


def register_blueprints():
    # don't need this globally so import in scope
    from views import home_views
    from views import package_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)


if __name__ == '__main__':
    main()
