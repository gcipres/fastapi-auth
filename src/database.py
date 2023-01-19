import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData

load_dotenv('config/.env')

DATABASE_URL: str = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine = create_engine(DATABASE_URL)

connection = engine.connect()

meta_data = MetaData()