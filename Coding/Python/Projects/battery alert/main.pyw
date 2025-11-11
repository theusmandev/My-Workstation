import psutil
import time
import winsound

def battery_alert(threshold=86):
    alerted = False
    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = battery.power_plugged

        print(f"Battery: {percent}% | Plugged: {plugged}", end="\r")

        if percent >= threshold and plugged and not alerted:
            print(f"\n⚡ Battery is {percent}% charged! Please unplug the charger.")
            for _ in range(3):
                winsound.Beep(1000, 700)
                time.sleep(0.5)
            alerted = True  # alert only once
        elif not plugged:
            alerted = False  # reset alert once unplugged

        time.sleep(30)

if __name__ == "__main__":
    battery_alert()
