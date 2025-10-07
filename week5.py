# ==============================
# Assignment 1: Design Your Own Class!
# ==============================

# Create a base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

    def phone_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")


# Add inheritance to explore polymorphism or encapsulation
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, strap_color):
        super().__init__(brand, model, storage)
        self.strap_color = strap_color

    def phone_info(self):  # Polymorphism: overriding parent method
        print(f"Smartwatch - Brand: {self.brand}, Model: {self.model}, Strap Color: {self.strap_color}")

    def track_steps(self, steps):
        print(f"{self.model} tracked {steps} steps today!")


# Create objects with unique values
phone1 = Smartphone("Apple", "iPhone 15", 256)
watch1 = Smartwatch("Samsung", "Galaxy Watch 6", 32, "Black")

# Use methods
phone1.phone_info()
phone1.make_call("08123456789")

watch1.phone_info()
watch1.track_steps(8500)


# ==============================
# Activity 2: Polymorphism Challenge!
# ==============================

class Vehicle:
    def move(self):
        print("Vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water...")

# Create a list of different vehicles
vehicles = [Car(), Plane(), Boat()]

# Demonstrate polymorphism
print("\n--- Vehicle Movements ---")
for v in vehicles:
    v.move()
