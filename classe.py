class Car:
    portas = 2
    def __init__(self, name):
        self.name = name

class Ferrari(Car):
    def __init__(self, model):
        super().__init__('Ferrari')
        self.model = model