from carbontracker.tracker import CarbonTracker

def run_carbon_tracker_code(epochs, power_intensive_func):
    tracker = CarbonTracker(epochs=epochs)

    for epoch in range(epochs):
        tracker.epoch_start()
        
        # Evaluate the provided code as a function
        exec(power_intensive_func, globals())
        power_result = custom_task()
        
        print("Power Intensive Task Result: {}".format(power_result))
        
        tracker.epoch_end()

    tracker.stop()

# Get user-provided function as a string
user_provided_function = input("Enter Python code (e.g., 'def custom_task(): return 42'): ")
user_provided_function = user_provided_function.strip("'''")

# Wrap the user-provided function in a string for later execution
power_intensive_func = f'''
def custom_task():
    {user_provided_function}
'''

run_carbon_tracker_code(epochs=2, power_intensive_func=power_intensive_func)
