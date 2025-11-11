'''
The app runs quietly in background.

It pauses itself until you plug in the charger.

Once you plug in, it starts monitoring.

When unplugged again, it waits silently.
'''


import psutil
import time
import winsound

def battery_alert(threshold=90):
    alerted = False

    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = battery.power_plugged

        if not plugged:
            # If unplugged, wait and check again
            print("Charger not plugged in, waiting...", end="\r")
            time.sleep(10)
            continue

        # Only monitor when charging
        print(f"Battery: {percent}% | Plugged: {plugged}", end="\r")

        if percent >= threshold and plugged and not alerted:
            print(f"\n⚡ Battery is {percent}% charged! Please unplug the charger.")
            for _ in range(3):
                winsound.Beep(1000, 700)
                time.sleep(0.5)
            alerted = True
        elif not plugged:
            alerted = False

        time.sleep(30)


if __name__ == "__main__":
    battery_alert()
