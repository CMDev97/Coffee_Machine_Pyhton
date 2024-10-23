msg_action_machine = "Write action (buy, fill, take, remaining, exit): "
msg_buy_product = "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"

msg_many_water = "Write how many ml of water you want to add:"
msg_many_milk = "Write how many ml of milk you want to add: "
msg_many_grams_coffe = "Write how many grams of coffee beans you want to add:"
msg_many_cups = "Write how many disposable cups you want to add:"

all_msg = [msg_many_water, msg_many_milk, msg_many_grams_coffe, msg_many_cups]

msg_yes_dispense = "Yes, I can make that amount of coffee"
msg_yes_more_dispense = "Yes, I can make that amount of coffee (and even {} more than that)"
msg_no_dispense = "No, I can make only {} cups of coffee"


class CoffeeMachine:
    COFFE = (250, 0, 16, 1, 4)
    MILK = (350, 75, 20, 1, 7)
    CAPUCCINO = (200, 100, 12, 1, 6)

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550

    @staticmethod
    def get_type_of_product(type_product):
        if type_product == '1':
            return CoffeeMachine.COFFE
        if type_product == '2':
            return CoffeeMachine.MILK
        if type_product == '3':
            return CoffeeMachine.CAPUCCINO
        return None

    def get_missing_ingredient(self, water, milk, coffee, cups):
        if self.water < water:
            return 'water'
        if self.milk < milk:
            return 'milk'
        if self.coffee < coffee:
            return 'coffee'
        if self.cups < cups:
            return 'cups'
        return ''

    def take_money(self):
        money = self.money
        self.money = 0
        return money

    def fill_machine(self, water, milk, coffee, cups):
        self.water += water
        self.milk += milk
        self.coffee += coffee
        self.cups += cups

    def disposable_product(self, water, milk, coffee, cups, money):
        self.water -= water
        self.milk -= milk
        self.coffee -= coffee
        self.cups -= cups
        self.money += money

    def __str__(self):
        return f"""{self.water} ml of water
{self.milk} ml of milk
{self.coffee} g of coffee beans
{self.cups} disposable cups 
${self.money} of money"""


class PrinterDisplay:

    @staticmethod
    def machine_choosing():
        print(msg_action_machine)
        return input()

    @staticmethod
    def machine_buying():
        print(msg_buy_product)
        return input()

    @staticmethod
    def print_missing_ingredients(ingredient):
        if ingredient == 'water':
            print("Sorry, not enough water!")
        elif ingredient == 'milk':
            print("Sorry, not enough milk!")
        elif ingredient == 'coffee':
            print("Sorry, not enough grams of coffee!")
        elif ingredient == 'cups':
            print("Sorry, not enough cups of coffee!")

    @staticmethod
    def print_take_money(money_to_take):
        print(f"I gave you ${money_to_take}")

    @staticmethod
    def print_enough_resources():
        print("I have enough resources, making you a coffee!")

    @staticmethod
    def print_status_machine(coffee_machine: CoffeeMachine):
        print("The coffee machine has:")
        print(coffee_machine)

    @staticmethod
    def read_input_ingredients_to_fill() -> tuple:
        input_array = []
        for i, msg in enumerate(all_msg):
            print(msg)
            command_input = int(input())
            input_array.append(command_input)
        return tuple(input_array)


class CoffeMachineController:

    def __init__(self):
        self.coffee_machine = CoffeeMachine()

    def _buy_action(self):
        user_choose = PrinterDisplay.machine_buying()
        if user_choose != "back":
            product = CoffeeMachine.get_type_of_product(user_choose)
            if product is not None:
                water, milk, coffe, cups, price = product
                missing_ingredient = self.coffee_machine.get_missing_ingredient(water, milk, coffe, cups)
                if len(missing_ingredient) == 0:
                    self.coffee_machine.disposable_product(water, milk, coffe, cups, price)
                    PrinterDisplay.print_enough_resources()
                else:
                    PrinterDisplay.print_missing_ingredients(missing_ingredient)

    def _fill_action(self):
        water, milk, coffe, cups = PrinterDisplay.read_input_ingredients_to_fill()
        self.coffee_machine.fill_machine(water, milk, coffe, cups)

    def _take_action(self):
        money_take = self.coffee_machine.take_money()
        PrinterDisplay.print_take_money(money_take)

    def _remaining_action(self):
        PrinterDisplay.print_status_machine(self.coffee_machine)

    def handler(self):
        while True:
            user_choose = PrinterDisplay.machine_choosing()
            if user_choose == 'buy':
                self._buy_action()
            elif user_choose == 'fill':
                self._fill_action()
            elif user_choose == 'take':
                self._take_action()
            elif user_choose == 'remaining':
                self._remaining_action()
            elif user_choose == 'exit':
                break


if __name__ == "__main__":
    controller = CoffeMachineController()
    controller.handler()
