import os
USE_SQLITE = True  # Set False to use MySQL (edit MYSQL_CONFIG below)

MYSQL_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "client_queries"
}

DB_PATH = os.path.join(os.path.dirname(__file__), "db.sqlite")
