from carbontracker.tracker import CarbonTracker

# Define the maximum number of epochs
max_epochs = 5  # You can set this to the desired value

def power_intensive_task():
    result = 0
    for _ in range(10**10):
        result += 1  # Replace this with your actual power-intensive computation
    return result

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
