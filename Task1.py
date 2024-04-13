class Car:
    car_properties = []

    def __init__(self, model, year_of_release, manufacturer, engine_capacity,
color, price):
        self.model = model
        self.year_of_release = year_of_release
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price
        Car.car_properties.append(self)
    @classmethod
    def input_things(cls):
        model = input("enter car model ")
        year_of_release = int(input("enter year of release "))
        manufacturer = input("enter manufacturer ")
        engine_capacity = float(input("enter engine_capacity "))
        color = input("enter color ")
        price = int(input("enter price "))
        return cls(model, year_of_release, manufacturer, engine_capacity, color, price)
    @classmethod
    def output_things(cls):
        print("cars")
        for car in cls.car_properties:
            print(f"moder: {car.model},"
                  f" year of release: {car.year_of_release},"
                  f" manufacturer: {car.manufacturer},"
                  f" engine capacity: {car.color},"
                  f" price: {car.price}")

car1 = Car.input_things()

Car.output_things()