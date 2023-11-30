from carbontracker.tracker import CarbonTracker

def run_carbon_tracker_code(epochs, power_intensive_func):
    tracker = CarbonTracker(epochs=epochs)

    for epoch in range(epochs):
        tracker.epoch_start()
        
        power_result = power_intensive_func()
        print("Power Intensive Task Result:", power_result)
        
        tracker.epoch_end()

    tracker.stop()

# User provides the entire function as a string
user_provided_function = '''
def custom_task():
    result = sum(1 for _ in range((10 * multiplier)**7))
    return result
'''

# Remove leading and trailing triple quotes
user_provided_function = user_provided_function.strip("'''")

# Execute the user-provided function dynamically and make it globally accessible
exec(user_provided_function)

# Run CarbonTracker with the dynamically provided function
run_carbon_tracker_code(epochs=2, power_intensive_func=custom_task)
