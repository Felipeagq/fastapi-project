from app.db.db_core import DataBase

class PostgresDataBase(DataBase):
    
    @staticmethod
    def create(**kwargs):
        db = kwargs.get("db")
        entity = kwargs.get("entity")
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity
    
    @staticmethod
    def read(**kwargs):
        db = kwargs.get("db")
        entity = kwargs.get("entity")
        param = kwargs.get("param")
        value = kwargs.get("value")
        if not param:
            return db.query(entity).all()
        return db.query(entity).filter(entity[param] == value)