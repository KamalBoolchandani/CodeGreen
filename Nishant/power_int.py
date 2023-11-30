from codecarbon import EmissionsTracker

def custom_measure_energy(func):
    def wrapper(*args, **kwargs):
        tracker = EmissionsTracker()

        try:
            tracker.start()
            result = func(*args, **kwargs)
            return result
        finally:
            tracker.stop()
            print(f"Carbon Emissions (gCO2): {tracker._emissions}")
            print(f"Duration (s): {tracker.duration() if hasattr(tracker, 'duration') else 'N/A'}")

    return wrapper

# Power-intensive function
@custom_measure_energy
def power_intensive_function():
    result = 0
    for _ in range(10**7):
        result += 1  # This can be any computationally intensive operation
    return result

# Example usage:
result = power_intensive_function()
print("Result:", result)




# #ChatGPT
# Certainly! I'll provide an explanation for each line of the code:

# python
# Copy code
# from codecarbon import EmissionsTracker
# This line imports the EmissionsTracker class from the codecarbon library. EmissionsTracker is a class provided by CodeCarbon for tracking carbon emissions and related metrics during the execution of a program.
# python
# Copy code
# def custom_measure_energy(func):
# This line defines a decorator called custom_measure_energy. A decorator is a special type of function in Python that can be used to modify or extend the behavior of other functions. In this case, the decorator will be used to wrap another function with CodeCarbon tracking.
# python
# Copy code
#     def wrapper(*args, **kwargs):
# This line defines an inner function called wrapper inside the decorator. This function will replace the original function (func) when the decorator is applied. It takes any number of positional and keyword arguments (*args and **kwargs), allowing it to be used with functions of varying signatures.
# python
# Copy code
#         tracker = EmissionsTracker()
# This line creates an instance of the EmissionsTracker class. This tracker will be used to measure carbon emissions, energy consumption, and duration during the execution of the wrapped function.
# python
# Copy code
#         try:
#             tracker.start()
# This line starts the measurement of emissions using the start method of the EmissionsTracker instance. The try block ensures that even if an exception occurs during the execution of the wrapped function, the emissions tracking is properly stopped in the finally block.
# python
# Copy code
#             result = func(*args, **kwargs)
# This line calls the original function (func) with the provided arguments and captures its result.
# python
# Copy code
#             return result
# This line returns the result of the wrapped function.
# python
# Copy code
#         finally:
#             tracker.stop()
# This block of code is executed no matter what happens in the try block. It stops the emissions tracking using the stop method of the EmissionsTracker instance.
# python
# Copy code
#             print(f"Carbon Emissions (gCO2): {tracker.emissions}")
# This line prints the total carbon emissions measured by the EmissionsTracker during the execution of the wrapped function.
# python
# Copy code
#             print(f"Duration (s): {tracker.duration() if hasattr(tracker, 'duration') else 'N/A'}")
# This line prints the duration of the measurement in seconds. It uses the duration method of the EmissionsTracker instance, but it checks if the duration attribute exists before attempting to access it. If the attribute doesn't exist (for compatibility with different versions of CodeCarbon), it prints 'N/A' instead.
# python
# Copy code
#     return wrapper
# This line returns the wrapper function, which is now the modified version of the original function with emissions tracking.
# python
# Copy code
# @custom_measure_energy
# def power_intensive_function():
# This line applies the custom_measure_energy decorator to the power_intensive_function function. This means that when power_intensive_function is called, it will be wrapped by the functionality provided by the custom_measure_energy decorator.
# python
# Copy code
#     result = 0
#     for _ in range(10**7):
#         result += 1  # This can be any computationally intensive operation
#     return result
# This block of code represents a power-intensive function. It performs a large number of simple computations (adding 1 to result in a loop). This is just an example, and a real power-intensive function would likely involve more complex computations.
# python
# Copy code
# result = power_intensive_function()
# This line calls the power_intensive_function and captures its result.
# python
# Copy code
# print("Result:", result)
# This line prints the result of the power-intensive function. This line is outside the custom_measure_energy decorator, so it won't include the emissions tracking details in its output.
# I hope this explanation helps you understand each part of the code! If you have any specific questions about certain lines or concepts, feel free to ask.