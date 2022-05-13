import time
import os


def timer(hours, minutes, seconds):
    while hours >= 0 and minutes >= 0 and seconds >= 0:
        time.sleep(1)
        os.system("cls")
        if seconds == 0 and minutes == 0 and hours == 0:
            break

        seconds = seconds - 1

        if seconds == -1 and minutes > 0:
            minutes -= 1
            seconds = 59

        if minutes == 0 and hours > 0:
            hours -= 1
            minutes = 59
            seconds = 59

        print(f"{hours}:{minutes}:{seconds}")


timer(0, 1, 30)
