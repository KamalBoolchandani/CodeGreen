from carbontracker.tracker import CarbonTracker

# Define the maximum number of epochs
max_epochs = 0  # You can set this to the desired value

def power_intensive_task():
    print("Select operation:")
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
            return

        if choice == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid Input")

# Example usage
power_intensive_task()


tracker = CarbonTracker(epochs=max_epochs)

# Training loop.
for epoch in range(max_epochs):
    tracker.epoch_start()
    
    # Your model training.

    # Adding a power-intensive task
    power_result = power_intensive_task()
    print(f"Power Intensive Task Result: {power_result}")

    tracker.epoch_end()

# Optional: Add a stop in case of early termination before all monitor_epochs have
# been monitored to ensure that actual consumption is reported.
tracker.stop()
