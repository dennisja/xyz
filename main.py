import os
from typing import Optional

from core.app import create_app


environment = os.environ.get("ENVIRONMENT", "development")

app = create_app(environment)


if __name__ == "__main__":
    app.run(port=app.config.get("PORT"))
