from typing import Optional

from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView

from core.config import CONFIGS
from core.db import db
from core.schema import schema


def create_app(environment: Optional[str] = "development") -> Flask:
    app = Flask(__name__)

    app_config = CONFIGS.get(environment)

    CORS(app)
    app_config.init_app(app)
    db.init_app(app)

    app.add_url_rule(
        "/notify",
        view_func=GraphQLView.as_view(
            "notify", schema=schema, graphiql=app_config.SHOW_GRAPHIQL
        ),
    )

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        """
        Rollback session if exceptions occurred and remove the session
        """
        if exception:
            db.session.rollback()
        db.session.remove()

    return app
