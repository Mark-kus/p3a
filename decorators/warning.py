def new_record(func):
    def wrapper(*args, **kwargs):
        print("Ingreso de nuevo registro")
        return func(*args, **kwargs)

    return wrapper


def delete_record(func):
    def wrapper(*args, **kwargs):
        print("Eliminación de registro")
        return func(*args, **kwargs)

    return wrapper


def update_record(func):
    def wrapper(*args, **kwargs):
        print("Actualización de registro")
        return func(*args, **kwargs)

    return wrapper
