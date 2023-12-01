from carbontracker.tracker import CarbonTracker

def run_carbon_tracker_code(epochs, power_intensive_func):
    tracker = CarbonTracker(epochs=epochs)

    for epoch in range(epochs):
        tracker.epoch_start()
        
        
        power_result = power_intensive_func()
        print("Power Intensive Task Result: {}".format(power_result))
        
        tracker.epoch_end()

    tracker.stop()

def power_intensive_task():
    rows = 100
    for i in range(rows):
        for j in range(i+1):
            print("* ", end="")
        print("\n")

run_carbon_tracker_code(epochs=2, power_intensive_func=power_intensive_task)
