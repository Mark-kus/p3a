class Observer:
    def update(self, message: str):
        raise NotImplementedError("Delegación de actualización")


class EmailNotifier(Observer):
    def __init__(self, obj):
        self.watched = obj
        self.watched.attach(self)

    def update(self, message: str):
        print(f"Email enviado con el mensaje: {message}")


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)