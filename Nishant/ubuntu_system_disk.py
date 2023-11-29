import psutil

def get_disk_space_info():
    # Get disk partitions
    partitions = psutil.disk_partitions()

    print("Disk Space Information:")
    for partition in partitions:
        print("\nPartition: " + partition.device)
        try:
            partition_info = psutil.disk_usage(partition.mountpoint)
            print(f"  Total Space: {partition_info.total / (1024 ** 3):.2f} GB")
            print(f"  Used Space: {partition_info.used / (1024 ** 3):.2f} GB")
            print(f"  Free Space: {partition_info.free / (1024 ** 3):.2f} GB")
            print(f"  Percentage Used: {partition_info.percent:.2f}%")
        except PermissionError as e:
            print(f"  PermissionError: {e}")

if __name__ == "__main__":
    get_disk_space_info()
