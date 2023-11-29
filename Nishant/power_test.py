import pyJoules
import psutil
import time

from pyJoules.energy_meter import measure_energy

@measure_energy

def food():
    def power_intensive_task():
        result = 0
        for i in range(100**7):
            result += i
        return result

# Example usage
    result = power_intensive_task()
    print("Result:", result)

food()

# if __name__ == "__main__":
#     measure_power_consumption()
