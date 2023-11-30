from codecarbon import EmissionsTracker
from pyJoules.energy_meter import measure_energy as joules_measure_energy

def custom_measure_energy(func):
    # Your implementation of the decorator goes here
    pass

# This function adds two numbers
def power_intensive_task(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Cannot divide by zero.")
        return None

# Function to perform calculations based on user input
def perform_calculation(choice, num1, num2):
    if choice == '1':
        return power_intensive_task(num1, num2)
    elif choice == '2':
        return subtract(num1, num2)
    elif choice == '3':
        return multiply(num1, num2)
    elif choice == '4':
        return divide(num1, num2)
    else:
        return None

# Main calculator loop
while True:
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Start CodeCarbon tracker
        tracker = EmissionsTracker()

        try:
            # Start measuring emissions
            tracker.start()

            # Perform the calculation
            result = perform_calculation(choice, num1, num2)

            if result is not None:
                print(f"Result: {result}")

        finally:
            # Stop measuring emissions
            tracker.stop()

            # Print the emissions details
            print(f"Carbon Emissions (gCO2): {tracker._emissions}")
            print(f"Energy Consumption (Joules): {tracker.energy()}")
            print(f"Duration (s): {tracker.duration()}")

        # check if the user wants another calculation
        # break the loop if the answer is no
        next_calculation = input("Let's do the next calculation? (yes/no): ").lower()
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")
