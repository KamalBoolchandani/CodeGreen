import sqlite3
from datetime import datetime
from carbontracker.tracker import CarbonTracker

max_epochs = 1
tracker = CarbonTracker(epochs=max_epochs)

# Training loop.
tracker.epoch_start()
    
# Connect to the SQLite database
conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()

# Create a table to store attendance records if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT,
        date TEXT,
        status TEXT
    )
''')
conn.commit()

def mark_attendance(student_id):
    date_today = datetime.today().strftime('%Y-%m-%d')
    cursor.execute('''
        INSERT INTO attendance (student_id, date)
        VALUES (?, ?, ?)
    ''', (student_id, date_today))
    conn.commit()

def view_attendance():
    cursor.execute('SELECT * FROM attendance')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    
    print("\nAttendance Management System")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = '1' #input("Enter your choice: ")

    if choice == '1':
        student_id = 24 #input("Enter student ID: ")
        #status = Present.capitalize()
        #mark_attendance(student_id)
        print("Attendance marked successfully!")

    elif choice == '2':
        view_attendance()

    elif choice == '3':
        print("Exiting...")

    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

# Close1
#  the database connection
#input("Enter attendance status (Present/Absent): ")

tracker.epoch_end()

# Optional: Add a stop in case of early termination before all monitor_epochs has
# been monitored to ensure that actual consumption is reported.
tracker.stop()