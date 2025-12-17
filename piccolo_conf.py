from piccolo.engine.postgres import PostgresEngine
from piccolo.conf.apps import AppRegistry

DB = PostgresEngine(
    config={
        "database": "blacksheepDB",
        "user": "nahim",
        "password": "nahim",
        "host": "localhost",
        "port": 5435,
    }
)
APP_REGISTRY = AppRegistry(apps=["app.piccolo_app"])
