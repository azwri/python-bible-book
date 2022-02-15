class Car:
    """A simple attempt to represent a car."""

    amount_cars = 0

    def __init__(self, manufacturer, model, hp) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.hp = hp
        self.__hidden_attribute = "This is a hidden attribute"
        Car.amount_cars += 1
    
    def __str__(self) -> str:
        return f"Manfacturer {self.manufacturer}, Model {self.model}, HP {self.hp}"

    def __del__(self):
        Car.amount_cars -= 1


class Mercedes(Car):

    def __init__(self, manufacturer, model, hp, city) -> None:
        super().__init__(manufacturer, model, hp)
        self.city = city

    def info(self):
        print(f"{self.manufacturer} {self.model} {self.hp} {self.city}" )


myCar = Mercedes("Mercedes", "S500", "500", "Berlin")
myCar.info()