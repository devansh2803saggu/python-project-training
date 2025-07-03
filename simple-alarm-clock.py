import time
import datetime
import sys

def alarm_clock():
    alarm_time = input("Set the alarm time (HH:MM, 24-hour format): ")
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        if not (0 <= alarm_hour < 24 and 0 <= alarm_minute < 60):
            print("Invalid time format. Please enter a valid time.")
            return
    except ValueError:
        print("Invalid input. Please enter time as HH:MM.")
        return

    print(f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}. Waiting...")

    while True:
        now = datetime.datetime.now()
        if now.hour == alarm_hour and now.minute == alarm_minute:
            print("\nWake up! Alarm ringing! ⏰")

            # Play beep sound (works on Windows)
            try:
                import winsound
                duration = 1000  # milliseconds
                freq = 440  # Hz
                for _ in range(5):  # beep 5 times
                    winsound.Beep(freq, duration)
                    time.sleep(0.2)
            except ImportError:
                # For other OSes, just print beep symbol multiple times
                for _ in range(5):
                    print('\a')  # terminal bell character
                    time.sleep(1)

            break
        time.sleep(10)  # check every 10 seconds

if __name__ == "__main__":
    alarm_clock()
