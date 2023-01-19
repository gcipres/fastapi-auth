from ..database import meta_data
from sqlalchemy import Table, Column, ForeignKeyConstraint
from sqlalchemy.dialects.mysql import CHAR, VARCHAR, BIGINT, TEXT

UserDB = Table(
    "users", 
    meta_data,
    Column("id", CHAR(38), primary_key=True, nullable=False),
    Column("email", VARCHAR(50), unique=True, nullable=False),
    Column("password", VARCHAR(200)),
    Column("name", VARCHAR(150)),
    Column("create_at", BIGINT)
)