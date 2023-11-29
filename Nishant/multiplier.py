from carbontracker.tracker import CarbonTracker

# Define the maximum number of epochs
max_epochs = 10  # You can set this to the desired value

def create_power_intensive_task(multiplier):
    def power_intensive_task():
        result = sum(1 for _ in range((10 * multiplier)**7))
        # If you need to perform additional computations, you can do so here
        return result

    return power_intensive_task

# Example usage with a multiplier of 2
multiplier_2_task = create_power_intensive_task(2)
result = multiplier_2_task()
print("Result:", result)


tracker = CarbonTracker(epochs=max_epochs)

# Training loop.
for epoch in range(max_epochs):
    tracker.epoch_start()
    
    # Your model training.

    # Adding a power-intensive task
    power_result = multiplier_2_task()
    print(f"Power Intensive Task Result: {power_result}")

    tracker.epoch_end()

# Optional: Add a stop in case of early termination before all monitor_epochs have
# been monitored to ensure that actual consumption is reported.
tracker.stop()
