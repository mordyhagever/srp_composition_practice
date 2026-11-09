from .engine import Engine
class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    def start(self):
        return f"{self.model}: engine {self.engine.get_hp()}hp started"
