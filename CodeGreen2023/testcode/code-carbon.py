from codecarbon import EmissionsTracker
tracker = EmissionsTracker()
tracker.start()
try:
     # Compute intensive code goes here
     _ = 1 + 1
finally:
     tracker.stop()











    # Start CodeCarbon tracker
    # tracker = EmissionsTracker()

    # try:
        # Start measuring emissions
        # tracker.start()

        # Run power-intensive task
    # result = power_intensive_task()
        # print("Result:", result)

    # finally:
    #     # Stop measuring emissions
    #     # tracker.stop()

    #     # Print the emissions report
    #     print("Carbon Emissions:", tracker._emissions)


if __name__ == "__main__":
    food()