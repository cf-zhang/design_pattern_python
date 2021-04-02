

class Packing:
    def pack(self)->str:
        pass


class Wrapper(Packing):
    def pack(self)->str:
        return 'Wrapper'
    def __str__(self):
        return 'Wrapper'

class Bottle(Packing):
    def pack(self)->str:
        return 'Bottle'
    def __str__(self):
        return 'Bottle'

class Item:
    def name(self)->str:
        pass
    def packing(self)->Packing:
        pass
    def price(self) -> float:
        pass

class Burger(Item):
    def packing(self)->Packing:
        return Wrapper()

    def price(self)->float:
        pass

class ColdDrink(Item):
    def packing(self)->Packing:
        return Bottle()

    def price(self)->float:
        pass

class VegBurger(Burger):
    def price(self)->float:
        return 25.0

    def name(self)->str:
        return "Veg Burger"


class ChickenBurger(Burger):
    def price(self) -> float:
        return 50.0

    def name(self) -> str:
        return "Chicken Burger"


class Coke(ColdDrink):
    def price(self) -> float:
        return 30.0

    def name(self) -> str:
        return "Coke"


class Pepsi(ColdDrink):
    def price(self) -> float:
        return 36.0

    def name(self) -> str:
        return "Pepsi"

class Meal:
    items = list()

    def addItem(self, item: 'Item'):
        self.items.append(item)

    def getCost(self)->float:
        cost = 0.0
        for x in self.items:
            cost += x.price()
        return cost

    def showItems(self):
        for x in self.items:
            print(str(x.name()))
            print(str(x.packing()))
            print(str(x.price()))


class MealBuilder:
    def prepareVegMeal(self):
        meal = Meal()
        meal.addItem(VegBurger())
        meal.addItem(Coke())
        return meal

    def prepareNonVegMeal(self):
        meal = Meal()
        meal.addItem(ChickenBurger())
        meal.addItem(Pepsi())
        return meal




meal_builder = MealBuilder()
meal = meal_builder.prepareNonVegMeal()
meal.showItems()


