# Import libraries

import time
from pydub import AudioSegment
from pydub.playback import play

def counter(time_in_minutes):
    """
    Define a function for time counting
    until the user input is reached.
    """
    time_in_seconds = 60 * time_in_minutes
    seconds = 1 # start counting from 1
    time.sleep(1) # delay for 1 second
    while seconds < time_in_seconds:
        if seconds == 1:
            print(str(seconds) + " second has passed.")
        else:
            print(str(seconds) + " seconds have passed.")
        seconds += 1
        time.sleep(1) # delay for 1 second
    print("The allocated time is up.")

time_in_minutes = float(input("Set your Pomodoro time cycle in minutes: "))

counter(time_in_minutes)

song = AudioSegment.from_wav("357_magnum.wav")
play(song)