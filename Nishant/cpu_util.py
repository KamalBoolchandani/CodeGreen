import pyJoules
import multiprocessing
import time

def cpu_intensive_task():
    while True:
        # Simulate CPU-bound computation
        result = 0
        for i in range(10**7):
            result += i

def simulate_high_cpu_utilization(num_processes):
    try:
        with pyJoules.EnergyMeter() as meter:
            processes = []

            # Create multiple processes to simulate parallel CPU-intensive tasks
            for _ in range(num_processes):
                process = multiprocessing.Process(target=cpu_intensive_task)
                process.start()
                processes.append(process)

            try:
                # Let the processes run for a certain duration
                time.sleep(10)

            except KeyboardInterrupt:
                # Stop the processes if the user interrupts (e.g., Ctrl+C)
                pass
            finally:
                # Terminate the processes
                for process in processes:
                    process.terminate()
                    process.join()

                # Get the energy consumption
                energy_consumption = meter.total_energy()
                print(f"Total Energy Consumption: {energy_consumption} Joules")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    num_processes = 6  # Adjust the number of processes based on your system capacity
    simulate_high_cpu_utilization(num_processes)
