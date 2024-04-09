class Director():
    """
    Director:
    in charge of actually builiding a product
    requires a concrete builder
    """

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder():
    """
    Abstract Builder:
    provides all necessary interfaces required in building an object
    """

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLarkBuilder(Builder):
    """
    Concrete Builder: (inheirits from abstract builder)
    implements the detail of the interfaces
    """

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"


class TeslaBuilder(Builder):
    """
    Concrete Builder: (inheirits from abstract builder)
    implements the detail of the interfaces
    """

    def add_model(self):
        self.car.model = "Tesla"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Electric engine"


class Car():
    """
    Product:
    the object being built
    """

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)


builder = SkyLarkBuilder()  # Concrete builder
director = Director(builder)  # Director using concrete builder
director.construct_car()  # director builds car
car = director.get_car()  # object is the object made by director
print(car)

# Try 2nd type of car (only added new concrete builder)
builder2 = TeslaBuilder()
director2 = Director(builder2)
director2.construct_car()
car = director2.get_car()
print(f'car 2 is {car}')
