from codecarbon import EmissionsTracker
from pyJoules.energy_meter import measure_energy

@measure_energy
def power_intensive_task():
    n = 100**7
    return n * (n + 1) // 2

@measure_energy
def food():
    # Start CodeCarbon tracker
    tracker = EmissionsTracker()

    try:
        # Start measuring emissions
        tracker.start()

        # Run power-intensive task
        result = power_intensive_task()
        print("Result:", result)

    finally:
        # Stop measuring emissions
        tracker.stop()

        # Print the emissions report
        print("Carbon Emissions:", tracker._emissions)

if __name__ == "__main__":
    food()
