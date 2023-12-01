
from carbontracker.tracker import CarbonTracker

max_epochs = 2  
def create_power_intensive_task(multiplier):
    def power_intensive_task():
        return sum(1 for _ in range((10 * multiplier)**7))
    
    return power_intensive_task

multiplier_2_task = create_power_intensive_task(2)
result = multiplier_2_task()
print("Result:", result)

tracker = CarbonTracker(epochs=max_epochs)

for epoch in range(max_epochs):
    tracker.epoch_start()
    

    power_result = multiplier_2_task()
    print("Power Intensive Task Result: {}".format(power_result))
    
    tracker.epoch_end()

    
tracker.stop()
