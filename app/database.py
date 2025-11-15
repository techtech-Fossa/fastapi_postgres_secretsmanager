from sqlalchemy import create_engine, inspect
import os

from aws_client import get_secrets

user_id = os.getenv("USER_ID")

user_secrets = get_secrets(user_id)

print(user_secrets)

user = user_secrets["user"]
password = user_secrets["password"]
postgres_db = os.getenv("POSTGRES_DB")
postgres_db_endpoint = os.getenv("POSTGRES_DB_ENDPOINT")

url = f"postgresql+psycopg://{user}:{password}@{postgres_db_endpoint}/{postgres_db}"

engine = create_engine(url)

inspector = inspect(engine)
print(inspector.get_schema_names())
