from codecarbon import EmissionsTracker
def power_intensive_task():
    n = 1000**7
    return n * (n + 1) // 2


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