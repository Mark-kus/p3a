from sqlalchemy.orm import Session


def model_methods(cls: type):
    def get_all(db: Session):
        return db.query(cls).all()

    def get_by_id(db: Session, id: int):
        return db.query(cls).get(id)

    def get_by_filter(db: Session, **kwargs):
        return db.query(cls).filter_by(**kwargs).all()

    def get_by_filter_first(db: Session, **kwargs):
        return db.query(cls).filter_by(**kwargs).first()

    def create(db: Session, entity):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def update(db: Session, id: int, entity):
        pass

    def delete(db: Session, id: int):
        entity = db.query(cls).get(id)
        db.delete(entity)
        db.commit()
        return entity

    cls.get_all = staticmethod(get_all)
    cls.get_by_id = staticmethod(get_by_id)
    cls.get_by_filter = staticmethod(get_by_filter)
    cls.get_by_filter_first = staticmethod(get_by_filter_first)
    cls.create = staticmethod(create)
    cls.update = staticmethod(update)
    cls.delete = staticmethod(delete)
    return cls
