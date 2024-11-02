from datetime import datetime
from models.log import LogModel


def new_record(func):
    def wrapper(*args, **kwargs):
        print("Ingreso de nuevo registro")
        log_entry = LogModel(description="Nuevo registro creado", created_at=datetime.now())
        args[0].add(log_entry)
        return func(*args, **kwargs)

    return wrapper


def delete_record(func):
    def wrapper(*args, **kwargs):
        print("Eliminación de registro")
        log_entry = LogModel(description="Registro eliminado", created_at=datetime.now())
        args[0].add(log_entry)
        return func(*args, **kwargs)

    return wrapper


def update_record(func):
    def wrapper(*args, **kwargs):
        print("Actualización de registro")
        log_entry = LogModel(description="Registro actualizado", created_at=datetime.now())
        args[0].add(log_entry)
        return func(*args, **kwargs)

    return wrapper
