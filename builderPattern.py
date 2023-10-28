class Meal:
    def __init__(self):
        self.appetizer = ""
        self.main_course = ""
        self.dessert = ""

    def __str__(self):
        return f"Vorspeise: {self.appetizer}, Hauptgericht: {self.main_course}, Nachspeise: {self.dessert}"

class MealBuilder:
    def __init__(self):
        self.meal = Meal()
    def build_appetizer(self):
        pass
    def build_main_course(self):
        pass
    def build_dessert(self):
        pass

class BurgerMealBuilder(MealBuilder):
    def build_appetizer(self):
        self.meal.appetizer = "Kartoffelchips"
    def build_main_course(self):
        self.meal.main_course = "Hamburger"
    def build_dessert(self):
        self.meal.dessert = "Eis"

class PastaMealBuilder(MealBuilder):
    def build_appetizer(self):
        self.meal.appetizer = "Bruschetta"
    def build_main_course(self):
        self.meal.main_course = "Spaghetti Carbonara"
    def build_dessert(self):
        self.meal.dessert = "Tiramisu"

class SaladMealBuilder(MealBuilder):
    def build_appetizer(self):
        self.meal.appetizer = "Gemischter Salat"
    def build_main_course(self):
        self.meal.main_course = "Caesar-Salat"
    def build_dessert(self):
        self.meal.dessert = "Obstsalat"

class LasagnaMealBuilder(MealBuilder):
    def build_appetizer(self):
        self.meal.appetizer = "Knoblauchbrot"
    def build_main_course(self):
        self.meal.main_course = "Lasagne"
    def build_dessert(self):
        self.meal.dessert = "Panna Cotta"

class PizzaMealBuilder(MealBuilder):
    def build_appetizer(self):
        self.meal.appetizer = "Caprese-Salat"
    def build_main_course(self):
        self.meal.main_course = "Pizza Margherita"
    def build_dessert(self):
        self.meal.dessert = "Tiramisu"

class Waiter:
    def __init__(self, builder):
        self.builder = builder

    def construct_meal(self):
        self.builder.build_appetizer()
        self.builder.build_main_course()
        self.builder.build_dessert()

    def get_meal(self):
        return self.builder.meal

if __name__ == "__main__":
    # Erstellen von Mahlzeiten
    burger_builder = BurgerMealBuilder()
    pasta_builder = PastaMealBuilder()
    salad_builder = SaladMealBuilder()
    lasagna_builder = LasagnaMealBuilder()
    pizza_builder = PizzaMealBuilder()

    for builder in [burger_builder, pasta_builder, salad_builder, lasagna_builder, pizza_builder]:
        waiter = Waiter(builder)
        waiter.construct_meal()
        meal = waiter.get_meal()
        print("\nBestellte Mahlzeit:")
        print(meal)
