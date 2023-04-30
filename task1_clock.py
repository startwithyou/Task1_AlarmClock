import time
import winsound

# Set the time for the alarm
alarm_time = input("Enter the time in 'HH:MM:SS AM/PM' format: ")

# Convert the time to 24-hour format
alarm_time = time.strftime("%H:%M:%S", time.strptime(alarm_time, "%I:%M:%S %p"))

while True:
    # Get the current time in 24-hour format
    current_time = time.strftime("%H:%M:%S")

    # Check if the current time matches the alarm time
    if current_time == alarm_time:
        # Play the alarm sound
        frequency = 2500  # Set frequency to 2500 hertz
        duration = 1000  # Set duration to 1000 milliseconds (1 second)
       
        winsound.Beep(frequency, duration)
        print("Wake up!")
        break

    # Wait for 1 second before checking the time again
    time.sleep(1)