class Vehicle:
    __model = ""
    __engine_power = 0
    __color = ""

    __color_variants = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = power

    def get_model(self):
        return f"Model is: {self.__model}"

    def get_horsepower(self):
        return f"Power is: {self.__engine_power}"

    def get_color(self):
        return f"Color is: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Owner is: {self.owner}")

    def set_color(self, new_color):
        if str(new_color).lower() in str(self.__color_variants).lower() and isinstance(new_color, str):
            self.__color = new_color
        else:
            print(f"You cannot change color on: {new_color}")


class Sedan(Vehicle):
    __passengers_limit = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()