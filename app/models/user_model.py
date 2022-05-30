from sqlalchemy import Column,String,Integer
from app.db.postgres.pg_core import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key= True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    role = Column(String)