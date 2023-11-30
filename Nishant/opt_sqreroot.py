from carbontracker.tracker import CarbonTracker

def run_carbon_tracker_code(epochs: int, power_intensive_func, *args, **kwargs):
    tracker = CarbonTracker(epochs=epochs)

    for epoch in range(epochs):
        tracker.epoch_start()
        
        power_result = power_intensive_func(*args, **kwargs)
        print(f"Power Intensive Task Result: {power_result}")
        
        tracker.epoch_end()

    tracker.stop()

def power_intensive_task(x: int, y: int, iterations: int = 10**7) -> int:
    result = 0
    for _ in range(iterations):
        result += (x ** y) + (y ** x)
    return result

if __name__ == "__main__":
    # Example inputs with larger numbers
    x_value = 10**2
    y_value = 10**3
    
    run_carbon_tracker_code(epochs=2, power_intensive_func=power_intensive_task, x=x_value, y=y_value)
