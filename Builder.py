from abc import ABC, abstractmethod

class PizzaBuilder(ABC):
    def __init__(self):
        self.pizza = []

    @abstractmethod
    def add_base(self): pass

    @abstractmethod
    def add_sauce(self): pass

    @abstractmethod
    def add_toppings(self): pass

    def get_pizza(self):
        return self.pizza

class MeatLoversPizzaBuilder(PizzaBuilder):
    def add_base(self):
        self.pizza.append("Thick crust base")

    def add_sauce(self):
        self.pizza.append("BBQ sauce")

    def add_toppings(self):
        self.pizza.append("Pepperoni, sausage, bacon")

class VeganPizzaBuilder(PizzaBuilder):
    def add_base(self):
        self.pizza.append("Thin crust base")

    def add_sauce(self):
        self.pizza.append("Tomato basil sauce")

    def add_toppings(self):
        self.pizza.append("Mushrooms, olives, bell peppers, onions")

class PizzaChef:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_pizza(self):
        self.builder.add_base()
        self.builder.add_sauce()
        self.builder.add_toppings()


def show_pizza(builder):
    print("\n Custom Pizza:")
    for item in builder.get_pizza():
        print(" -", item)


meat_builder = MeatLoversPizzaBuilder()
veggie_builder = VeganPizzaBuilder()

chef = PizzaChef(meat_builder)
chef.make_pizza()
show_pizza(meat_builder)

chef = PizzaChef(veggie_builder)
chef.make_pizza()
show_pizza(veggie_builder)
