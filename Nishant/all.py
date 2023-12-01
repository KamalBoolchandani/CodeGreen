from codecarbon import EmissionsTracker
from carbontracker.tracker import CarbonTracker

def power_intensive_task(multiplier):
    return sum(1 for _ in range((10 * multiplier)**7))

def measure_energy_codecarbon(func):
    def wrapper(*args, **kwargs):
        tracker = EmissionsTracker()

        try:
            tracker.start()
            result = func(*args, **kwargs)
            return result
        finally:
            tracker.stop()
            print(f"Carbon Emissions (gCO2): {tracker._emissions}")
            print(f"Duration (s): {tracker.duration if hasattr(tracker, 'duration') else 'N/A'}")

    return wrapper

@measure_energy_codecarbon
def power_intensive_codecarbon():
    return power_intensive_task(2)  # Example usage with multiplier 2

# CarbonTracker usage
max_epochs = 2

@measure_energy_codecarbon
def power_intensive_carbontracker():
    return power_intensive_task(2)  # Example usage with multiplier 2

# Example usage
result_codecarbon = power_intensive_codecarbon()
result_carbontracker = 0

tracker = CarbonTracker(epochs=max_epochs)

for epoch in range(max_epochs):
    tracker.epoch_start()

    # Your model training.

    result_carbontracker += power_intensive_task(2)  # Example usage with multiplier 2

    tracker.epoch_end()

tracker.stop()

print("Result (CodeCarbon):", result_codecarbon)
print("Result (CarbonTracker):", result_carbontracker)
