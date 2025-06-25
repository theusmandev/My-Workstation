import psutil
import time
import platform
import pygetwindow as gw
import pyautogui
from plyer import notification
import datetime
import os
import json

# Configuration
TARGET_APP = "Code"  # Name of the target app (e.g., "Code" for VS Code)
IDLE_THRESHOLD = 60  # Seconds of no input to consider idle
DISTRACTION_THRESHOLD = 600  # Seconds (10 minutes) to trigger notification
LOG_FILE = "activity_log.json"
POINTS_PER_MINUTE = 10  # Focus points awarded per minute

# Initialize state
last_active_time = time.time()
last_app_switch_time = time.time()
current_app = ""
focus_points = 0
last_notification_time = 0
log_data = []

def get_active_window():
    """Get the title of the currently active window."""
    try:
        if platform.system() == "Windows":
            return gw.getActiveWindow().title
        elif platform.system() == "Linux":
            return gw.getActiveWindow().title
        elif platform.system() == "Darwin":  # macOS
            return gw.getActiveWindow().title
        return ""
    except Exception:
        return ""

def is_target_app_active(window_title):
    """Check if the target app is active based on window title."""
    return TARGET_APP in window_title

def detect_idle():
    """Detect if user is idle based on mouse and keyboard activity."""
    try:
        # Get current mouse position
        current_pos = pyautogui.position()
        # Store last position in a global variable
        global last_mouse_pos
        if 'last_mouse_pos' not in globals():
            last_mouse_pos = current_pos
            return False
        # Check if mouse moved
        if current_pos != last_mouse_pos:
            last_mouse_pos = current_pos
            return False
        # Note: pyautogui doesn't directly detect keyboard, rely on mouse for simplicity
        return True
    except Exception:
        return False

def log_activity(event_type, details):
    """Log activity with timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {
        "timestamp": timestamp,
        "event_type": event_type,
        "details": details,
        "focus_points": focus_points
    }
    log_data.append(log_entry)
    # Save to file
    try:
        with open(LOG_FILE, 'w') as f:
            json.dump(log_data, f, indent=2)
    except Exception as e:
        print(f"Error saving log: {e}")

def show_notification(title, message):
    """Show desktop notification."""
    global last_notification_time
    current_time = time.time()
    # Avoid spamming notifications
    if current_time - last_notification_time > 60:  # At least 1 minute between notifications
        notification.notify(
            title=title,
            message=message,
            app_name="Procrastination Tracker",
            timeout=10
        )
        last_notification_time = current_time

def award_focus_points(minutes):
    """Award focus points based on minutes of focus."""
    global focus_points
    points_earned = minutes * POINTS_PER_MINUTE
    focus_points += points_earned
    return points_earned

def main():
    global last_active_time, last_app_switch_time, current_app
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, 'r') as f:
                global log_data
                log_data = json.load(f)
        except Exception:
            log_data = []

    log_activity("start", f"Tracker started, monitoring for {TARGET_APP}")

    while True:
        try:
            # Get current window
            active_window = get_active_window()
            current_time = time.time()

            # Detect app switch
            if active_window != current_app:
                if current_app:
                    log_activity("app_switch", f"Switched from {current_app} to {active_window}")
                current_app = active_window
                last_app_switch_time = current_time

            # Check if user is idle
            if detect_idle():
                if current_time - last_active_time > IDLE_THRESHOLD:
                    log_activity("idle", "User is idle")
            else:
                last_active_time = current_time

            # Check if user is away from target app
            if not is_target_app_active(active_window) and active_window:
                time_away = current_time - last_app_switch_time
                if time_away > DISTRACTION_THRESHOLD:
                    show_notification(
                        "Focus Reminder",
                        f"You've been away from {TARGET_APP} for {int(time_away/60)} minutes. Come back!"
                    )
                    log_activity("distraction", f"Away from {TARGET_APP} for {int(time_away/60)} minutes")

            # Award focus points for staying in target app
            if is_target_app_active(active_window) and not detect_idle():
                minutes_focused = (current_time - last_app_switch_time) / 60
                if minutes_focused >= 1:
                    points = award_focus_points(int(minutes_focused))
                    if points > 0:
                        log_activity("focus", f"Earned {points} focus points")
                    last_app_switch_time = current_time  # Reset to avoid double-counting

            time.sleep(1)  # Check every second
        except KeyboardInterrupt:
            log_activity("stop", "Tracker stopped")
            print(f"Tracker stopped. Total focus points: {focus_points}")
            break
        except Exception as e:
            log_activity("error", f"Error occurred: {str(e)}")
            time.sleep(1)

if __name__ == "__main__":
    main()