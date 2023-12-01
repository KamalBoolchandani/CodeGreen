from carbontracker.tracker import CarbonTracker
import math

def power_intensive_task():
    result = 0
    for i in range(1, 10001):
        result += math.sqrt(i)
    return result

def measure_carbon_emissions(epochs):
    tracker = CarbonTracker(epochs=epochs)

    try:
        tracker.start()

        for epoch in range(epochs):
            tracker.epoch_start()
            
            # Run power-intensive task
            power_result = power_intensive_task()
            print(f"Power Intensive Task Result: {power_result}")

            tracker.epoch_end()

            # Print emissions for each epoch
            print(f"Epoch {epoch + 1} Carbon Emissions: {tracker.emissions}")

    finally:
        tracker.stop()

# Example usage with 5 epochs
measure_carbon_emissions(epochs=5)
