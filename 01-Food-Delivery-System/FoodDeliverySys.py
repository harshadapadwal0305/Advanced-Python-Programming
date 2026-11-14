# ---------------- DECORATOR ----------------
def decorate(fun):
    def inner(self, food, quantity):
        print("\nOrder operation started")
        fun(self, food, quantity)
        print("Order operation completed")
    return inner


# ---------------- FOOD ITEM ----------------
class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return self.name + " - Rs." + str(self.price)

    def __str__(self):
        return self.name + " - Rs." + str(self.price)


# ---------------- PIZZA ----------------
class Pizza(FoodItem):

    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def get_details(self):
        return "Pizza: " + self.name + " - " + self.size + " - Rs." + str(self.price)


# ---------------- BURGER ----------------
class Burger(FoodItem):

    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type

    def get_details(self):
        return "Burger: " + self.name + " - " + self.type + " - Rs." + str(self.price)


# ---------------- BEVERAGE ----------------
class Beverage(FoodItem):

    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def get_details(self):
        return "Beverage: " + self.name + " - " + self.size + " - Rs." + str(self.price)


# ---------------- RESTAURANT ----------------
class Restaurant:

    def __init__(self, restaurant_id, name):
        self.restaurant_id = restaurant_id
        self.name = name
        self.food_items = []

    def add_food(self, food):
        self.food_items.append(food)


# ---------------- CUSTOMER ----------------
class Customer:

    total_orders = 0

    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.order = []

    @decorate
    def place_order(self, food, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        self.order.append([food, quantity])
        Customer.total_orders += 1
        print("Order placed successfully")


    def bill(self):
        if len(self.order) == 0:
            raise ValueError("Order is empty")
        total = 0
        for item in self.order:
            food = item[0]
            quantity = item[1]
            total = total + food.price * quantity
        return total

    def show_order(self):
        if len(self.order) == 0:
            print("No items in order")
            return
        print("\n===== YOUR ORDER =====")
        for item in self.order:
            food = item[0]
            quantity = item[1]
            print(food.name, "x", quantity)


# ---------------- ITERATOR ----------------
class FoodIterator:

    def __init__(self, food_items):
        self.food_items = food_items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.food_items):
            food = self.food_items[self.index]
            self.index = self.index + 1
            return food
        else:
            raise StopIteration


# ---------------- GENERATOR ----------------
def order_generator(customer):
    for item in customer.order:
        food = item[0]
        quantity = item[1]
        yield food.name + " x " + str(quantity)


# ---------------- CREATE RESTAURANTS ----------------
r1 = Restaurant(1, "Food Palace")
r2 = Restaurant(2, "Tasty Bites")


# ---------------- ADD FOOD ----------------
r1.add_food(Pizza("Margherita", 200, "Medium"))
r1.add_food(Burger("Cheese Burger", 150, "Veg"))
r1.add_food(Beverage("Cold Coffee", 100, "Large"))

r2.add_food(Pizza("Farmhouse", 300, "Large"))
r2.add_food(Burger("Chicken Burger", 220, "Regular"))
r2.add_food(Beverage("Coke", 60, "Medium"))

restaurants = [r1, r2]


# ---------------- CUSTOMER ----------------
customer = Customer(101, "Rahul")


# ---------------- MENU ----------------
while True:
    print("\n===== FOOD DELIVERY SYSTEM =====")

    print("1. Show Restaurants")
    print("2. Show Food Items")
    print("3. Add Food to Order")
    print("4. Show Order")
    print("5. Calculate Bill")
    print("6. Generate Order Report")
    print("7. Exit")
    try:
        choice = int(input("Enter choice: "))
        # Show Restaurants
        if choice == 1:
            print("\n===== RESTAURANTS =====")
            for restaurant in restaurants:
                print(restaurant.restaurant_id, "-",restaurant.name)

        # Show Food Items
        elif choice == 2:
            restaurant_id = int(input("Enter Restaurant ID: "))
            found = False
            for restaurant in restaurants:
                if restaurant.restaurant_id == restaurant_id:
                    found = True
                    print("\n===== FOOD ITEMS =====")
                    iterator = FoodIterator(restaurant.food_items)
                    try:
                        while True:
                            food = next(iterator)
                            print(food.get_details())
                    except StopIteration:
                        print("End of food list")
                    break
            if found == False:
                print("Invalid restaurant ID")

        # Add Food
        elif choice == 3:
            restaurant_id = int(input("Enter Restaurant ID: "))
            found = False
            for restaurant in restaurants:
                if restaurant.restaurant_id == restaurant_id:
                    found = True
                    print("\nFood Items:")
                    for i in range(len(restaurant.food_items)):
                        print(i + 1,restaurant.food_items[i])
                    food_no = int(input("Enter Food Number: "))

                    if food_no < 1 or food_no > len(restaurant.food_items):
                        raise ValueError("Invalid food item")

                    quantity = int(input("Enter Quantity: "))
                    food = restaurant.food_items[food_no - 1]
                    customer.place_order(food,quantity)
                    break
            if found == False:
                print("Invalid restaurant ID")

        # Show Order
        elif choice == 4:
            customer.show_order()

        # Calculate Bill
        elif choice == 5:
            total = customer.bill()
            print("\nTotal Bill: Rs.", total)

        # Generator
        elif choice == 6:
            print("\n===== ORDER REPORT =====")
            report = order_generator(customer)
            for item in report:
                print(item)

        # Exit
        elif choice == 7:
            print("Thank you!")
            break
        else:
            print("Invalid choice")

    except ValueError as e:
        print("Error:", e)