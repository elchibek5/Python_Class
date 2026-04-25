from car import Car
from book import Book

def main():
    # Example for Book
    my_book = Book("Python Basics", "Gaddis", "Pearson")
    print(my_book)

    # Logic for Car
    my_car = Car(2014, "Toyota Prius")

    print("\nAccelerating...")
    for _ in range(5):
        my_car.accelerate()
        print(f"Current speed: {my_car.get_speed()}")

    print("\nBraking...")
    for _ in range(5):
        my_car.brake()
        print(f"Current speed: {my_car.get_speed()}")

if __name__ == "__main__":
    main()