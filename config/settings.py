import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")