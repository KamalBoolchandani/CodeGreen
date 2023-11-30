from codecarbon import EmissionsTracker
from carbontracker.tracker import CarbonTracker

def custom_measure_energy(func):
    def wrapper(*args, **kwargs):
        tracker = EmissionsTracker()

        try:
            tracker.start()
            result = func(*args, **kwargs)
            return result
        finally:
            tracker.stop()
            print(f"Carbon Emissions (gCO2): {tracker.final_emissions}")
            print(f"Duration (s): {tracker.duration() if hasattr(tracker, 'duration') else 'N/A'}")

    return wrapper

@custom_measure_energy
def power_intensive_multiply_decimals(x, y, iterations=10**6):
    result = 1.0
    for _ in range(iterations):
        result *= x * y
    return result

if __name__ == "__main__":
    # Default decimal inputs
    x = 0.123456789
    y = 0.456987654
    
    result = power_intensive_multiply_decimals(x, y)
    print("Decimal Multiplication Result:", result)
