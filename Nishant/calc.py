import pyJoules
import psutil
import time

# def measure_power_consumption():
#     try:
#         # Initialize the power monitoring library (if needed)
#         # pyJoules.initialize()

#         # Assuming you're using psutil for CPU usage
#         cpu_percent = psutil.cpu_percent(interval=1)

#         # Assuming you're using pyJoules for power measurement
#         # Replace the following line with the actual method or class from pyJoules
#         power_measurement = 10.0  # Replace with actual measurement

#         print(f"CPU Usage: {cpu_percent}%")
#         print(f"Power Consumption: {power_measurement} Watts")

#     except Exception as e:
#         print(f"Error: {e}")

#     finally:
#         pass
#         # Cleanup (if needed)
#         # pyJoules.finalize()



from pyJoules.energy_meter import measure_energy

@measure_energy
# def food():
#     food1="ancd"
#     food2="hdkbd"
#     food3=food1+food2
#     print("cpu utilization is")++.
#     print(food3)
# 	# Instructions to be evaluated.

# food()

def food():
    # This function adds two numbers
    def add(x, y):
        return x + y

# This function subtracts two numbers
    def subtract(x, y):
        return x - y

# This function multiplies two numbers
    def multiply(x, y):
        return x * y

# This function divides two numbers
    def divide(x, y):
        return x / y


    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print# This function adds two numbers
    def add(x, y):
        return x + y

# This function subtracts two numbers
    def subtract(x, y):
        return x - y

# This function multiplies two numbers
    def multiply(x, y):
        return x * y

# This function divides two numbers
    def divide(x, y):
        return x / y


    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
    # take input from the user
        choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
              break
        else:
            print("Invalid Input")
    # Instructions to be evaluated.

food()

# if __name__ == "__main__":
#     measure_power_consumption()
